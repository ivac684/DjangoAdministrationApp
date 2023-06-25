from django.contrib import admin
from .models import Korisnici, Predmeti, Upisi
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Korisnici)
class KorisnikAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('None', {'fields':('role', 'status')}),
    )
    
admin.site.register(Predmeti)
admin.site.register(Upisi)