# Generated by Django 5.1.4 on 2024-12-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_alter_addmission_sadddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmission',
            name='sadddate',
            field=models.DateField(),
        ),
    ]
