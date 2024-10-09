from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ErpView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'erp/index.html'