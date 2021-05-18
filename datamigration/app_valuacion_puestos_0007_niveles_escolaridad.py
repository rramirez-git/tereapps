from app_valuacion_puestos.factor_models import Factor

def migration():
    factor = Factor.objects.get(factor="Escolaridad")
    if factor.niveles.filter(nivel='I').exists():
        nivel = factor.niveles.get(nivel='I')
        nivel.nivel = "Primaria"
        nivel.save()
    if factor.niveles.filter(nivel='II').exists():
        nivel = factor.niveles.get(nivel='II')
        nivel.nivel = "Secundaria Terminada"
        nivel.save()
