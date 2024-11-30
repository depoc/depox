from django import template

register = template.Library()

@register.filter
def first_name(name) -> str:
    first_name = name.split()[0].upper() if name else ''
    return first_name
    
@register.filter
def format_fantasia(fantasia) -> str:
    if fantasia:
        fantasia = fantasia.split()[0].lower() if fantasia else ''
        if len(fantasia) <= 9:
            return fantasia
        else:
            return 'cnpj'
    return 'cnpj'
