# Generated by Django 4.2.7 on 2024-02-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='typ',
            field=models.CharField(default='Action', max_length=200),
        ),
    ]
