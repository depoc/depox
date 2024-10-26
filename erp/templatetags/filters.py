from django import template

register = template.Library()

@register.filter
def first_name(name) -> str:
    first_name = name.split()[0].lower() if name else ''
    return first_name

@register.filter
def user(name) -> str:
    first_name = name.split()[0].lower() if name else ''
    if len(first_name) <= 9:
        return first_name
    else:
        return 'eu'

@register.filter
def format_cnpj(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'