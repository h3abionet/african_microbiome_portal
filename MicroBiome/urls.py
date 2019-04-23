from django.urls import path

from . import views

urlpatterns = [
    path('', views.front_main, name="index"),
    path('search/', views.search_form, name="search"),
    path('results/', views.results, name="results"),
]
