# Generated by Django 2.0.3 on 2018-04-11 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0008_auto_20180329_1601'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name': 'варіант', 'verbose_name_plural': 'варіанти'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'статус', 'verbose_name_plural': 'статуси'},
        ),
        migrations.AlterField(
            model_name='option',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='status.Status', verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(max_length=1024, verbose_name='значення'),
        ),
        migrations.AlterField(
            model_name='status',
            name='is_static',
            field=models.NullBooleanField(default=None, verbose_name='статичне поле?'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=4096, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='status',
            name='stations',
            field=models.ManyToManyField(blank=True, related_name='statuses', to='territory.PollingStation', verbose_name='дільниці'),
        ),
        migrations.AlterField(
            model_name='status',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'число'), (2, 'рядок')], verbose_name='тип'),
        ),
    ]
