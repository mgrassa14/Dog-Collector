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
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    # route to show a form and create a dog
    path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
    # route to show a form and edit the dog
    path('dogs/<int:pk>/update', views.DogUpdate.as_view(), name='dogs_update'),
    # route to delete dog
    path('dogs/<int:pk>/delete', views.DogDelete.as_view(), name='dogs_delete'),
    path('cats/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # associate a toy with a cat (M:M)
    path('cats/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
