# Generated by Django 4.1.7 on 2023-04-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_kamarkost_gambar'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamarkost',
            name='namakost',
            field=models.CharField(max_length=50, null=True),
        ),
    ]