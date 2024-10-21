from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app2-home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]
