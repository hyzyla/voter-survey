# Generated by Django 2.0.3 on 2018-04-11 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0004_auto_20180408_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constituency',
            options={'verbose_name': 'округ', 'verbose_name_plural': 'округи'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'район', 'verbose_name_plural': 'райони'},
        ),
        migrations.AlterModelOptions(
            name='pollingstation',
            options={'verbose_name': 'дільниця', 'verbose_name_plural': 'дільниці'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'область', 'verbose_name_plural': 'області'},
        ),
        migrations.AlterField(
            model_name='constituency',
            name='description',
            field=models.CharField(blank=True, max_length=8192, null=True, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='name',
            field=models.CharField(max_length=2048, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='stations',
            field=models.ManyToManyField(related_name='constituencies', to='territory.PollingStation', verbose_name='дільниці'),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='year',
            field=models.PositiveIntegerField(null=True, verbose_name='рік'),
        ),
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.CharField(max_length=2048, null=True, verbose_name='місто'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=2048, verbose_name='назва'),
        ),
        migrations.AlterField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='territory.Region', verbose_name='область'),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='address',
            field=models.CharField(max_length=2048, null=True, verbose_name='адреса'),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='description',
            field=models.TextField(null=True, verbose_name='опис'),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stations', to='territory.District', verbose_name='район'),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='is_deprecated',
            field=models.BooleanField(default=False, verbose_name='не активна?'),
        ),
        migrations.AlterField(
            model_name='pollingstation',
            name='number',
            field=models.CharField(max_length=256, verbose_name='номер'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='назва'),
        ),
    ]