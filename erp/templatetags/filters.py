from django import template

register = template.Library()

@register.filter
def first_name(value):
    return value.split()[0].lower() if value else ''

@register.filter
def format_cnpj(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'