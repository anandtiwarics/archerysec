# Generated by Django 3.1.2 on 2020-10-04 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("manual_scan", "0009_manual_scan_results_db_poc_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="manual_scan_results_db",
            old_name="vuln_fixed",
            new_name="vuln_status",
        ),
    ]
