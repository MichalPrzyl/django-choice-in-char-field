# Generated by Django 4.2.15 on 2024-08-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_mymodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
