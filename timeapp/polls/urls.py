from django.urls import path, include
from . import views

urlpatterns = [
    path('chack-day/', views.check_last_day_for_month, name='check_day'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()), 
    path('time/', views.TimeList.as_view()),
    path('time/<int:pk>/', views.TimeDetail.as_view()),
    path('totale/', views.TotaleList.as_view()),
    path('totale/<int:pk>/', views.TotaleDetail.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('sum-time/', views.SunTimeList.as_view()),  
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

