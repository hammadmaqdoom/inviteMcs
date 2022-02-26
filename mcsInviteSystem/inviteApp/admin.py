from django.contrib import admin

# Register your models here.

from . import models
class userReferAdmin(admin.ModelAdmin):
    list_display = ("userID", "firstName", "lastName", "email", "phoneNumber", "userCode", "userCodeInitials", "userCodeNumber")
admin.site.register(models.userRefer, userReferAdmin)