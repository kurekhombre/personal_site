# Generated by Django 4.1.1 on 2022-09-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Technologies'},
        ),
        migrations.AddField(
            model_name='technology',
            name='alt_text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
