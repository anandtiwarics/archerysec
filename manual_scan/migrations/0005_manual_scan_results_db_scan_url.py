# Generated by Django 2.2 on 2019-04-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manual_scan", "0004_manual_scans_db_pentest_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="manual_scan_results_db",
            name="scan_url",
            field=models.TextField(blank=True),
        ),
    ]
