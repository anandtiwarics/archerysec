# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-04-03 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("compliance", "0005_inspec_scan_results_db_controls_tags_audit_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inspec_scan_db",
            name="inspec_failed",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="inspec_scan_db",
            name="inspec_passed",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="inspec_scan_db",
            name="inspec_skipped",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
