from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('add_todo', views.add_todo , name = 'add_todo'),
    path('complete/<todo_id>/',views.complete_todo , name = 'complete'),
    path('delete_complete/',views.delete_completed, name='delete_completed'),
    path('delete-all/',views.delete_all , name = 'delete_all')
]