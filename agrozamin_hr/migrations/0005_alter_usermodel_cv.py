# Generated by Django 4.1.4 on 2023-01-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0004_alter_usermodel_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='cv',
            field=models.FileField(upload_to='cv_files'),
        ),
    ]