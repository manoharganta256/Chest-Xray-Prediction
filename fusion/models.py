from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True,on_delete=models.NOT_PROVIDED)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    chest_xray = models.ImageField(upload_to='xray_images',blank=True)
    prediction = models.CharField(max_length = 100,blank=True)
    probability = models.CharField(max_length = 10, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures',blank=True)
    limit = models.IntegerField(default=0,blank=True)
    def __str__(self):
        return self.user.username

import os
@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.chest_xray:
        if os.path.isfile(instance.chest_xray.path):
            os.remove(instance.chest_xray.path)