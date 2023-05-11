from django.urls import path
from . import views

urlpatterns = [
    path("", views.Starting_Page.as_view(), name="starting-page")
]
