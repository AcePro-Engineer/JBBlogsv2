# Generated by Django 3.0.2 on 2020-03-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='preview_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/images'),
        ),
    ]