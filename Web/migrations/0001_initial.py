# Generated by Django 2.1.5 on 2019-04-05 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_Name', models.CharField(max_length=500)),
                ('File_Path', models.FileField(upload_to='static/Files')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=255)),
                ('Last_Name', models.CharField(max_length=255, null=True)),
                ('Email', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.User'),
        ),
    ]