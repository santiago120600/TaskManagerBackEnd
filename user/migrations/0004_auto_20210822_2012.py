# Generated by Django 3.1.6 on 2021-08-23 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210820_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_task',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='user.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='user.folder'),
        ),
        migrations.AlterField(
            model_name='task',
            name='img_task',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.user'),
        ),
    ]
