from django.contrib import admin

from .models import CDI_dataset, retag,broken_api,updates_masterlist,original_masterlist, qa_updates,not_in_masterlist,cdi_metrics,warnings_summary

# Register your models here.
class RetagAdmin(admin.ModelAdmin):
    pass

#admin.site.register(CDI_dataset, RetagAdmin)
admin.site.register(retag, RetagAdmin)
admin.site.register(broken_api, RetagAdmin)
admin.site.register(updates_masterlist, RetagAdmin)
admin.site.register(original_masterlist, RetagAdmin)
admin.site.register(qa_updates, RetagAdmin)

admin.site.register(not_in_masterlist, RetagAdmin)
admin.site.register(cdi_metrics, RetagAdmin)
admin.site.register(warnings_summary, RetagAdmin)