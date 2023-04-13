from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse

from .models import Dog, Toy
# Import the FeedingForm
from .forms import FeedingForm

class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

# Add dogs view
def dogs_index(request):
    # key 'dogs' will be the variable name in the dogs/index.html
    # dogs will be the array that we are storing in the 'dogs'
  dogs = Dog.objects.all() # finding all of the dogs from the database!
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id) # find the dog with the id that was in the params in the db
  # Get the toys the dog doesn't have
  toys_dog_doesnt_have = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {'dog': dog, 'feeding_form': feeding_form, 'toys': toys_dog_doesnt_have})

def add_feeding(request, dog_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the dog_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    # django automatically looks in templates folder for html
    return render(request, 'about.html')

class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, dog_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('detail', dog_id=dog_id)