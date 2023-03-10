# Generated by Django 4.1.5 on 2023-01-09 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haversine', '0003_position_latitude_two_position_longitude_two_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='latitude_two',
        ),
        migrations.RemoveField(
            model_name='position',
            name='longitude_two',
        ),
        migrations.RemoveField(
            model_name='position',
            name='place',
        ),
        migrations.RemoveField(
            model_name='position',
            name='place_two',
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=90, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='haversine.position')),
            ],
        ),
    ]
