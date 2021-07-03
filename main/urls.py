from django.contrib import admin
from django.urls import path
from .views import MainView,TrolleibusesView,Trolleibus1View,Trolleibus2View,Trolleibus3View,Trolleibus4View,TaxiesView,Taxi1View,Taxi2View,Taxi3View,Taxi4View,SprinteresView,Sprinter1View,Sprinter2View,Sprinter3View,Sprinter4View

urlpatterns = [
    path("", MainView.as_view(), name="main_wrap"),

    path("trolleibuses/", TrolleibusesView.as_view(), name="trolleibuses"),
    path("trolleibus1/", Trolleibus1View.as_view(), name="trolleibus1"),
    path("trolleibus2/", Trolleibus2View.as_view(), name="trolleibus2"),
    path("trolleibus3/", Trolleibus3View.as_view(), name="trolleibus3"),
    path("trolleibus4/", Trolleibus4View.as_view(), name="trolleibus4"),

    path("taxies/", TaxiesView.as_view(), name="taxies"),
    path("taxi1/", Taxi1View.as_view(), name="taxi1"),
    path("taxi2/", Taxi2View.as_view(), name="taxi2"),
    path("taxi3/", Taxi3View.as_view(), name="taxi3"),
    path("taxi4/", Taxi4View.as_view(), name="taxi4"),

    path("sprinteres/", SprinteresView.as_view(), name="sprinteres"),
    path("sprinter1/", Sprinter1View.as_view(), name="sprinter1"),
    path("sprinter2/", Sprinter2View.as_view(), name="sprinter2"),
    path("sprinter3/", Sprinter3View.as_view(), name="sprinter3"),
    path("sprinter4/", Sprinter4View.as_view(), name="sprinter4"),
]
