# Generated by Django 2.1.5 on 2019-04-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_auto_20190405_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='Lable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
