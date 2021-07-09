# Generated by Django 3.2.5 on 2021-07-08 11:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='custom_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.CharField(blank=True, max_length=1)),
                ('profile_pic', models.ImageField(blank=True, upload_to='uploads/')),
            ],
        ),
    ]