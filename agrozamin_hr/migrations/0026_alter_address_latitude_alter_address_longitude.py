# Generated by Django 4.1.4 on 2023-01-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0025_remove_address_date_alter_address_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
