from django.contrib import admin
from fusion.models import Image,UserProfile
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user','chest_xray','prediction','upload_time','probability']
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','profile_picture','limit']
admin.site.register(Image,ImageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)