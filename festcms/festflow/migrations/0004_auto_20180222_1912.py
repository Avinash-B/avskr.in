# Generated by Django 2.0.2 on 2018-02-22 19:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festflow', '0003_eventgroup_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='group_identifier',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[a-z]*$', 'Only lower case alphabets are allowed.')]),
        ),
    ]
