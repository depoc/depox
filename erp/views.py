from django.shortcuts import render
from django.views.generic import TemplateView


class ErpView(TemplateView):
    template_name = 'erp/index.html'