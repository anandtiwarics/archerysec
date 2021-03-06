# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-08 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("compliance", "0003_inspec_scan_results_db_controls_results_backtrace"),
    ]

    operations = [
        migrations.AddField(
            model_name="inspec_scan_db",
            name="inspec_failed",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="inspec_scan_db",
            name="inspec_passed",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="inspec_scan_db",
            name="inspec_skipped",
            field=models.TextField(blank=True, null=True),
        ),
    ]
