# Generated by Django 3.0.4 on 2020-04-15 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200414_2129'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Main',
        ),
        migrations.RemoveField(
            model_name='forms',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='forms',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='forms',
            name='username',
        ),
        migrations.AddField(
            model_name='forms',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forms',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='forms',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='forms',
            table='marks',
        ),
    ]