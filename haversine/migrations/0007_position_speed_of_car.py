# Generated by Django 4.1.5 on 2023-02-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haversine', '0006_position_latitude_two_position_longitude_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='speed_of_car',
            field=models.DecimalField(decimal_places=8, max_digits=26, null=True),
        ),
    ]
