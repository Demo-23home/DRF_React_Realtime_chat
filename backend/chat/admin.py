from django.contrib import admin
from .models import UserProfile, Chat
# Register your models here.


admin.site.register(Chat)
admin.site.register(UserProfile)
