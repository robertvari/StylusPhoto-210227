# Generated by Django 3.1.7 on 2021-03-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_aboutpagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpagemodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
