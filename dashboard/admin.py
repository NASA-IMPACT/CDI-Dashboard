from django.contrib import admin

from .models import CDI_dataset

# Register your models here.
class RetagAdmin(admin.ModelAdmin):
    pass

admin.site.register(CDI_dataset, RetagAdmin)
