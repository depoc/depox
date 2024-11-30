from django import template

register = template.Library()

@register.filter
def format_money(number):
    money = f"{number:,.2f}" \
        .replace(",", "X") \
        .replace(".", ",") \
        .replace("X", ".")
    
    return money
