from users.forms import CustomUserChangeForm
from .forms import CompanyForm, MemberCreationForm


class Settings:
    @staticmethod
    def context(request) -> dict:
        context = {}
        context.update(Settings.get_user_context(request))
        context.update(Settings.get_company_context(request))
        context.update(Settings.get_team_context(request))

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

        if company:
            team = company.user_set.all()                        

        return {'member_form': form, 'team': team}
    
