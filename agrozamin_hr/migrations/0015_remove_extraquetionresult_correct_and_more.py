# Generated by Django 4.1.4 on 2023-01-07 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrozamin_hr', '0014_rename_userresult_quetionresult_extraquetionresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extraquetionresult',
            name='correct',
        ),
        migrations.RemoveField(
            model_name='quetionresult',
            name='correct',
        ),
        migrations.AddField(
            model_name='extraquetionresult',
            name='extra_category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.extracategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraquetionresult',
            name='result',
            field=models.CharField(default='True', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extraquetionresult',
            name='user_answer',
            field=models.CharField(default='A', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quetionresult',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quetionresult',
            name='result',
            field=models.CharField(default='True', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quetionresult',
            name='user_answer',
            field=models.CharField(default='A', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='chat_id',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
