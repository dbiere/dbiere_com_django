# Generated by Django 2.1.3 on 2018-12-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20181230_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='continuation_of_uspto_number',
            field=models.IntegerField(blank=True),
        ),
    ]