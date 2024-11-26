from django import template

register = template.Library()

@register.filter
def first_name(name) -> str:
    first_name = name.split()[0].upper() if name else ''
    return first_name

@register.filter
def bank_account(name) -> str:
    if name:
        name = str(name).lower()
        bank_name = name.split()
        bank_last_name = bank_name[len(bank_name)-1]

        if len(name) <= 10:
            return name

    return bank_last_name
    
@register.filter
def company(fantasia) -> str:
    if fantasia:
        fantasia = fantasia.split()[0].lower() if fantasia else ''
        if len(fantasia) <= 9:
            return fantasia
        else:
            return 'cnpj'
    return 'cnpj'

@register.filter
def format_cnpj(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'

@register.filter
def format_money(number):
    money = f"{number:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    return money

@register.filter
def absolute_value(value):
    result = abs(value)

    return result