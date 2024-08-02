# Generated by Django 5.0.6 on 2024-07-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_donation_delete_donated_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='breakfast_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donation',
            name='dinner_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donation',
            name='lunch_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donation',
            name='meal_type',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=10),
        ),
    ]