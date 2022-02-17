from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Statii', views.StatiiView.as_view(), name='statii')
]
