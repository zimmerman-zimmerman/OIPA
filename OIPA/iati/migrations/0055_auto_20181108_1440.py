# Generated by Django 2.0.6 on 2018-11-08 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0054_auto_20181108_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentlink',
            name='result_indicator_baseline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='baseline_document_links', to='iati.ResultIndicatorBaseline'),
        ),
    ]
