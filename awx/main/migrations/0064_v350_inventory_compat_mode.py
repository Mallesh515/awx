# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-28 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_v350_org_host_limits'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorysource',
            name='compatibility_mode',
            field=models.BooleanField(default=True, help_text='This field is deprecated and will be removed in a future release. Restore old hostvars and names from before the transition to inventory plugins.'),
        ),
        migrations.AddField(
            model_name='inventoryupdate',
            name='compatibility_mode',
            field=models.BooleanField(default=True, help_text='This field is deprecated and will be removed in a future release. Restore old hostvars and names from before the transition to inventory plugins.'),
        )
    ]