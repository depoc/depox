from django import template

register = template.Library()

@register.filter
def format_money(number):
    money = f"{number:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")
    
    return money

@register.filter
def format_cep(cep: str) -> str:
    if cep:
        cep_formatted = f'{cep[0:5]}-{cep[5:8]}'
        return cep_formatted
    return cep