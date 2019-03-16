from django.db import models
from django.utils import timezone
from geoposition import Geoposition
from django.conf import settings
from geoposition.fields import GeopositionField
from checkout.models import Order

# Create your models here.


class SampleStatus(models.Model):
    """Sample Status model is automatically generated when an sample is
    ordered, it is updated automatically as the sample gets processesed"""
    STATUS_CHOICES = ((('Ordered'), ('Ordered')),
                      (('Dispatched'), ('Dispatched')),
                      (('Submitted'), ('Submitted')),
                      (('Received'), ('Received')),
                      (('Complete'), ('Complete')))

    TEST_CHOICES = ((('SS1'), ('Soil 1 - Basic')),
                    (('SS2'), ('Soil 2 - Beef, Sheep & Horses')),)

    order = models.ForeignKey(Order,
                              null=False)
    sample_ref = models.CharField(max_length=50,
                                  blank=False)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='Ordered',)
    testing_required = models.CharField(max_length=50,
                                        choices=TEST_CHOICES)
    ordered_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.CASCADE,
                                   related_name='orderedby',
                                   blank=True,
                                   null=True)
    ordered_date = models.DateTimeField(blank=True,
                                        null=True)
    dispatched_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='dispatchedby',
                                      blank=True,
                                      null=True)
    dispatched_date = models.DateTimeField(blank=True,
                                           null=True)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.CASCADE,
                                     related_name='submittedby',
                                     blank=True,
                                     null=True)
    submit_date = models.DateTimeField(blank=True,
                                       null=True)
    received_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    limit_choices_to={'is_staff': True},
                                    on_delete=models.CASCADE,
                                    related_name='recievedby',
                                    blank=True,
                                    null=True)
    received_date = models.DateTimeField(blank=True,
                                         null=True)
    tested_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  limit_choices_to={'is_staff': True},
                                  on_delete=models.CASCADE,
                                  related_name='testedby',
                                  blank=True,
                                  null=True)
    tested_date = models.DateTimeField(blank=True,
                                       null=True)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.testing_required,
                                    self.id,
                                    self.status)


class SampleDetails(models.Model):
    """Sample Details model stores the data entered
    by the customer about each sample"""

    SOIL_TYPES = ((('Clay - low plasticity, lean clay'),
                   ('Clay - low plasticity, lean clay')),
                  (('Clay - high plasticity, fat clay'),
                   ('Clay - high plasticity, fat clay')),
                  (('Clay - organic'),
                   ('Clay - organic')),
                  (('Gravel - well-graded, fine to coarse gravel'),
                   ('Gravel - well-graded, fine to coarse gravel')),
                  (('Gravel - poorly graded'),
                   ('Gravel - poorly graded')),
                  (('Gravel - silty'),
                   ('Gravel - silty')),
                  (('Gravel - clayey'),
                   ('Gravel - clayey')),
                  (('Sand - well-graded, fine to coarse Sand'),
                   ('Sand - well-graded, fine to coarse Sand')),
                  (('Sand - poorly graded'),
                   ('Sand - poorly graded')),
                  (('Sand - silty'),
                   ('Sand - silty')),
                  (('Sand - clayey'),
                   ('Sand - clayey')),
                  (('Peat'),
                   ('Peat')),
                  (('Silt - low plasticity, lean silt'),
                   ('Silt - low plasticity, lean silt')),
                  (('Silt - high plasticity, fat silt'),
                   ('Silt - high plasticity, fat silt')),
                  (('Silt - organic'),
                   ('Silt - organic')))

    LAND_USES = ((('Beef'), ('Beef')),
                 (('Dairy'), ('Dairy')),
                 (('Grassland'), ('Grassland')),
                 (('Horticulture'), ('Horticulture')),
                 (('Sheep'), ('Sheep')),
                 (('Tillage'), ('Tillage')))

    sample = models.ForeignKey(SampleStatus,
                               null=True)

    customer_name = models.CharField(max_length=50,
                                     blank=False)
    customer_ref_1 = models.CharField(max_length=50,
                                      blank=True,
                                      null=True)
    customer_ref_2 = models.CharField(max_length=50,
                                      blank=True,
                                      null=True)
    sample_location = GeopositionField()
    sample_address = models.CharField(max_length=250,
                                      blank=True,
                                      null=True)
    sample_date = models.DateField(blank=False,
                                   default=timezone.now)
    soil_type = models.CharField(max_length=50,
                                 choices=SOIL_TYPES)
    land_use = models.CharField(max_length=50,
                                choices=LAND_USES)
    other_comments = models.TextField(max_length=500,
                                      blank=True)

    def __str__(self):
        return "{0}-{1}-Details".format(self.sample.testing_required,
                                        self.sample.id)


class SampleResults(models.Model):
    """Sample Results stores the sample test results for each sample"""
    sample = models.ForeignKey(SampleStatus,
                               null=False,
                               limit_choices_to={'status': 'Received'},)
    p = models.DecimalField(max_digits=4,
                            decimal_places=2,
                            null=False)
    k = models.DecimalField(max_digits=4,
                            decimal_places=2,
                            null=False)
    lr_ph = models.DecimalField(max_digits=4,
                                decimal_places=2,
                                null=False)
    ph = models.DecimalField(max_digits=4,
                             decimal_places=2,
                             null=False)
    other_comments = models.TextField(max_length=254,
                                      blank=True)

    def __str__(self):
        return "{0}-{1}-Results".format(self.sample.testing_required,
                                        self.sample.id)
