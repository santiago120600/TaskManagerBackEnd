# Generated by Django 3.1.6 on 2021-09-09 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20210901_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img_task',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]