# Generated by Django 4.0.6 on 2023-07-29 07:59

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_newsmodels_new_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodels',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='news_title'),
        ),
    ]
