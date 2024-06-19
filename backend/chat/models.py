from django.db import models
from accounts.models import User
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    name = models.CharField(blank=True, null=True, max_length=100)
    online_status= models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.user.email




class Chat(models.Model):
    sender = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True , max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)     


    def __str__(self) -> str:
        return self.message