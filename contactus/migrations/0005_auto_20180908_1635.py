# Generated by Django 2.1 on 2018-09-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0004_auto_20180906_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Done'),
        ),
    ]
