# Generated by Django 2.1 on 2018-08-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weoffer', '0004_auto_20180809_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sequence',
            field=models.IntegerField(null=True),
        ),
    ]