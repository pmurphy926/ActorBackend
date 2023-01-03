from django.urls import path
from . import views

urlpatterns = [
    path('api/actors', views.ActorList.as_view(), name='actor_list'),
    path('api/actors/<int:pk>', views.ActorDetail.as_view(), name='actor_detail'),
]
