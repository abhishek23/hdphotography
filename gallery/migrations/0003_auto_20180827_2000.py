# Generated by Django 2.1 on 2018-08-27 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180827_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='columnId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.GalleryColumn'),
        ),
    ]
