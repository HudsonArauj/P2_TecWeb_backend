from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/marcas/<int:note_id>/', views.api_note),
    path('api/marcas', views.api_note_list),



]