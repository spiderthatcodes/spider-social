# Generated by Django 4.2.4 on 2023-09-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='species',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
