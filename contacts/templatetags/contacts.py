from django import template

register = template.Library()

@register.filter
def format_phone_number(phone: str) -> str:
    return f'{phone[:2]} {phone[2:7]}-{phone[7:11]}' if phone else ''

@register.filter
def format_cpf_cnpj(cpf_cnpj: str) -> str:
    if cpf_cnpj and len(cpf_cnpj) == 11:
        cpf = f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:11]}'
        return cpf
    
    cnpj = (
        f'{cpf_cnpj[0:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}'
        f'/{cpf_cnpj[8:12]}-{cpf_cnpj[12:14]}'
    )
    return cnpj