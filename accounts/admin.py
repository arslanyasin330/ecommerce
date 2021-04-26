from django.contrib import admin

# Register your models here.
from accounts import models

admin.site.register(models.UserProfile)
