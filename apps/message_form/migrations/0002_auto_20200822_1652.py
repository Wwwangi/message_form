# Generated by Django 2.2 on 2020-08-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='id',
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='姓名'),
        ),
    ]
