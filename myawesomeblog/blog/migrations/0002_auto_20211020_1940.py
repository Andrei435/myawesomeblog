# Generated by Django 3.2.8 on 2021-10-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='event_image/'),
        ),
    ]