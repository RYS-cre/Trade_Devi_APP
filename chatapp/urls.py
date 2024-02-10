from django.urls import path
from . import views

urlpatterns = [
  path('agent1/', views.handleMessageDM, name='handleMessageDM'),
  path('agent2/', views.handleMessageAL, name='handleMessageAL'),
  path('agent3/', views.handleMessageW, name='handleMessageW'),
]