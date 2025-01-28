from django.contrib import admin
from .models import Plant, Owner
# Register your models here.

admin.site.register([Plant, Owner])
