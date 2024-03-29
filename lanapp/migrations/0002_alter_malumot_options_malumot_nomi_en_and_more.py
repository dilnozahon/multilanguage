# Generated by Django 4.0.4 on 2022-05-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='malumot',
            options={'verbose_name': 'Malumot', 'verbose_name_plural': 'Malumotlar'},
        ),
        migrations.AddField(
            model_name='malumot',
            name='nomi_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='malumot',
            name='nomi_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='malumot',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='malumot',
            name='text_uz',
            field=models.TextField(null=True),
        ),
    ]
