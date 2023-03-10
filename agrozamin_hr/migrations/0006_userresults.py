# Generated by Django 4.1.4 on 2023-01-05 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0005_alter_usermodel_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.BooleanField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.usermodel')),
            ],
        ),
    ]
