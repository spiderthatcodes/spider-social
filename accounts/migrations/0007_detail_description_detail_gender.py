# Generated by Django 4.2.4 on 2023-09-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_detail_species'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=10, null=True),
        ),
    ]
