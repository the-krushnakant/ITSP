#from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.details, name='details' ),
    path('team/', views.details_page, name='team'),
    path('<str:team_id>/', views.team_view, name='team_view'),
    path('team/<str:team__id>/', views.team_detail, name='team_detail')
    
]
