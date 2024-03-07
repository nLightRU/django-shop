# Generated by Django 5.0.3 on 2024-03-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_delete_smartwatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/phone/'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]