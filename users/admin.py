from django.contrib import admin

# Register your models here.

from .models import Profile

#register profile to admin page
admin.site.register(Profile)