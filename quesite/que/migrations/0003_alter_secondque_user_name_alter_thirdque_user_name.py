# Generated by Django 4.0.1 on 2022-01-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('que', '0002_rename_user_1q_firstque_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondque',
            name='user_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='thirdque',
            name='user_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]