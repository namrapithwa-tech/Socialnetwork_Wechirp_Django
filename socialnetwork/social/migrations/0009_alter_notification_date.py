# Generated by Django 4.1.5 on 2023-03-29 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
