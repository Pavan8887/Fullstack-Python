from django.urls import path
from . import views

urlpatterns = [
    path('function/', views.hello_world, name='function'),
    path('class/', views.helloindia.as_view(), name='class'),
    path('reservation/', views.reservation, name='reservation'),
]
