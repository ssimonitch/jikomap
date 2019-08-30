# Generated by Django 2.2.4 on 2019-08-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('address', models.CharField(max_length=50, verbose_name='住所')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='緯度')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='軽度')),
            ],
            options={
                'verbose_name': '顧客',
                'verbose_name_plural': '顧客',
            },
        ),
    ]