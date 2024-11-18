from .models import BankAccount
from .forms import TransactionsForm


class Finance:
    @staticmethod
    def context(request) -> dict:
        context = {}
        context.update(Finance.get_balance_context(request))
        context.update(Finance.add_transactions(request))

        return context


    @staticmethod
    def get_balance_context(request) -> dict:
        company = request.user.company
        banks = BankAccount.objects.filter(company=company)

        saldos = [bank.saldo for bank in banks]
        saldo_total = sum(saldos)
        
        return {'saldo_total': saldo_total, 'banks': banks}
    

    @staticmethod
    def add_transactions(request) -> dict:
        form = TransactionsForm()     
        conta = request.POST.get('conta')
        if conta:
            bank = BankAccount.objects.get(id=conta)
        tipo = request.POST.get('tipo')         

        if request.method == 'POST' and 'add-transaction' in request.POST:
            post_data = request.POST.copy()
            valor = post_data.get('valor', '')
            valor_cleaned = valor.replace('.', '').replace(',', '.')
            post_data['valor'] = valor_cleaned

            if tipo == 'entrada': 
                saldo = float(bank.saldo) + float(valor_cleaned)
                bank.saldo = saldo
                bank.save()
            
            form = TransactionsForm(post_data)
            
            if form.is_valid():
                form.save()
            else:
                print(form.errors)

        return {'transaction': form}
