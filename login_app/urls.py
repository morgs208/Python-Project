from django.urls import path     
from . import views
urlpatterns = [
    path('', views.login),
    path("process_registration", views.process_registration),
    path("success", views.success),
    path("process_login", views.process_login),
    path("logout", views.logout),
]