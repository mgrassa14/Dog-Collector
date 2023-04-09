from django.urls import path
from . import views
# these include the paths that will define each route  below
urlpatterns = [
    # localhost:8000
    path('', views.home, name='home'),
]
