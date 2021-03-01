# Generated by Django 3.1.7 on 2021-03-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanremo', '0003_auto_20210228_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valutazione',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='valutazione',
            name='voto',
        ),
        migrations.AddField(
            model_name='valutazione',
            name='voto_brano',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valutazione',
            name='voto_interpretazione',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valutazione',
            name='voto_outfit',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]