from django.db import models


# Create your models here.
class CDI_dataset(models.Model):
    date_id = model.UUIDField(primary_key=True)
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

class retag(CDI_dataset):
    pass

class broken_api(CDI_dataset):
    pass

class updates_masterlist(CDI_dataset):
    pass

class original_masterlist(CDI_dataset):
    pass

class qa_updates(models.Model):
    date_id = 
    cdi_id = 
    name = 
    title =
    organization = 
    catalog_url = 
    metadata_type = 
    datagov_id = 

class not_in_masterlist(models.Model):
    date_id = 
    title =
    name =
    api_url =
    catalog_url =


class cdi_metrics(models.model):
    date_id = 
    masterlist_count = 
    climate_collection_count = 

class warnings_summary(models.model):
    date_id = 
    total_warnings = 
    broken_urls =
    lost_climate_tag = 
    not_in_masterlist =  




