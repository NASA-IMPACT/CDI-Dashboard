from django.db import models
from datetime import datetime

class Masterlist(models.Model):
    cdi_id = models.AutoField(primary_key=True)
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

class CAP_Instance(models.Model):
    cap_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today())
    masterlist_count = models.IntegerField()
    climate_collection_count = models.IntegerField()
    broken_urls = models.IntegerField()
    lost_climate_tag = models.IntegerField()
    not_in_masterlist = models.IntegerField()
    total_warnings = models.IntegerField()

class Broken_API(models.Model):
    broken_id = models.AutoField(primary_key=True)
    cap_id = models.IntegerField()
    datagov_ID = models.UUIDField()

class Retag(models.Model):
    retag_id = models.AutoField(primary_key=True)
    cap_id = models.IntegerField()
    datagov_ID = models.UUIDField()

class QA_Updates(models.Model):
    qa_id = models.AutoField(primary_key=True)
    cap_id = models.IntegerField()
    datagov_ID = models.UUIDField()
    name = models.CharField(max_length=500)
    title =models.CharField(max_length=500)
    organization = models.CharField(max_length=50, null=True)
    catalog_url = models.URLField(null=True)
    metadata_type = models.CharField(max_length=50, null=True, blank=True)

class Not_in_Masterlist(models.Model):
    nml_id = models.AutoField(primary_key=True)
    cap_id = models.IntegerField()
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    api_url = models.URLField(null=True)
    catalog_url = models.URLField(null=True)

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



