# Generated by Django 4.2.15 on 2024-08-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('normal', 'Normal'), ('extra', 'Extra'), ('additional', 'Additional'), ('cosmic', 'Cosmic')], max_length=255, null=True)),
            ],
        ),
    ]
