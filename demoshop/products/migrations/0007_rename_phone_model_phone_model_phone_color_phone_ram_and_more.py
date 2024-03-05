# Generated by Django 5.0.3 on 2024-03-05 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_phone_series'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='phone_model',
            new_name='model',
        ),
        migrations.AddField(
            model_name='phone',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='ram',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='SmartWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=20)),
                ('series', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=200000.0, max_digits=10)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]