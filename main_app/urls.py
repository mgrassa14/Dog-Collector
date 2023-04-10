from django.urls import path
from . import views
# these include the paths that will define each route  below
urlpatterns = [
    # localhost:8000
    path('', views.home, name='home'),
    # localhost:8000/about
    path('about/', views.about, name='about'),
    # route for dogs index
    # localhost:8000/ddogs
    path('dogs/', views.dogs_index, name='index'),
    # dogs detail (show page)
    # localhost:8000/dogs/dog_id
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail')
]
