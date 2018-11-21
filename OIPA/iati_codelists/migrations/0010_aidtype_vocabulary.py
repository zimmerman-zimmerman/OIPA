# Generated by Django 2.0.6 on 2018-07-12 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati_vocabulary', '0004_aidtypevocabulary'),
        ('iati_codelists', '0009_auto_20180711_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='aidtype',
            name='vocabulary',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='iati_vocabulary.AidTypeVocabulary'),
        ),
    ]
