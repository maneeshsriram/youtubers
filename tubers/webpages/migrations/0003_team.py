# Generated by Django 3.1.5 on 2021-01-19 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_slider_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=75)),
                ('fb_link', models.CharField(max_length=250)),
                ('insta_link', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='media/team/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
