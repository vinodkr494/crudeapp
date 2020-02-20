# Generated by Django 2.2 on 2019-12-23 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_problemreporting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='problemreporting',
            name='report',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reports.Report'),
            preserve_default=False,
        ),
    ]
