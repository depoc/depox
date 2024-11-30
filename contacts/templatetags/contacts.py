from django import template

register = template.Library()

@register.filter
def format_phone_number(phone: str) -> str:
    if phone:
        return f'{phone[:2]} {phone[2:7]}-{phone[7:11]}'
    return 'adicionar celular'