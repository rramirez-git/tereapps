from django import template

register = template.Library()

@register.inclusion_tag('app_tablero/tablero/view_cta.html', takes_context=True)
def tablero_tr_cta(context, cta, cta_padre=0, nivel=0):
    new_cta_padre = str(cta_padre) + '-' + str(cta.pk)
    show_cta = cta_padre == 0
    return {
        'cta': cta,
        'cta_padre': cta_padre,
        'new_cta_padre': new_cta_padre,
        'object': context.get('object'),
        'nivel': nivel+1,
        'ancho': nivel*10,
        'show_cta': show_cta,
    }
