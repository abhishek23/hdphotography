# Generated by Django 2.1 on 2018-08-21 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weoffer', '0005_event_sequence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='featured_thumbnails')),
                ('coverImage', models.ImageField(upload_to='featured_cover_images')),
                ('description', models.TextField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_ids', to='weoffer.Event')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='featured_images')),
                ('featured_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='weoffer.Featured')),
            ],
        ),
    ]