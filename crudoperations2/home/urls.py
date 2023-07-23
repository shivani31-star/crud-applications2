from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('registration/',views.registration),
    path('login/',views.login),
    path('table/',views.table),
    path('update/<int:uid>/',views.update_view),
    path('update/',views.update_form),
    path('delete/<int:pk>/',views.delete,name="delete"),
]
