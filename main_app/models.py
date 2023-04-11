from django.db import models
from django.urls import reverse # kind of like redirect
# Create your models here.
class Dog(models.Model):
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()
 
	def get_absolute_url(self):
    	# path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
		return reverse('detail', kwargs={'dog_id': self.id})