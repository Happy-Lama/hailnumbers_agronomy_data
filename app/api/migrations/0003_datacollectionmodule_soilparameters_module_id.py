# Generated by Django 5.0.3 on 2024-04-16 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_soilparameters_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCollectionModule',
            fields=[
                ('module_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='soilparameters',
            name='module_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.datacollectionmodule'),
        ),
    ]