from django.contrib import admin

# Register your models here.
from .models import User, Entry

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class Entry(admin.ModelAdmin):
    pass
