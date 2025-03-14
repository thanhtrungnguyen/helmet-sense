# Generated by Django 5.0.12 on 2025-03-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicPricing',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bike_type', models.CharField(max_length=50)),
                ('time_of_day', models.CharField(blank=True, max_length=10, null=True)),
                ('day_of_week', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('weather_condition', models.CharField(blank=True, max_length=50, null=True)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ai_adjusted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'unique_together': {('bike_type', 'time_of_day', 'day_of_week', 'weather_condition')},
            },
        ),
    ]
