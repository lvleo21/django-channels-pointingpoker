# Generated by Django 4.1.7 on 2023-03-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_estimate_is_closed_estimate_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='close_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Dt. Fim'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='start_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Dt. Início'),
        ),
    ]
