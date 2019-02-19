# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-19 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultsLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_morgan_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('k_morgan_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('lr_ph_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('ph_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('mg_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('cu_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('zn_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('er_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('mn_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('organic_result', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('submit_date', models.DateField(auto_now_add=True)),
                ('sample_ref', models.CharField(max_length=50)),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_ref_1', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_ref_2', models.CharField(blank=True, max_length=50, null=True)),
                ('sample_location', geoposition.fields.GeopositionField(max_length=42, null=True)),
                ('sample_address', models.CharField(blank=True, max_length=50, null=True)),
                ('sample_date', models.DateField(default=django.utils.timezone.now)),
                ('analysis_req', models.CharField(choices=[('1', 'Soil 1-SS Basic'), ('2', 'Soil 2-SS Dairy/Beef/Sheep/Horses'), ('3', 'Soil 3-SS Sheep/Tillage'), ('4', 'Soil 4-SS Tillage'), ('5', 'Soil 5-SS Horticulture'), ('6', 'Soil 6-SS Tillage/Grassland (S1 + Mg)'), ('7', 'Soil 7-SS Organic Matter'), ('8', 'Soil 8-SS Tillage (S6 + S7)'), ('9', 'Soil 9-SS Tillage (S4 + S7)')], max_length=50)),
                ('soil_type', models.CharField(blank=True, choices=[('GW', 'Well-graded gravel, fine to coarse gravel'), ('GP', 'Poorly graded gravel'), ('GM', 'Silty gravel'), ('GC', 'Clayey gravel'), ('SW', 'Well-graded sand, fine to coarse sand'), ('SP', 'Poorly graded sand'), ('SM', 'Silty sand'), ('SC', 'Clayey sand'), ('ML', 'Silt'), ('CL', 'Clay of low plasticity, lean clay'), ('OL', 'Organic silt, organic clay'), ('MH', 'Silt of high plasticity, elastic silt'), ('CH', 'Clay of high plasticity, fat clay'), ('OH', 'Organic clay, organic silt'), ('Pt', 'Peat')], default='', max_length=50)),
                ('land_use', models.CharField(blank=True, choices=[('B', 'Beef'), ('D', 'Dairy'), ('G', 'Grassland'), ('H', 'Horticulture'), ('S', 'Sheep'), ('T', 'Tillage')], default='', max_length=50)),
                ('other_comments', models.CharField(blank=True, max_length=100)),
                ('sample_condition', models.CharField(blank=True, max_length=50)),
                ('recieved_date', models.DateField(blank=True, null=True)),
                ('recieved_by', models.CharField(blank=True, max_length=50, null=True)),
                ('batch_no', models.DateField(blank=True, null=True)),
                ('test_start_date', models.DateField(blank=True, null=True)),
                ('test_end_date', models.DateField(blank=True, null=True)),
                ('tested_by', models.CharField(blank=True, max_length=50, null=True)),
                ('lab_comments', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Submitted', 'Submitted'), ('Received', 'Received'), ('Testing', 'Testing'), ('Complete', 'Complete')], default='Submitted', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='resultslineitem',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Sample'),
        ),
    ]
