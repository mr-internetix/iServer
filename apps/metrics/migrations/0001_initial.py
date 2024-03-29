# Generated by Django 4.2.8 on 2023-12-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbluserdata',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('project_sid', models.CharField(blank=True, db_column='PROJECT_SID', max_length=255, null=True)),
                ('average_time', models.CharField(blank=True, db_column='AVERAGE_TIME', max_length=255, null=True)),
                ('username', models.CharField(blank=True, db_column='USERNAME', max_length=255, null=True)),
                ('number_of_links', models.TextField(blank=True, db_column='NUMBER_OF_LINKS', null=True)),
                ('date_time_stamp', models.DateTimeField(blank=True, db_column='DATE_TIME_STAMP', null=True)),
                ('uuid', models.CharField(blank=True, db_column='UUID', max_length=255, null=True)),
                ('length_of_interview', models.CharField(blank=True, db_column='LENGTH_OF_INTERVIEW', max_length=255, null=True)),
                ('region', models.CharField(blank=True, db_column='REGION', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblUserData',
                'managed': False,
            },
        ),
    ]
