from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register

app_name = 'profile' 

urlpatterns = [ 
    # Logar / Registrar / Sair
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


 
]

"""
ROTAS AUTOMÁTICAS QUE O DJANGO CRIA:

accounts/login/
→ login do usuário

accounts/logout/
→ logout do usuário

accounts/password_change/
→ trocar senha estando logado

accounts/password_change/done/
→ página de confirmação da troca de senha

accounts/password_reset/
→ pedir redefinição de senha por email

accounts/password_reset/done/
→ aviso de email enviado

accounts/reset/<uidb64>/<token>/
→ link único recebido no email

accounts/reset/done/
→ senha redefinida com sucesso
"""