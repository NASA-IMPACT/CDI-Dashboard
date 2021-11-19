from django.contrib import admin

from .models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist

# Register your models here.
class CAPAdmin(admin.ModelAdmin):
    pass

class MasterlistAdmin(admin.ModelAdmin):
    list_display = ('cdi_id', 'title', 'organization', 'catalog_url', 'api_url', 'status', 'datagov_ID')

class CAPInstanceAdmin(admin.ModelAdmin):
    list_display = ('cap_id', 'date', 'masterlist_count', 'climate_collection_count',
                    'broken_urls', 'lost_climate_tag', 'not_in_masterlist', 'total_warnings'
                    )

class BrokenAPIAdmin(admin.ModelAdmin):
    list_display = ('broken_id', 'cap_id', 'datagov_ID')

class RetagAdmin(admin.ModelAdmin):
    list_display = ('retag_id', 'cap_id', 'datagov_ID')

class QAUpdatesAdmin(admin.ModelAdmin):
    list_display = ('qa_id', 'cap_id', 'datagov_ID')

class NotInMasterlistAdmin(admin.ModelAdmin):
    list_display = ('nml_id', 'cap_id', 'title', 'catalog_url', 'api_url')

#admin.site.register(Model, Admin)
admin.site.register(Masterlist, MasterlistAdmin)
admin.site.register(CAPInstance, CAPInstanceAdmin)
admin.site.register(BrokenAPI, BrokenAPIAdmin)
admin.site.register(Retag, RetagAdmin)
admin.site.register(QAUpdates, QAUpdatesAdmin)
admin.site.register(NotInMasterlist, NotInMasterlistAdmin)
