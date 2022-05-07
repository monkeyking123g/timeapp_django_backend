from django.urls import path
from . import views

urlpatterns = [
    path('time', views.time_list, name='list_time'),
    path('time-detail/<int:pk>', views.time_detail, name='detail_time'),
    path('totale', views.total_list, name='list_total'),
    path('totale-detail/<int:pk>', views.totale_detail, name='detail_totale'),
    path('sum-time', views.sum_time, name='sum_time'),
    path('time-add/', views.TimeListView.as_view(), name='time_add'),
    path('chack-day/', views.check_last_day_for_month, name='check_day'),   
   
]

