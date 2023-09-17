# Generated by Django 4.2.5 on 2023-09-17 18:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_restaurant_dine_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='closing_time',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='days',
            field=models.CharField(choices=[('SU', 'Sunday'), ('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday')], default='SU', max_length=2),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='opening_time',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='dine_in',
            field=models.BooleanField(default=False),
        ),
    ]