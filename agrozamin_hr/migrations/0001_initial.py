# Generated by Django 4.1.4 on 2022-12-30 09:54

import agrozamin_hr.models.usermodel
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_name_ru', models.CharField(max_length=200, null=True)),
                ('category_name_uz', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_category_name', models.CharField(max_length=200)),
                ('extra_category_name_ru', models.CharField(max_length=200, null=True)),
                ('extra_category_name_uz', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': "Qo'shimcha kategoriya",
                'verbose_name_plural': "Qo'shimcha kategoriyalar",
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.PositiveIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=9, unique=True, validators=[agrozamin_hr.models.usermodel.validate_length])),
                ('gender', models.CharField(choices=[('E', 'Erkak'), ('A', 'Ayol')], max_length=10)),
                ('education', models.CharField(choices=[("O'rta", "O'rta"), ("O'rta maxsus", "o'rta maxsus"), ('Oliy tugallanmagan', 'Oliy tugallanmagan'), ('Oliy', 'Oliy'), ('Magister', 'Magistr'), ('PhD', 'PhD')], max_length=30)),
                ('age', models.CharField(choices=[('18-24', ' 18 24'), ('25-30', ' 25 30'), ('31-35', ' 31 35'), ('36-45', ' 36 45'), ('46-...', ' 46')], max_length=10)),
                ('cv', models.FileField(upload_to='cv_files')),
                ('test_result', models.FileField(upload_to='test_result_files')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.city')),
                ('extra_skill', models.ManyToManyField(blank=True, null=True, to='agrozamin_hr.extracategory')),
                ('program_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.category')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.city')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_ru', models.TextField(null=True)),
                ('question_uz', models.TextField(null=True)),
                ('A', models.CharField(max_length=200, null=True)),
                ('A_ru', models.CharField(max_length=200, null=True)),
                ('A_uz', models.CharField(max_length=200, null=True)),
                ('B', models.CharField(max_length=200, null=True)),
                ('B_ru', models.CharField(max_length=200, null=True)),
                ('B_uz', models.CharField(max_length=200, null=True)),
                ('C', models.CharField(max_length=200, null=True)),
                ('C_ru', models.CharField(max_length=200, null=True)),
                ('C_uz', models.CharField(max_length=200, null=True)),
                ('D', models.CharField(max_length=200, null=True)),
                ('D_ru', models.CharField(max_length=200, null=True)),
                ('D_uz', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('ans_ru', models.CharField(max_length=200, null=True)),
                ('ans_uz', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.category')),
                ('category_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.category')),
                ('category_uz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.category')),
            ],
            options={
                'verbose_name': 'Savol',
                'verbose_name_plural': 'Savollar',
            },
        ),
        migrations.CreateModel(
            name='ExtraQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_ru', models.TextField(null=True)),
                ('question_uz', models.TextField(null=True)),
                ('A', models.CharField(max_length=200, null=True)),
                ('A_ru', models.CharField(max_length=200, null=True)),
                ('A_uz', models.CharField(max_length=200, null=True)),
                ('B', models.CharField(max_length=200, null=True)),
                ('B_ru', models.CharField(max_length=200, null=True)),
                ('B_uz', models.CharField(max_length=200, null=True)),
                ('C', models.CharField(max_length=200, null=True)),
                ('C_ru', models.CharField(max_length=200, null=True)),
                ('C_uz', models.CharField(max_length=200, null=True)),
                ('D', models.CharField(max_length=200, null=True)),
                ('D_ru', models.CharField(max_length=200, null=True)),
                ('D_uz', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('ans_ru', models.CharField(max_length=200, null=True)),
                ('ans_uz', models.CharField(max_length=200, null=True)),
                ('extra_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.extracategory')),
                ('extra_category_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.extracategory')),
                ('extra_category_uz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agrozamin_hr.extracategory')),
            ],
            options={
                'verbose_name': "Qo'shimcha savol",
                'verbose_name_plural': "Qo'shimcha savollar",
            },
        ),
        migrations.CreateModel(
            name='User_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administratorlar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
