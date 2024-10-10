from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('erp/', include('erp.urls')),

    # temporary: while the index page is not built
    path(
        '',
        TemplateView.as_view(template_name='users/login.html'),
        name='login'
    ),
]
