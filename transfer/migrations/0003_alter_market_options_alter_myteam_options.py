# Generated by Django 4.0.6 on 2022-08-11 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0002_market_skills_myteam_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='market',
            options={'ordering': ['position', '-skills']},
        ),
        migrations.AlterModelOptions(
            name='myteam',
            options={'ordering': ['position', '-skills']},
        ),
    ]
