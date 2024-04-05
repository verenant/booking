from . import views
from django.urls import path

urlpatterns = [
    path('', views.vehicle_view,name = 'vehicle'),
    #path('create', views.create,name = 'create'),
    path('<int:id>',views.detail_view, name='detail'),

]