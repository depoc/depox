from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('erp/', include('erp.urls')),
    path('caixa/', include('finance.urls')),
    path('contatos/', include('contacts.urls')),

    # temporary: while the index page is not built
    path(
        '',
        TemplateView.as_view(template_name='users/login.html'),
        name='login'
    ),

    path(
        'recuperar-senha/', 
        auth_views.PasswordResetView.as_view(),
        name='reset_password'
    ),
    path(
        'recuperar-senha/enviado/', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'recuperar-senha/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'recuperar-senha/fim/', 
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
