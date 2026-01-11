from users.forms import CustomUserChangeForm
from .forms import CompanyForm, MemberCreationForm
from decimal import Decimal


class Settings:
    @staticmethod
    def context(request) -> dict:
        context = {}
        context.update(Settings.get_user_context(request))
        context.update(Settings.get_company_context(request))
        context.update(Settings.get_team_context(request))
        context.update(Settings.calculate_total_balance(request))

        return context
    

    @staticmethod
    def get_user_context(request) -> dict:
        user = request.user
        form = CustomUserChangeForm(instance=user)

        if request.method == 'POST' and 'user-form' in request.POST:
            form = CustomUserChangeForm(request.POST, instance=user)
            if form.is_valid():
                form.save()

        return {'form': form}


    @staticmethod
    def get_company_context(request) -> dict:
        user = request.user
        company = user.company
        form = CompanyForm(instance=company)

        if request.method == 'POST'and 'company-form' in request.POST:
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                company = form.save()
                user.company = company
                user.save()

        return {'company_form': form}
    

    @staticmethod
    def get_team_context(request) -> dict:
        company = request.user.company
        form = MemberCreationForm()

        if request.method == 'POST' and 'member-form' in request.POST:
            form = MemberCreationForm(request.POST)
            if form.is_valid():
                member = form.save(commit=False)
                member.company = company
                member.save()

        context = {'member_form': form}

        if company:
            team = company.user_set.all()
            if team:
                context['team'] = team
                return context
            
        return context
    
    @staticmethod
    def calculate_total_balance(request) -> dict:
        company = request.user.company
        total_balance = Decimal(0)
        
        if company:
            banks = company.banks.all()

            for bank in banks:
                total_balance += bank.saldo

        return {"total_balance": total_balance}
