# Generated by Django 3.1.2 on 2020-10-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]