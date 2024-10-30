from django import template

register = template.Library()

@register.filter
def first_name(name) -> str:
    first_name = name.split()[0].lower() if name else ''
    if first_name == 'depoc':
        return 'DEPOC'
    return first_name.capitalize()

@register.filter
def user(name) -> str:
    first_name = name.split()[0].lower() if name else ''
    if len(first_name) <= 9:
        return first_name
    else:
        return 'eu'
    
@register.filter
def company(fantasia) -> str:
    fantasia = fantasia.split()[0].lower() if fantasia else ''
    if len(fantasia) <= 9:
        return fantasia
    else:
        return 'cnpj'    

@register.filter
def format_cnpj(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'