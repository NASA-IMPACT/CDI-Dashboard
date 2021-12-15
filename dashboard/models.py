from django.db import models

status_choices = (
    ('Active', 'Active'), 
    ('Not Active','Not Active'), 
    ('Retired','Retired')
)

metadata_type_choices = (
    ('No metadata type', 'No Metadata Type'), 
    ('geospatial','Geospatial')
)

class Masterlist(models.Model):
    cdi_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    organization = models.CharField(max_length=50)
    catalog_url = models.URLField(max_length=500)
    api_url = models.URLField(max_length=500)
    cdi_themes = models.CharField(max_length=500, null=True)
    metadata_type = models.CharField(max_length=50, null=True, blank=True, choices=metadata_type_choices, default='No metadata type')
    geoplatform_id = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Active')
    datagov_ID = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.datagov_ID)

class CAPInstance(models.Model):
    cap_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    masterlist_count = models.IntegerField()
    climate_collection_count = models.IntegerField()
    broken_urls = models.IntegerField()
    lost_climate_tag = models.IntegerField()
    not_in_masterlist = models.IntegerField()
    total_warnings = models.IntegerField()

    def __str__(self):
        return str(self.cap_id)

class BrokenAPI(models.Model):
    broken_id = models.AutoField(primary_key=True)
    cap_id = models.ForeignKey('CAPInstance', db_column='cap_id', on_delete=models.CASCADE)
    datagov_ID = models.ForeignKey('Masterlist', to_field='datagov_ID', db_column='datagov_ID', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.broken_id)

class Retag(models.Model):
    retag_id = models.AutoField(primary_key=True)
    cap_id = models.ForeignKey('CAPInstance', db_column='cap_id', on_delete=models.CASCADE)
    datagov_ID = models.ForeignKey('Masterlist', to_field='datagov_ID', db_column='datagov_ID', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.retag_id)

class QAUpdates(models.Model):
    qa_id = models.AutoField(primary_key=True)
    cap_id = models.ForeignKey('CAPInstance', db_column='cap_id', on_delete=models.CASCADE)
    datagov_ID = models.ForeignKey('Masterlist', to_field='datagov_ID', db_column='datagov_ID', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True, blank=True)
    title =models.CharField(max_length=1000, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    catalog_url = models.CharField(max_length=1000, null=True, blank=True)
    metadata_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.qa_id)

class NotInMasterlist(models.Model):
    nml_id = models.AutoField(primary_key=True)
    cap_id = models.ForeignKey('CAPInstance', db_column='cap_id', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    api_url = models.URLField(max_length=500)
    catalog_url = models.URLField(max_length=500)

    def __str__(self):
        return str(self.nml_id)

'''
# Create your models here.
class CDI_dataset(models.Model):
    date_id = models.CharField(max_length=20, null=True)
    cdi_id = models.IntegerField()
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    organization = models.CharField(max_length=50, null=True)
    catalog_url = models.URLField(null=True)
    api_url = models.URLField(null=True)
    cdi_themes = models.CharField(max_length=200, null=True)
    metadata_type = models.CharField(max_length=50, null=True, blank=True)
    geoplatform_id = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    datagov_ID = models.UUIDField(null=True)

    class Meta:
        abstract = True

class retag(CDI_dataset):
    pass

class broken_api(CDI_dataset):
    pass

class updates_masterlist(CDI_dataset):
    pass

class original_masterlist(CDI_dataset):
    pass

class qa_updates(models.Model):
    date_id = models.CharField(max_length=20, null=True)
    cdi_id = models.IntegerField()
    name = models.CharField(max_length=500)
    title =models.CharField(max_length=500)
    organization = models.CharField(max_length=50, null=True)
    catalog_url = models.URLField(null=True)
    metadata_type = models.CharField(max_length=50, null=True, blank=True)
    datagov_id = models.UUIDField(null=True)

class not_in_masterlist(models.Model):
    date_id = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    api_url = models.URLField(null=True)
    catalog_url = models.URLField(null=True)


class cdi_metrics(models.Model):
    date_id = models.CharField(max_length=20, null=True)
    masterlist_count = models.IntegerField()
    climate_collection_count = models.IntegerField()

class warnings_summary(models.Model):
    date_id = models.CharField(max_length=20, null=True)
    total_warnings = models.IntegerField()
    broken_urls = models.IntegerField()
    lost_climate_tag = models.IntegerField()
    not_in_masterlist = models.IntegerField()
'''



