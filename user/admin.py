from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Inline für das Profil erstellen
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Benutzeradmin erweitern
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Registriere den erweiterten Benutzeradmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


