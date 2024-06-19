from django.contrib.auth.models import Permission

from app_valuacion_puestos.models import Factor
from app_valuacion_puestos.models import Nivel
from app_valuacion_puestos.models import Puesto
from app_valuacion_puestos.models import Tabulador
from zend_django.models import MenuOpc
from zend_django.models import ParametroUsuario
from zend_django.parametros_models import PARAM_TYPES


def int2romman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman += syb[i]
            num -= val[i]
        i += 1
    return roman


def migration():
    vp = MenuOpc.objects.get_or_create(
        nombre="Valuacion de Puestos", posicion=1,
        padre=None, vista='idx_tereapp_valuacion_de_puestos')[0]
    items = {}
    items['puesto'] = MenuOpc.objects.get_or_create(
        nombre="Puestos", posicion=1, padre=vp, vista="puesto_list")[0]
    items['factor'] = MenuOpc.objects.get_or_create(
        nombre="Factores", posicion=2, padre=vp, vista="factor_list")[0]

    for obj, mnuOpc in items.items():
        ParametroUsuario.objects.get_or_create(
            seccion='basic_search', nombre=obj, valor_default='',
            tipo=PARAM_TYPES['CADENA'], es_multiple=False)
        mnuOpc.permisos_requeridos.set([
            Permission.objects.get(codename=f"add_{obj}"),
            Permission.objects.get(codename=f"change_{obj}"),
            Permission.objects.get(codename=f"delete_{obj}"),
            Permission.objects.get(codename=f"view_{obj}"),
        ])

    tab = Tabulador.objects.all().first()

    afanadora = Puesto.objects.get_or_create(
        puesto="Afanadora", posicion=1,
        estatus=True, tabulador=tab)[0]
    facturista = Puesto.objects.get_or_create(
        puesto="Facturista", posicion=2,
        estatus=True, tabulador=tab)[0]
    jefe_de_personal = Puesto.objects.get_or_create(
        puesto="Jefe de Personal", posicion=3,
        estatus=True, tabulador=tab)[0]
    jefe_de_almacen = Puesto.objects.get_or_create(
        puesto="Jefe de Almacen", posicion=4,
        estatus=True, tabulador=tab)[0]
    sub_jefe_de_almacen = Puesto.objects.get_or_create(
        puesto="Sub Jefe de Almacen", posicion=5,
        estatus=True, tabulador=tab)[0]
    montacarguista = Puesto.objects.get_or_create(
        puesto="Montacarguista", posicion=6,
        estatus=True, tabulador=tab)[0]
    almacenista = Puesto.objects.get_or_create(
        puesto="Almacenista", posicion=7,
        estatus=True, tabulador=tab)[0]
    chofer_de_reparto = Puesto.objects.get_or_create(
        puesto="Chofer de Reparto", posicion=8,
        estatus=True, tabulador=tab)[0]
    auxiliar_de_aduana = Puesto.objects.get_or_create(
        puesto="Auxiliar de Aduana", posicion=9,
        estatus=True, tabulador=tab)[0]
    auxiliar_de_ventas = Puesto.objects.get_or_create(
        puesto="Auxiliar de Ventas", posicion=10,
        estatus=True, tabulador=tab)[0]
    auxiliar_atención_a_clientes = Puesto.objects.get_or_create(
        puesto="Auxiliar Atención a Clientes", posicion=11,
        estatus=True, tabulador=tab)[0]
    mensajero_cobrador = Puesto.objects.get_or_create(
        puesto="Mensajero-Cobrador", posicion=12,
        estatus=True, tabulador=tab)[0]
    cobrador = Puesto.objects.get_or_create(
        puesto="Cobrador", posicion=13,
        estatus=True, tabulador=tab)[0]
    auxiliar_de_cobranza = Puesto.objects.get_or_create(
        puesto="Auxiliar de Cobranza", posicion=14,
        estatus=True, tabulador=tab)[0]
    supervisor_de_crédito_y_cobranza = Puesto.objects.get_or_create(
        puesto="Supervisor de Crédito y Cobranza", posicion=15,
        estatus=True, tabulador=tab)[0]
    auxiliar_contable = Puesto.objects.get_or_create(
        puesto="Auxiliar Contable", posicion=16,
        estatus=True, tabulador=tab)[0]
    contador_et = Puesto.objects.get_or_create(
        puesto="Contador ET", posicion=17,
        estatus=True, tabulador=tab)[0]
    contador_comisiones = Puesto.objects.get_or_create(
        puesto="Contador Comisiones", posicion=18,
        estatus=True, tabulador=tab)[0]
    cajera = Puesto.objects.get_or_create(
        puesto="Cajera", posicion=19,
        estatus=True, tabulador=tab)[0]
    recepcionista = Puesto.objects.get_or_create(
        puesto="Recepcionista", posicion=20,
        estatus=True, tabulador=tab)[0]
    programador_crochet = Puesto.objects.get_or_create(
        puesto="Programador Crochet", posicion=21,
        estatus=True, tabulador=tab)[0]
    oficial_de_mantenimiento = Puesto.objects.get_or_create(
        puesto="Oficial de Mantenimiento", posicion=22,
        estatus=True, tabulador=tab)[0]
    jefe_de_acabado = Puesto.objects.get_or_create(
        puesto="Jefe de Acabado", posicion=23,
        estatus=True, tabulador=tab)[0]
    auxiliar_de_acabado = Puesto.objects.get_or_create(
        puesto="Auxiliar de Acabado", posicion=24,
        estatus=True, tabulador=tab)[0]
    diseñador_de_crochet = Puesto.objects.get_or_create(
        puesto="Diseñador de Crochet", posicion=25,
        estatus=True, tabulador=tab)[0]
    mecánico_de_crochet = Puesto.objects.get_or_create(
        puesto="Mecánico de Crochet", posicion=26,
        estatus=True, tabulador=tab)[0]
    diseñador_de_torcido = Puesto.objects.get_or_create(
        puesto="Diseñador de Torcido", posicion=27,
        estatus=True, tabulador=tab)[0]
    mecánico_de_trenzado_y_bolillo = Puesto.objects.get_or_create(
        puesto="Mecánico de Trenzado y Bolillo", posicion=28,
        estatus=True, tabulador=tab)[0]
    diseñador_de_trenzado = Puesto.objects.get_or_create(
        puesto="Diseñador de Trenzado", posicion=29,
        estatus=True, tabulador=tab)[0]
    jefe_de_mantenimiento = Puesto.objects.get_or_create(
        puesto="Jefe de Mantenimiento", posicion=30,
        estatus=True, tabulador=tab)[0]
    ayudante_de_mantenimiento = Puesto.objects.get_or_create(
        puesto="Ayudante de Mantenimiento", posicion=31,
        estatus=True, tabulador=tab)[0]
    encargado_de_compras = Puesto.objects.get_or_create(
        puesto="Encargado de Compras", posicion=32,
        estatus=True, tabulador=tab)[0]
    jefe_de_almacén_de_materia_p = Puesto.objects.get_or_create(
        puesto="Jefe de Almacén de Materia P.", posicion=33,
        estatus=True, tabulador=tab)[0]
    encargado_de_exportaciones = Puesto.objects.get_or_create(
        puesto="Encargado de Exportaciones", posicion=34,
        estatus=True, tabulador=tab)[0]
    auxiliar_de_sistemas = Puesto.objects.get_or_create(
        puesto="Auxiliar de Sistemas", posicion=35,
        estatus=True, tabulador=tab)[0]
    analista_programador = Puesto.objects.get_or_create(
        puesto="Analista Programador", posicion=36,
        estatus=True, tabulador=tab)[0]
    controlador_bodega_clientes = Puesto.objects.get_or_create(
        puesto="Controlador bodega clientes", posicion=37,
        estatus=True, tabulador=tab)[0]

    escolaridad = Factor.objects.get_or_create(
        factor='Escolaridad', posicion=1,
        ponderacion_nivel_1=21)[0]
    experiencia = Factor.objects.get_or_create(
        factor='Experiencia', posicion=2,
        ponderacion_nivel_1=13)[0]
    criterio = Factor.objects.get_or_create(
        factor='Criterio', posicion=3,
        ponderacion_nivel_1=13)[0]
    iniciativa = Factor.objects.get_or_create(
        factor='Iniciativa', posicion=4,
        ponderacion_nivel_1=6)[0]
    complejidad_e_importancia = Factor.objects.get_or_create(
        factor='Complejidad e Importancia', posicion=5,
        ponderacion_nivel_1=13)[0]
    resp_en_supervición = Factor.objects.get_or_create(
        factor='Resp. en Supervición', posicion=6,
        ponderacion_nivel_1=12)[0]
    resp_en_documentos = Factor.objects.get_or_create(
        factor='Resp. en Documentos', posicion=7,
        ponderacion_nivel_1=7)[0]
    resp_en_mat_mob_y_equipo = Factor.objects.get_or_create(
        factor='Resp. en Mat. Mob. y Equipo', posicion=8,
        ponderacion_nivel_1=5)[0]
    grado_de_atención = Factor.objects.get_or_create(
        factor='Grado de Atención', posicion=9,
        ponderacion_nivel_1=4)[0]
    esfuerzo_físico = Factor.objects.get_or_create(
        factor='Esfuerzo Físico', posicion=10,
        ponderacion_nivel_1=2)[0]
    condiciones_de_trbajo = Factor.objects.get_or_create(
        factor='Condiciones de Trbajo', posicion=11,
        ponderacion_nivel_1=4)[0]

    fact5niveles = [
        escolaridad,
        iniciativa,
        resp_en_supervición,
        resp_en_mat_mob_y_equipo,
        grado_de_atención,
        condiciones_de_trbajo,
    ]
    fact6niveles = [
        experiencia,
        criterio,
        complejidad_e_importancia,
        resp_en_documentos,
        esfuerzo_físico,
    ]

    for factor in fact5niveles:
        for nivel in range(1, 6):
            Nivel.objects.get_or_create(
                nivel_multiplicador=nivel,
                nivel=int2romman(nivel),
                factor=factor)
    for factor in fact6niveles:
        for nivel in range(1, 7):
            Nivel.objects.get_or_create(
                nivel_multiplicador=nivel,
                nivel=int2romman(nivel),
                factor=factor)
