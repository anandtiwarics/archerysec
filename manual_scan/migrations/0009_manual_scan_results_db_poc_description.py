# Generated by Django 2.1.8 on 2020-08-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manual_scan", "0008_auto_20200825_0235"),
    ]

    operations = [
        migrations.AddField(
            model_name="manual_scan_results_db",
            name="poc_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
