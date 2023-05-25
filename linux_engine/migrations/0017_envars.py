# Generated by Django 3.2.18 on 2023-04-22 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investigations', '0001_initial'),
        ('linux_engine', '0016_sockstat_sourceport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COMM', models.TextField(null=True)),
                ('KEY', models.TextField(null=True)),
                ('PID', models.BigIntegerField(null=True)),
                ('PPID', models.BigIntegerField(null=True)),
                ('VALUE', models.TextField(null=True)),
                ('Tag', models.CharField(choices=[('Evidence', 'Evidence'), ('Suspicious', 'Suspicious')], max_length=11, null=True)),
                ('investigation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linux_envars_investigation', to='investigations.uploadinvestigation')),
            ],
        ),
    ]