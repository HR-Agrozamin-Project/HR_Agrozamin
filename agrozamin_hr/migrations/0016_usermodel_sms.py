# Generated by Django 4.1.4 on 2023-01-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0015_remove_extraquetionresult_correct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='sms',
            field=models.BooleanField(default='False'),
        ),
    ]