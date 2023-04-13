from django.contrib import admin

# Register your models here.
from .models import Dog, Feeding, Toy
# Add our Dog model to the admin site, so we can perform
# CRUD operations on it!
admin.site.register(Dog)
# register the new Feeding Model 
admin.site.register(Feeding)
# register the new Toy Model 
admin.site.register(Toy)