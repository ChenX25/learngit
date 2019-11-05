from django.urls import path

from . import views

app_name = 'learning_logs'         # is not a registered namespace
urlpatterns = [
    path('', views.index, name='index'),       # name of re pattern

    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
]