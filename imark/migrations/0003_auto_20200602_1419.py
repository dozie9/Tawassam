# Generated by Django 3.0.6 on 2020-06-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imark', '0002_auto_20200602_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='images',
        ),
        migrations.AddField(
            model_name='set',
            name='images',
            field=models.ManyToManyField(related_name='set_imgs', to='imark.Img'),
        ),
    ]