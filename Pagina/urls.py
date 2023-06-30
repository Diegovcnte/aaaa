from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("boat", views.boat, name="boat"),
    path("bob", views.bob, name="bob"),
    path("flappydino", views.flappydino, name="flappydino"),
    path("foro", views.foro, name="foro"),
    path("IniciarSesion", views.IniciarSesion, name="IniciarSesion"),
    path("miner", views.miner, name="miner"),
    path("mydreamy", views.mydreamy, name="mydreamy"),
    path("pacman", views.pacman, name="pacman"),
    path("pinpong", views.pinpong, name="pinpong"),
    path("pokedex", views.pokedex, name="pokedex"),
    path("registrar", views.registrar, name="registrar"),
    path("tazita", views.tazita, name="tazita"),
    path("tetris", views.tetris, name="tetris"),
    path("tipo_add", views.tipo_add, name="tipo_add"),
    path("tipo_edit", views.tipo_edit, name="tipo_edit"),
    path("tipo_list", views.tipo_list, name="tipo_list"),
    path("user_add", views.tipo_add, name="user_add"),
    path("user_edit", views.tipo_edit, name="tipo_edit"),
    path("user_list",views.user_list, name="user_list"),
    path("tipo_add", views.tipo_add, name="tipo_add"),
    path("tipo_edit", views.tipo_edit, name="tipo_edit"),
    path("tipo_list", views.tipo_list, name="tipo_list"),
]