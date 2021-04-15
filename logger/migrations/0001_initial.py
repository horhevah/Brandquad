# Generated by Django 3.1.3 on 2021-04-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApacheLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unpack_ipv4=True, verbose_name='ip адрес')),
                ('data_time', models.DateTimeField(verbose_name='Дата')),
                ('method', models.CharField(max_length=10, verbose_name='Метод')),
                ('url', models.URLField(verbose_name='URL')),
                ('status_code', models.IntegerField(verbose_name='Код ответа')),
                ('size', models.IntegerField(verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Запись лога',
                'verbose_name_plural': 'Записи лога',
            },
        ),
    ]
