from django.contrib import admin

from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User

# Register your models here.





@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'phone', 'picture')
    list_filter = ('created', 'modified', 'id')
    search_fields = ('user__username', 'bio', 'phone', 'picture')
    ordering = ('-created',)

    fieldsets = (
        ("Profile Info", {
            "fields": (('user', 'picture'),),
        }),
        ("Extra Info", {
            "fields": (('bio', 'phone'),),
        }),
        ("Metadata", {
            "fields": (('created', 'modified'),),
        })
    )
    
    readonly_fields = ('created', 'modified')
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
