# Generated by Django 4.1.5 on 2023-01-16 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_HTMLField_step_16'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('lng', 'lat')},
        ),
    ]
