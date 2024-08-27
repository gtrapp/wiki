from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path('random_page/', views.random_page, name="random_page"),
    path('search/', views.search, name="search"),
    path('<str:entry>/', views.entry, name="page"),
    path('<str:entry>/edit/', views.edit, name="edit")
]
