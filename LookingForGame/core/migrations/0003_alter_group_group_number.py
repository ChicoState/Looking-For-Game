# Generated by Django 4.0.2 on 2022-04-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_number',
            field=models.IntegerField(null=True),
        ),
    ]
