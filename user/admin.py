from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'birthdate', 'profile_picture_preview')  # Email hinzugefügt

    def email(self, obj):
        return obj.user.email
    email.short_description = "E-Mail"

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" style="width: 50px; height: 50px;" />'
        return "Kein Bild"
    profile_picture_preview.allow_tags = True
    profile_picture_preview.short_description = "Profilbild"

admin.site.register(Profile, ProfileAdmin)


