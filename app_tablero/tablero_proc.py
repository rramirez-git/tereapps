from os import path
import pandas as pd
import re
from datetime import datetime
from django.db import connection
from MySQLdb._exceptions import ProgrammingError

from zend_django.models import ParametroSistema
from .models import Tablero, Cuenta, Estadistico, EstadisticoAnual

class TableroProc():
    tabl = None
    path_arch = ''
    hc = ''
    hdr = 0
    psos_thrd = []

    def __init__(self, tablero, hoja_cuentas='TDcuentas', headers=3):
        if isinstance(tablero, Tablero):
            self.tabl = tablero
        else:
            self.tabl = Tablero.objects.get(nombre=tablero)
        self.hc = hoja_cuentas
        self.hdr = headers

    def checkInFTP(self):
        ftp_dir = ParametroSistema.get('AppTablero', 'ruta_abs_ftp')
        self.path_arch = path.join(ftp_dir, self.tabl.nombre_de_archivo)
        return path.isfile(self.path_arch)

    def dataFrame_from_file(self):
        if self.checkInFTP():
            df = pd.read_excel(self.path_arch, self.hc, index_col=None, engine='openpyxl', header=self.hdr)
            return df.rename(columns={
                'Unnamed: 0': 'pre_cve',
                'Unnamed: 1': 'pre_posicion',
                ' ': 'pre_cve_2',
            })
        return None

    def process(self):
        df = self.dataFrame_from_file()
        if df is None:
            return False
        periodos = self.get_period_cols(df)
        anios = self.get_year_cols(df)
        with connection.cursor() as cursor:
            for query in [
                    f"""DELETE FROM app_tablero_estadistico WHERE cuenta_id IN (SELECT cuenta_id FROM app_tablero_cuenta WHERE tablero_id = {self.tabl.pk});""",
                    f"""DELETE FROM app_tablero_estadisticoanual WHERE cuenta_id IN (SELECT cuenta_id FROM app_tablero_cuenta WHERE tablero_id = {self.tabl.pk});"""]:
                cursor.execute(query);
        df = df[df[['Cuenta', 'Nivel']].notnull().all(1)]
        df = df[df['Nivel'] > 0]
        df['Nivel'] = df['Nivel'].astype(int)
        df['cuenta_id'] = df.apply(self.process_fila, axis=1, periodos=periodos)
        for per in periodos:
            df2sgbd = df[['cuenta_id', per]]
            df2sgbd['periodo'] = f'{per}-01'
            df2sgbd['cantidad'] = df[per]
            df2sgbd = df2sgbd.drop([per,], axis=1)
            Estadistico.objects.bulk_create(
                Estadistico(**vals) for vals in df2sgbd.to_dict('records')
            )
        for per in anios:
            df2sgbd = df[['cuenta_id', per]]
            df2sgbd['anio'] = int(per)
            df2sgbd['cantidad'] = df[per]
            df2sgbd = df2sgbd.drop([per,], axis=1)
            EstadisticoAnual.objects.bulk_create(
                EstadisticoAnual(**vals) for vals in df2sgbd.to_dict('records')
            )
        return True

    def get_period_cols(self, df):
        reg_exp = re.compile(r"^\d{4}-\d{2}$")
        cols = []
        for col in df.columns.tolist():
            try:
               if reg_exp.match(col):
                   cols.append(col)
            except TypeError:
                pass
        return cols

    def get_year_cols(self, df):
        reg_exp = re.compile(r"^\d{4}$")
        cols = []
        for col in df.columns.tolist():
            try:
                if reg_exp.match(str(col)):
                    cols.append(col)
            except TypeError:
                pass
        return cols

    def process_fila(self, fila, periodos):
        if fila.Cuenta:
            try:
                cta_num = str(int(fila.Cuenta))
            except ValueError:
                cta_num = str(fila.Cuenta)
            cta = Cuenta.objects.get_or_create(
                nivel=fila.Nivel,
                entidad=fila.Entidad,
                cuenta=cta_num,
                descripcion=fila.Descripcion,
                formato=str(int(fila.Formato)),
                tablero=self.tabl,
                pre_cve=fila.pre_cve,
                pre_posicion=fila.pre_posicion,
                pre_cve_2=fila.pre_cve_2
            )[0]
            return cta.pk
        return None
