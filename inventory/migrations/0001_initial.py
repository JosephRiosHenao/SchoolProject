# Generated by Django 4.0.3 on 2022-06-05 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100, unique=True)),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(default='', max_length=100, unique=True)),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='UnitMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100, unique=True)),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UnitMeters',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SubCategories',
                'unique_together': {('category', 'description')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('code_bar', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField(default=0)),
                ('last_buy', models.DateField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.brand')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.subcategory')),
                ('unit_meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.unitmeter')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('user_modified', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'unique_together': {('code', 'code_bar')},
            },
        ),
    ]
