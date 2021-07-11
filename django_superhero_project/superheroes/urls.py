from django.urls import path
from . import views

app_name = 'superheroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('delete/<int:id>/', views.deleteSuperHero, name='delete_superhero'),
    path('edit/<int:id>/', views.EditSuperHero, name='edit_superhero'),

 
]
