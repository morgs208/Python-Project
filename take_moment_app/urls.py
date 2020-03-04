from django.urls import path     
from . import views
urlpatterns = [
    path('home', views.home),
    path('moment', views.moment),
    path('proc_moment', views.proc_moment),
    path('add_comment', views.add_comment),
    path('delete_comment/<int:id>', views.delete_comment),
    path('delete_moment/<int:id>', views.delete_moment),
]