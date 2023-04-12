from django.db import models
from django.urls import reverse # kind of like redirect
from datetime import date

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
 
    def get_absolute_url(self):
    	# path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
        return reverse('detail', kwargs={'dog_id': self.id})

    # add this new method
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)




MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
    
class Feeding(models.Model):
    date = models.DateField('feeding Date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
  
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']