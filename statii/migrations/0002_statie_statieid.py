# Generated by Django 4.0.4 on 2022-05-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statii', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statie',
            name='StatieID',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
