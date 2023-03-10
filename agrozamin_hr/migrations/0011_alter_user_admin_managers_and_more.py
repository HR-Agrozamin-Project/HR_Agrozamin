# Generated by Django 4.1.4 on 2023-01-06 09:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0010_alter_user_admin_managers_remove_user_admin_username_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user_admin',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user_admin',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user_admin',
            name='spouse_name',
        ),
        migrations.AddField(
            model_name='user_admin',
            name='username',
            field=models.CharField(default=1, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_admin',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
