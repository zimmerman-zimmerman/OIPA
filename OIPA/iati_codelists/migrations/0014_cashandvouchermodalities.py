# Generated by Django 2.0.13 on 2019-10-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iati_codelists', '0013_category_null_on_aid_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashandVoucherModalities',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
