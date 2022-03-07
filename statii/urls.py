from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Harta', views.StatiiView.as_view(), name='statii')
]
