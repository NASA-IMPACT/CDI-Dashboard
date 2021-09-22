from django.contrib import admin

from .models import Retag

# Register your models here.
class RetagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Retag, RetagAdmin)
