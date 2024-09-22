# Generated by Django 5.1.1 on 2024-09-22 06:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destination', '0002_priceadvantage_alter_destination_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='USD', max_length=3)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trip.category')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='destination.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('transport', 'Transport'), ('lodging', 'Lodging'), ('activities', 'Activities')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_items', to='trip.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('item', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound')], max_length=3)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='trip.trip')),
            ],
        ),
    ]
