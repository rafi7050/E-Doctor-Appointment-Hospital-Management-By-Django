# Generated by Django 2.2 on 2020-12-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_auto_20201210_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_presscription',
            name='presscription1',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
