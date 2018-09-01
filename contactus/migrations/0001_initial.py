# Generated by Django 2.1 on 2018-09-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contactNo', models.CharField(max_length=20)),
                ('emailId', models.CharField(blank=True, max_length=254)),
                ('query', models.TextField()),
            ],
        ),
    ]
