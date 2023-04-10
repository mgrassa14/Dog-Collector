from django.contrib import admin

# Register your models here.
from .models import Dog
# Add our Dog model to the admin site, so we can perform
# CRUD operations on it!
admin.site.register(Dog)