# Generated by Django 4.1.4 on 2023-01-06 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('agrozamin_hr', '0008_rename_user_admin_admin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='User_admin',
        ),
    ]