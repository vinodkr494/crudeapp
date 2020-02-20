# Generated by Django 2.2 on 2019-11-26 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
        ('products', '0001_initial'),
        ('reports', '0002_auto_20191126_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='productionline',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='areas.ProductionLine'),
            preserve_default=False,
        ),
    ]
