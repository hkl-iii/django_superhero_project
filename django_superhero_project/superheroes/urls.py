from django.urls import path
from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, none='detail'),
    path('new/', views.create, name='create_new_superhero')
]
