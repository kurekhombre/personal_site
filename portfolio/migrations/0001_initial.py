# Generated by Django 4.1.1 on 2022-09-19 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=200)),
                ('github_link', models.URLField()),
                ('live_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('source', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project')),
            ],
        ),
    ]