from django.urls import path

#cosas para el login
from django.contrib.auth.views import LogoutView


from AppCoder import views




urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('gerencias', views.gerencias, name="Gerencias"),
    path('gerentes', views.gerentes, name="Gerentes"),
    path('colaboradores', views.colaboradores, name="Colaboradores"),
    #path('gerenciaFormulario', views.gerenciaFormulario, name="GerenciaFormulario"),
    #path('gerenteFormulario', views.gerenteFormulario, name="GerenteFormulario"),
    #path('colaboradorFormulario', views.colaboradorFormulario, name="ColaboradorFormulario"),
    path('buscar/', views.buscar),
 

]


