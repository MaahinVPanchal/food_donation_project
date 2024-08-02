# Generated by Django 5.0.6 on 2024-07-12 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_donation_breakfast_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='breakfast_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='dinner_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='lunch_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Invalid phone number')]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', 'Invalid phone number')]),
        ),
    ]
