from django.db import models
from django.utils import timezone
from geoposition import Geoposition
from django.conf import settings
from geoposition.fields import GeopositionField

# Create your models here.

class SampleStatus(models.Model):

    STATUS_CHOICES = ((('Submitted'),('Submitted')),
                      (('Received'),('Received')),
                      (('Complete'),('Complete')))

    sample_ref = models.CharField(max_length=50,
                                  blank=False)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='Submitted',)

    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.CASCADE,
                                     related_name = 'submittedby',)

    submit_date = models.DateTimeField(blank=True,
                                     null=True)

    received_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    limit_choices_to={'is_staff': True},
                                    on_delete=models.CASCADE,
                                    related_name = 'recievedby',
                                    blank=True,
                                    null=True)
    received_date = models.DateTimeField(blank=True,
                                     null=True)

    tested_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  limit_choices_to={'is_staff': True},
                                  on_delete=models.CASCADE,
                                  related_name = 'testedby',
                                  blank=True,
                                  null=True)
    tested_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.sample_ref, self.status)

class SampleDetails(models.Model):
    SOIL_TYPES = ((('Clay - low plasticity, lean clay'),('Clay - low plasticity, lean clay')),
                  (('Clay - high plasticity, fat clay'),('Clay - high plasticity, fat clay')),
                  (('Clay - organic'),('Clay - organic')),
                  (('Gravel - well-graded, fine to coarse gravel'),('Gravel - well-graded, fine to coarse gravel')),
                  (('Gravel - poorly graded'),('Gravel - poorly graded')),
                  (('Gravel - silty'),('Gravel - silty')),
                  (('Gravel - clayey'),('Gravel - clayey')),
                  (('Sand - well-graded, fine to coarse Sand'),('Sand - well-graded, fine to coarse Sand')),
                  (('Sand - poorly graded'),('Sand - poorly graded')),
                  (('Sand - silty'),('Sand - silty')),
                  (('Sand - clayey'),('Sand - clayey')),
                  (('Peat'),('Peat')),
                  (('Silt - low plasticity, lean silt'),('Silt - low plasticity, lean silt')),
                  (('Silt - high plasticity, fat silt'),('Silt - high plasticity, fat silt')),
                  (('Silt - organic'),('Silt - organic')))


    LAND_USES = ((('Beef'), ('Beef')),
                 (('Dairy'), ('Dairy')),
                 (('Grassland'), ('Grassland')),
                 (('Horticulture'), ('Horticulture')),
                 (('Sheep'), ('Sheep')),
                 (('Tillage'), ('Tillage')))

    sample = models.ForeignKey(SampleStatus, null=True)

    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_ref_1 = models.CharField(max_length=50, blank=True, null=True)
    customer_ref_2 = models.CharField(max_length=50, blank=True, null=True)
    sample_location = GeopositionField(null=True)
    sample_address = models.CharField(max_length=250, blank=True, null=True)
    sample_date = models.DateField(blank=False, default=timezone.now)
    soil_type = models.CharField(max_length=50, choices=SOIL_TYPES)
    land_use = models.CharField(max_length=50, choices=LAND_USES)
    other_comments = models.TextField(max_length=254, blank=True)


    def __str__(self):
        return "{0}-{1}-Details".format(self.id, self.sample.sample_ref)

class SampleResults(models.Model):
    sample = models.ForeignKey(SampleStatus, null=False, limit_choices_to={'status': 'Received'},)
    p = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    k = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    lr_ph = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ph = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    other_comments = models.TextField(max_length=254, blank=True)

    def __str__(self):
        return "{0}-{1}-Results".format(self.id, self.sample.sample_ref)
