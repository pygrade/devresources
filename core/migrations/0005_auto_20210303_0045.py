# Generated by Django 3.1.7 on 2021-03-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210302_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcecategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]