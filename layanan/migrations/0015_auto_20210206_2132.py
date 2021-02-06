# Generated by Django 2.2 on 2021-02-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0014_auto_20210206_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='judul_artikel',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='judul_terbitan',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='journal',
            name='kata_kunci',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='judul',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='keyword',
            field=models.TextField(blank=True, null=True),
        ),
    ]
