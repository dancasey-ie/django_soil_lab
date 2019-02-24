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
    SOIL_TYPES = ((('Clay - low plasticity, lean'),('Clay - low plasticity, lean')),
                  (('Clay - high plasticity, fat'),('Clay - high plasticity, fat')),
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
                  (('Silt - low plasticity, lean'),('Silt - low plasticity, lean')),
                  (('Silt - high plasticity, fat'),('Silt - high plasticity, fat')),
                  (('Silt - organic'),('Silt - organic')))


    LAND_USES = ((('Beef'), ('Beef')),
                 (('Dairy'), ('Dairy')),
                 (('Grassland'), ('Grassland')),
                 (('Horticulture'), ('Horticulture')),
                 (('Sheep'), ('Sheep')),
                 (('Tillage'), ('Tillage')))

    sample = models.ForeignKey(SampleStatus, null=False)

    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_ref_1 = models.CharField(max_length=50, blank=True, null=True)
    customer_ref_2 = models.CharField(max_length=50, blank=True, null=True)
    sample_location = GeopositionField(null=True)
    sample_address = models.CharField(max_length=50, blank=True, null=True)
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





class Sample(models.Model):
    TEST_CHOICES = ((('1'),('Soil 1-SS Basic')),
                    (('2'),('Soil 2-SS Dairy/Beef/Sheep/Horses')),
                    (('3'),('Soil 3-SS Sheep/Tillage')),
                    (('4'),('Soil 4-SS Tillage')),
                    (('5'),('Soil 5-SS Horticulture')),
                    (('6'),('Soil 6-SS Tillage/Grassland (S1 + Mg)')),
                    (('7'),('Soil 7-SS Organic Matter')),
                    (('8'),('Soil 8-SS Tillage (S6 + S7)')),
                    (('9'),('Soil 9-SS Tillage (S4 + S7)')))

    SOIL_TYPES = ((('GW'),('Well-graded gravel, fine to coarse gravel')),
                  (('GP'),('Poorly graded gravel')),
                  (('GM'),('Silty gravel')),
                  (('GC'),('Clayey gravel')),
                  (('SW'),('Well-graded sand, fine to coarse sand')),
                  (('SP'),('Poorly graded sand')),
                  (('SM'),('Silty sand')),
                  (('SC'),('Clayey sand')),
                  (('ML'),('Silt')),
                  (('CL'),('Clay of low plasticity, lean clay')),
                  (('OL'),('Organic silt, organic clay')),
                  (('MH'),('Silt of high plasticity, elastic silt')),
                  (('CH'),('Clay of high plasticity, fat clay')),
                  (('OH'),('Organic clay, organic silt')),
                  (('Pt'),('Peat')))

    LAND_USES = ((('B'), ('Beef')),
                 (('D'), ('Dairy')),
                 (('G'), ('Grassland')),
                 (('H'), ('Horticulture')),
                 (('S'), ('Sheep')),
                 (('T'), ('Tillage')))

    STATUS_CHOICES = ((('Submitted'),('Submitted')),
                      (('Received'),('Received')),
                      (('Testing'),('Testing')),
                      (('Complete'),('Complete')))

    # set by user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    submit_date = models.DateField(auto_now_add=True)

    # user inputs
    sample_ref = models.CharField(max_length=50, blank=False)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_ref_1 = models.CharField(max_length=50, blank=True, null=True)
    customer_ref_2 = models.CharField(max_length=50, blank=True, null=True)
    sample_location = GeopositionField(null=True)
    sample_address = models.CharField(max_length=50, blank=True, null=True)
    sample_date = models.DateField(blank=False, default=timezone.now)
    analysis_req = models.CharField(max_length=50, choices=TEST_CHOICES)
    soil_type = models.CharField(max_length=50, choices=SOIL_TYPES, blank=True, default='')
    land_use = models.CharField(max_length=50, choices=LAND_USES, blank=True, default='')
    other_comments = models.TextField(max_length=254, blank=True)

    #automated
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Submitted')

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.sample_ref, self.status)

class Soil1Results(models.Model):
    sample = models.ForeignKey(Sample, null=False)
    recieved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'is_staff': True},
        on_delete=models.CASCADE,
    )
    recieved_date = models.DateField(blank=True, null=True)
    sample_condition = models.CharField(max_length=50, blank=True)
    batch_no = models.CharField(max_length=50, blank=True)
    test_start_date = models.DateField(blank=True, null=True)
    p_morgan_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    k_morgan_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    lr_ph_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ph_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    lab_comments = models.TextField(max_length=254, blank=True)
    tested_by = models.CharField(max_length=50, blank=True)
    test_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{0}-{1}-Soil 1".format(self.id, self.sample.sample_ref)

class Soil2Results(models.Model):
    sample = models.ForeignKey(Sample, null=False)
    recieved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'is_staff': True},
        on_delete=models.CASCADE,
    )
    recieved_date = models.DateField(blank=True, null=True)
    sample_condition = models.CharField(max_length=50, blank=True)
    batch_no = models.DateField(blank=True, null=True)
    test_start_date = models.DateField(blank=True, null=True)
    p_morgan_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    k_morgan_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    lr_ph_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ph_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    mg_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cu_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    zn_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    er_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    mn_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    organic_result = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    lab_comments = models.TextField(max_length=254, blank=True)
    tested_by = models.CharField(max_length=50, blank=True)
    test_end_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return "{0}-{1}-Soil 2".format(self.id, self.sample.sample_ref)