# Generated by Django 2.0.3 on 2018-04-11 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0003_auto_20180411_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='territory.PollingStation', verbose_name='дільниця'),
        ),
    ]