# Generated by Django 4.0.3 on 2022-03-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_location_profile_organization_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
