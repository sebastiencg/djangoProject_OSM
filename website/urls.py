from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_route/', views.save_route, name='save_route'),

    path('routes/', views.list_routes, name='list_routes'),
    path('routes/<int:route_id>/', views.get_route, name='get_route'),
]