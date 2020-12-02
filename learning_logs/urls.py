from django.urls import path
from . import views



app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name= 'index'), 
    path('topics', views.topics, name='topics'),
    path('topics/<int:t_id>/', views.topics, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
]