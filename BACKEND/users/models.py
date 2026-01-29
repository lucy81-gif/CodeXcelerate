from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    badges = models.JSONField(default=list,blank=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class XPTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='xp_transactions')
    amount= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} + {self.amount} XP"

#Platform Model
class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to="platforms/", blank=True, null=True)

    def __str__(self):
        return self.name
