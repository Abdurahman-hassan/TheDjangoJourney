from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('months/<int:month>', views.months_by_number),
    path('months/<str:month>', views.months, name='month_str'),

]