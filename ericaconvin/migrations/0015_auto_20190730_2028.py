# Generated by Django 2.2.3 on 2019-07-30 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ericaconvin', '0014_auto_20190730_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilities',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ericaconvin.Category'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='cate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ericaconvin.Category'),
        ),
    ]
