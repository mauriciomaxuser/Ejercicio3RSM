#configuracion de rutas espesificas de la aplicacion empresas 
from django.urls import path
from .import views
urlpatterns=[
    path('',views.home),

    path('inicio',views.inicio),
    path('desarrolladores', views.desarrolladores),
    path('nuevoDesarrollador', views.nuevoDesarrollador),
    path('nuevoProyecto', views.nuevoProyecto),

    path('guardarDesarrollador', views.guardarDesarrollador),
    path('guardarProyecto', views.guardarProyecto),
    path('editarDesarrollador/<id>', views.editarDesarrollador),
    path('actualizandoDesarrollador/', views.actualizandoDesarrollador),
    path('editarProyecto/<id>', views.editarProyecto),
    path('actualizandoProyecto/', views.actualizandoProyecto),
    path('eliminarDesarrollador/<id>', views.eliminarDesarrollador),
    path('eliminarProyecto/<id>', views.eliminarProyecto),










    

]