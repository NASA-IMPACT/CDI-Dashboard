from django.db import models


# Create your models here.
class Retag(models.Model):
    cdi_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=50, null=True)
    catalog_url = models.URLField(null=True)
    api_url = models.URLField(null=True)
    cdi_themes = models.CharField(max_length=50, null=True)
    metadata_type = models.CharField(max_length=50, null=True, blank=True)
    geoplatform_id = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    datagov_ID = models.UUIDField(null=True)


# class JsonExport2(models.Model):
#     pass



# class JsonExport3(models.Model):
#     pass



# class JsonExport4(models.Model):
#     pass
