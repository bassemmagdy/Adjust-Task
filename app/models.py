# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class PerformanceMetric(models.Model):
    date = models.DateField(default=None)
    channel = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=20, default=None)
    os = models.CharField(max_length=20, default=None)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    spend = models.FloatField(default=0.0)
    revenue = models.FloatField(default=0.0)