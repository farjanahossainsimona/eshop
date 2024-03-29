# Generated by Django 3.2.4 on 2021-06-12 08:14

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('email_verify', models.CharField(default='0', max_length=10)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('phone_verify', models.CharField(default='0', max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=100, null=True)),
                ('password', models.CharField(max_length=264)),
                ('password_recovery', models.CharField(default='0', max_length=10)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=account.models.profile_pic_path)),
                ('address', models.TextField(blank=True, null=True)),
                ('district', models.CharField(blank=True, choices=[('manikganj', 'Manikganj'), ('dhaka', 'Dhaka'), ('faridpur', 'Faridpur')], max_length=64, null=True)),
                ('account_active', models.CharField(default='0', max_length=1)),
                ('account_block', models.CharField(default='0', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
    ]
