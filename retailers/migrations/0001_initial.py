# Generated by Django 3.0.5 on 2020-04-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('product', models.CharField(choices=[('Select', 'Select'), ('Masks', 'Masks'), ('Ventilators', 'Ventilators'), ('Medicines & medical equipments', 'Medicines & medical equipments'), ('Rooms', 'Rooms'), ('Beds', 'Beds'), ('Food', 'Food')], default='Select', max_length=80)),
                ('quantity', models.IntegerField(default=0)),
                ('coordinates', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]