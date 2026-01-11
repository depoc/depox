from django import template

register = template.Library()

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
def absolute_value(value):
    result = abs(value)

    return result