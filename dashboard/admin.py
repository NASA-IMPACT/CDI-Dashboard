from django.contrib import admin

from .models import Masterlist, CAPInstance, BrokenAPI, Retag, QAUpdates, NotInMasterlist

# Register your models here.
class CAPAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Model, CAPAdmin)
admin.site.register(Masterlist, CAPAdmin)
admin.site.register(CAPInstance, CAPAdmin)
admin.site.register(BrokenAPI, CAPAdmin)
admin.site.register(Retag, CAPAdmin)
admin.site.register(QAUpdates, CAPAdmin)
admin.site.register(NotInMasterlist, CAPAdmin)
