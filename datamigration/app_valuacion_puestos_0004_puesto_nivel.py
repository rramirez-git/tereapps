from app_valuacion_puestos.models import Factor
from app_valuacion_puestos.models import Ponderacion
from app_valuacion_puestos.models import Puesto
from app_valuacion_puestos.models import Tabulador


def migration():

    afanadora = Puesto.objects.get_or_create(
        puesto="Afanadora")[0]
    facturista = Puesto.objects.get_or_create(
        puesto="Facturista")[0]
    jefe_de_personal = Puesto.objects.get_or_create(
        puesto="Jefe de Personal")[0]
    jefe_de_almacen = Puesto.objects.get_or_create(
        puesto="Jefe de Almacen")[0]
    sub_jefe_de_almacen = Puesto.objects.get_or_create(
        puesto="Sub Jefe de Almacen")[0]
    montacarguista = Puesto.objects.get_or_create(
        puesto="Montacarguista")[0]
    almacenista = Puesto.objects.get_or_create(
        puesto="Almacenista")[0]
    chofer_de_reparto = Puesto.objects.get_or_create(
        puesto="Chofer de Reparto")[0]
    auxiliar_de_aduana = Puesto.objects.get_or_create(
        puesto="Auxiliar de Aduana")[0]
    auxiliar_de_ventas = Puesto.objects.get_or_create(
        puesto="Auxiliar de Ventas")[0]
    auxiliar_atención_a_clientes = Puesto.objects.get_or_create(
        puesto="Auxiliar Atención a Clientes")[0]
    mensajero_cobrador = Puesto.objects.get_or_create(
        puesto="Mensajero-Cobrador")[0]
    cobrador = Puesto.objects.get_or_create(
        puesto="Cobrador")[0]
    auxiliar_de_cobranza = Puesto.objects.get_or_create(
        puesto="Auxiliar de Cobranza")[0]
    supervisor_de_crédito_y_cobranza = Puesto.objects.get_or_create(
        puesto="Supervisor de Crédito y Cobranza")[0]
    auxiliar_contable = Puesto.objects.get_or_create(
        puesto="Auxiliar Contable")[0]
    contador_et = Puesto.objects.get_or_create(
        puesto="Contador ET")[0]
    contador_comisiones = Puesto.objects.get_or_create(
        puesto="Contador Comisiones")[0]
    cajera = Puesto.objects.get_or_create(
        puesto="Cajera")[0]
    recepcionista = Puesto.objects.get_or_create(
        puesto="Recepcionista")[0]
    programador_crochet = Puesto.objects.get_or_create(
        puesto="Programador Crochet")[0]
    oficial_de_mantenimiento = Puesto.objects.get_or_create(
        puesto="Oficial de Mantenimiento")[0]
    jefe_de_acabado = Puesto.objects.get_or_create(
        puesto="Jefe de Acabado")[0]
    auxiliar_de_acabado = Puesto.objects.get_or_create(
        puesto="Auxiliar de Acabado")[0]
    diseñador_de_crochet = Puesto.objects.get_or_create(
        puesto="Diseñador de Crochet")[0]
    mecánico_de_crochet = Puesto.objects.get_or_create(
        puesto="Mecánico de Crochet")[0]
    diseñador_de_torcido = Puesto.objects.get_or_create(
        puesto="Diseñador de Torcido")[0]
    mecánico_de_trenzado_y_bolillo = Puesto.objects.get_or_create(
        puesto="Mecánico de Trenzado y Bolillo")[0]
    diseñador_de_trenzado = Puesto.objects.get_or_create(
        puesto="Diseñador de Trenzado")[0]
    jefe_de_mantenimiento = Puesto.objects.get_or_create(
        puesto="Jefe de Mantenimiento")[0]
    ayudante_de_mantenimiento = Puesto.objects.get_or_create(
        puesto="Ayudante de Mantenimiento")[0]
    encargado_de_compras = Puesto.objects.get_or_create(
        puesto="Encargado de Compras")[0]
    jefe_de_almacén_de_materia_p = Puesto.objects.get_or_create(
        puesto="Jefe de Almacén de Materia P.")[0]
    encargado_de_exportaciones = Puesto.objects.get_or_create(
        puesto="Encargado de Exportaciones")[0]
    auxiliar_de_sistemas = Puesto.objects.get_or_create(
        puesto="Auxiliar de Sistemas")[0]
    analista_programador = Puesto.objects.get_or_create(
        puesto="Analista Programador")[0]
    controlador_bodega_clientes = Puesto.objects.get_or_create(
        puesto="Controlador bodega clientes")[0]

    escolaridad = Factor.objects.get_or_create(
        factor='Escolaridad')[0]
    experiencia = Factor.objects.get_or_create(
        factor='Experiencia')[0]
    criterio = Factor.objects.get_or_create(
        factor='Criterio')[0]
    iniciativa = Factor.objects.get_or_create(
        factor='Iniciativa')[0]
    complejidad_e_importancia = Factor.objects.get_or_create(
        factor='Complejidad e Importancia')[0]
    resp_en_supervición = Factor.objects.get_or_create(
        factor='Resp. en Supervición')[0]
    resp_en_documentos = Factor.objects.get_or_create(
        factor='Resp. en Documentos')[0]
    resp_en_mat_mob_y_equipo = Factor.objects.get_or_create(
        factor='Resp. en Mat. Mob. y Equipo')[0]
    grado_de_atención = Factor.objects.get_or_create(
        factor='Grado de Atención')[0]
    esfuerzo_físico = Factor.objects.get_or_create(
        factor='Esfuerzo Físico')[0]
    condiciones_de_trbajo = Factor.objects.get_or_create(
        factor='Condiciones de Trbajo')[0]

    afanadora.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    facturista.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    jefe_de_personal.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    jefe_de_almacen.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    sub_jefe_de_almacen.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    montacarguista.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    almacenista.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    chofer_de_reparto.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    auxiliar_de_aduana.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    auxiliar_de_ventas.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    auxiliar_atención_a_clientes.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    mensajero_cobrador.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    cobrador.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    auxiliar_de_cobranza.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    supervisor_de_crédito_y_cobranza.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    auxiliar_contable.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    contador_et.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    contador_comisiones.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    cajera.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    recepcionista.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    programador_crochet.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    oficial_de_mantenimiento.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    jefe_de_acabado.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    auxiliar_de_acabado.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    diseñador_de_crochet.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    mecánico_de_crochet.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    diseñador_de_torcido.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    mecánico_de_trenzado_y_bolillo.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    diseñador_de_trenzado.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    jefe_de_mantenimiento.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    ayudante_de_mantenimiento.tabulador = Tabulador.objects.get(tabulador="1er Nivel")
    encargado_de_compras.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    jefe_de_almacén_de_materia_p.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    encargado_de_exportaciones.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    auxiliar_de_sistemas.tabulador = Tabulador.objects.get(tabulador="2do Nivel")
    analista_programador.tabulador = Tabulador.objects.get(tabulador="3er Nivel")
    controlador_bodega_clientes.tabulador = Tabulador.objects.get(tabulador="2do Nivel")

    afanadora.save()
    facturista.save()
    jefe_de_personal.save()
    jefe_de_almacen.save()
    sub_jefe_de_almacen.save()
    montacarguista.save()
    almacenista.save()
    chofer_de_reparto.save()
    auxiliar_de_aduana.save()
    auxiliar_de_ventas.save()
    auxiliar_atención_a_clientes.save()
    mensajero_cobrador.save()
    cobrador.save()
    auxiliar_de_cobranza.save()
    supervisor_de_crédito_y_cobranza.save()
    auxiliar_contable.save()
    contador_et.save()
    contador_comisiones.save()
    cajera.save()
    recepcionista.save()
    programador_crochet.save()
    oficial_de_mantenimiento.save()
    jefe_de_acabado.save()
    auxiliar_de_acabado.save()
    diseñador_de_crochet.save()
    mecánico_de_crochet.save()
    diseñador_de_torcido.save()
    mecánico_de_trenzado_y_bolillo.save()
    diseñador_de_trenzado.save()
    jefe_de_mantenimiento.save()
    ayudante_de_mantenimiento.save()
    encargado_de_compras.save()
    jefe_de_almacén_de_materia_p.save()
    encargado_de_exportaciones.save()
    auxiliar_de_sistemas.save()
    analista_programador.save()
    controlador_bodega_clientes.save()

    afanadora.niveles_ponderacion.all().delete()
    facturista.niveles_ponderacion.all().delete()
    jefe_de_personal.niveles_ponderacion.all().delete()
    jefe_de_almacen.niveles_ponderacion.all().delete()
    sub_jefe_de_almacen.niveles_ponderacion.all().delete()
    montacarguista.niveles_ponderacion.all().delete()
    almacenista.niveles_ponderacion.all().delete()
    chofer_de_reparto.niveles_ponderacion.all().delete()
    auxiliar_de_aduana.niveles_ponderacion.all().delete()
    auxiliar_de_ventas.niveles_ponderacion.all().delete()
    auxiliar_atención_a_clientes.niveles_ponderacion.all().delete()
    mensajero_cobrador.niveles_ponderacion.all().delete()
    cobrador.niveles_ponderacion.all().delete()
    auxiliar_de_cobranza.niveles_ponderacion.all().delete()
    supervisor_de_crédito_y_cobranza.niveles_ponderacion.all().delete()
    auxiliar_contable.niveles_ponderacion.all().delete()
    contador_et.niveles_ponderacion.all().delete()
    contador_comisiones.niveles_ponderacion.all().delete()
    cajera.niveles_ponderacion.all().delete()
    recepcionista.niveles_ponderacion.all().delete()
    programador_crochet.niveles_ponderacion.all().delete()
    oficial_de_mantenimiento.niveles_ponderacion.all().delete()
    jefe_de_acabado.niveles_ponderacion.all().delete()
    auxiliar_de_acabado.niveles_ponderacion.all().delete()
    diseñador_de_crochet.niveles_ponderacion.all().delete()
    mecánico_de_crochet.niveles_ponderacion.all().delete()
    diseñador_de_torcido.niveles_ponderacion.all().delete()
    mecánico_de_trenzado_y_bolillo.niveles_ponderacion.all().delete()
    diseñador_de_trenzado.niveles_ponderacion.all().delete()
    jefe_de_mantenimiento.niveles_ponderacion.all().delete()
    ayudante_de_mantenimiento.niveles_ponderacion.all().delete()
    encargado_de_compras.niveles_ponderacion.all().delete()
    jefe_de_almacén_de_materia_p.niveles_ponderacion.all().delete()
    encargado_de_exportaciones.niveles_ponderacion.all().delete()
    auxiliar_de_sistemas.niveles_ponderacion.all().delete()
    analista_programador.niveles_ponderacion.all().delete()
    controlador_bodega_clientes.niveles_ponderacion.all().delete()

    Ponderacion.objects.create(puesto=afanadora,
        nivel=escolaridad.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=experiencia.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=criterio.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=afanadora,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=facturista,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=facturista,
        nivel=experiencia.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=facturista,
        nivel=criterio.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=facturista,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=facturista,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=facturista,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=facturista,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=facturista,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=facturista,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=facturista,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=facturista,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=escolaridad.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_personal,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacen,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=sub_jefe_de_almacen,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=experiencia.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=criterio.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=montacarguista,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=experiencia.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=almacenista,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=criterio.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=chofer_de_reparto,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=experiencia.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_aduana,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=iniciativa.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_ventas,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_atención_a_clientes,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=experiencia.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=criterio.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=mensajero_cobrador,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=experiencia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=criterio.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cobrador,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=experiencia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_cobranza,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=escolaridad.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=supervisor_de_crédito_y_cobranza,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_contable,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=escolaridad.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=experiencia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=contador_et,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=escolaridad.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=contador_comisiones,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=cajera,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=cajera,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=cajera,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=cajera,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cajera,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=cajera,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=cajera,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=cajera,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=cajera,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=cajera,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=cajera,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=programador_crochet,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=oficial_de_mantenimiento,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_acabado,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_acabado,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=experiencia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_crochet,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_crochet,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_torcido,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=criterio.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=mecánico_de_trenzado_y_bolillo,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=experiencia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=diseñador_de_trenzado,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=experiencia.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=criterio.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=ayudante_de_mantenimiento,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=escolaridad.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=criterio.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=encargado_de_compras,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=criterio.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_almacén_de_materia_p,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=escolaridad.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=experiencia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=criterio.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=iniciativa.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=encargado_de_exportaciones,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=escolaridad.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=experiencia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=iniciativa.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=auxiliar_de_sistemas,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=escolaridad.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=experiencia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=iniciativa.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=analista_programador,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=escolaridad.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=experiencia.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=criterio.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=iniciativa.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=controlador_bodega_clientes,
        nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=escolaridad.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=experiencia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=criterio.niveles.get(nivel_multiplicador=5))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=iniciativa.niveles.get(nivel_multiplicador=1))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
       nivel=complejidad_e_importancia.niveles.get(nivel_multiplicador=6))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=resp_en_supervición.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=resp_en_documentos.niveles.get(nivel_multiplicador=3))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=resp_en_mat_mob_y_equipo.niveles.get(nivel_multiplicador=4))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=grado_de_atención.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
        nivel=esfuerzo_físico.niveles.get(nivel_multiplicador=2))
    Ponderacion.objects.create(puesto=jefe_de_mantenimiento,
       nivel=condiciones_de_trbajo.niveles.get(nivel_multiplicador=5))




