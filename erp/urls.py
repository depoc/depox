from django.urls import path

from . import views

app_name = 'erp'
urlpatterns = [
    path('', views.ErpView.as_view(), name='index')
]
