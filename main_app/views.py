from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Stella', 'Golden Retriever', 'affectionate', 10),
  Dog('Luna', 'Chihuahua', 'snappy', 10),
  Dog('Pongo', 'Dalmatian', 'playful', 1)
]


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    # django automatically looks in templates folder for html
    return render(request, 'about.html')

# Add dogs view
def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })
