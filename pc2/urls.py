from django.urls import path
from . import views  

urlpatterns = [
    path('', views.login_mostrar, name='login'),  
    path('save_user/', views.login, name='login_submit'),  
    path('registro/', views.registro, name='registro'),
]
