# Generated by Django 4.0.6 on 2022-08-12 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0005_alter_myteam_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myteam',
            name='goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='myteam',
            name='skills',
            field=models.CharField(choices=[('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪🟪'), ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪🟪'), ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪🟪'), ('🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪', '🟩🟩🟥🟥🟫🟫🟦🟦🟦🟪'), ('🟩🟩🟥🟥🟫🟫🟦🟦🟦', '🟩🟩🟥🟥🟫🟫🟦🟦🟦'), ('🟩🟩🟥🟥🟫🟫🟦🟦', '🟩🟩🟥🟥🟫🟫🟦🟦'), ('🟩🟩🟥🟥🟫🟫🟦', '🟩🟩🟥🟥🟫🟫🟦'), ('🟩🟩🟥🟥🟫🟫', '🟩🟩🟥🟥🟫🟫'), ('🟩🟩🟥🟥🟫', '🟩🟩🟥🟥🟫'), ('🟩🟩🟥🟥', '🟩🟩🟥🟥'), ('🟩🟩🟥', '🟩🟩🟥'), ('🟩🟩', '🟩🟩')], default='💷', max_length=200),
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='league', to='transfer.myteam')),
            ],
        ),
    ]
