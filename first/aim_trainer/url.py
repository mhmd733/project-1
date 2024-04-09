
from django.urls import path
from . import views

urlpatterns = [
    path("",views.trainer(),name = "aim_trainer")
]