# Generated by Django 3.0.4 on 2020-04-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_data_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
