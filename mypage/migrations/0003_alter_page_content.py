# Generated by Django 3.2.18 on 2023-05-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]