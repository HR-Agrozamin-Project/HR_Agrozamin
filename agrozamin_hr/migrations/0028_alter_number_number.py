# Generated by Django 4.1.4 on 2023-01-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0027_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='number',
            field=models.CharField(max_length=9),
        ),
    ]
