# addition

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('wizard/', views.show, name='api-index'),
    path('wizard/new', views.create, name='api-index'),
]