from app_valuacion_puestos.models import Tabulador

def migration():
    for (tab_desc, new_desc) in [
            ('1er Nivel', '1 Nivel'),
            ('2do Nivel', '3 Niveles'),
            ('3er Nivel', '5 Niveles')]:
        tab = Tabulador.objects.get(tabulador=tab_desc)
        tab.tabulador = new_desc
        tab.save()

