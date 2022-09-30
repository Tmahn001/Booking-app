from django.urls import path
from . import views
urlpatterns = [

    path('', views.get_data, name='api_app'),
    path('test/', views.getRoutes, name='api'),
    ]