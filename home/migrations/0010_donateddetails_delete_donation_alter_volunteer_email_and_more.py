# Generated by Django 5.0.6 on 2024-07-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_donation_breakfast_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonatedDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_type', models.CharField(max_length=100)),
                ('breakfast', models.BooleanField(default=False)),
                ('breakfast_quantity', models.IntegerField(default=0)),
                ('breakfast_time', models.TimeField(blank=True, null=True)),
                ('lunch', models.BooleanField(default=False)),
                ('lunch_quantity', models.IntegerField(default=0)),
                ('lunch_time', models.TimeField(blank=True, null=True)),
                ('dinner', models.BooleanField(default=False)),
                ('dinner_quantity', models.IntegerField(default=0)),
                ('dinner_time', models.TimeField(blank=True, null=True)),
                ('meal_prepared', models.CharField(max_length=100)),
                ('restaurant_name', models.CharField(max_length=200)),
                ('restaurant_address', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]