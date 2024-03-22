# Generated by Django 5.0.3 on 2024-03-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoilParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_temperature', models.FloatField(default=0)),
                ('soil_moisture', models.FloatField(default=0)),
                ('soil_ph', models.FloatField(default=0)),
                ('soil_nitrogen_content', models.FloatField(default=0)),
                ('soil_phosphorus_content', models.FloatField(default=0)),
                ('soil_potassium_content', models.FloatField(default=0)),
                ('soil_electrical_conductivity', models.FloatField(default=0)),
            ],
        ),
    ]