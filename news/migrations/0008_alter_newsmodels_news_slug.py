# Generated by Django 4.0.6 on 2023-07-29 08:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newsmodels_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodels',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='news_title'),
        ),
    ]
