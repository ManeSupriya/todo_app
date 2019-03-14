from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.schedule_list, name="schedule_list"),
    path('newtask/',views.new_task_view, name="new_task"),
    path('delete/',views.delete_view, name="delete"),
    path('detail/',views.detail_view,name="detail"),


]
