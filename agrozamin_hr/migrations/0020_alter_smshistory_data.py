# Generated by Django 4.1.4 on 2023-01-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0019_alter_smshistory_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smshistory',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
