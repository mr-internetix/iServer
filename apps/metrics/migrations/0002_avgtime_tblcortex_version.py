# Generated by Django 4.2.8 on 2023-12-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_sid', models.CharField(blank=True, db_column='PROJECT_SID', max_length=255, null=True)),
                ('uuid', models.CharField(blank=True, db_column='UUID', max_length=255, null=True)),
                ('avg_time', models.FloatField(blank=True, db_column='AVG_TIME', null=True)),
            ],
            options={
                'db_table': 'AVG_TIME',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblcortex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(db_column='Question')),
                ('options', models.TextField(db_column='Options')),
            ],
            options={
                'db_table': 'tblCortex',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(db_column='Program Name', max_length=50)),
                ('version', models.FloatField(blank=True, db_column='Version', null=True)),
            ],
            options={
                'db_table': 'Version',
                'managed': False,
            },
        ),
    ]