# Generated by Django 3.1.6 on 2021-03-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing_code', '0002_auto_20210208_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='code',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
