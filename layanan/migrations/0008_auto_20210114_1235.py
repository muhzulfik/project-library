# Generated by Django 2.2 on 2021-01-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0007_remove_catalog_kepengarangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='bahasa',
            field=models.CharField(choices=[('indonesia', 'Indonesia'), ('english', 'English')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='judul',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='keyword',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='penulis',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='journal',
            name='issn',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='journal',
            name='judul_artikel',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='journal',
            name='kata_kunci',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='journal',
            name='penulis',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
