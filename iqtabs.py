# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Version(models.Model):
    program_name = models.CharField(db_column='PROGRAM NAME', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.FloatField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Version'


class Password(models.Model):
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'password'


class Tblexecutionlogs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    project_sid = models.CharField(db_column='PROJECT_SID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tab_plan_type = models.CharField(db_column='TAB_PLAN_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    log_type = models.CharField(db_column='LOG_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    log_description = models.TextField(db_column='LOG_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    date_time_stamp = models.DateTimeField(db_column='DATE_TIME_STAMP', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExecutionLogs'


class Tblusagedata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dsc_job_number = models.CharField(db_column='DSC_JOB_NUMBER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tab_plan_type = models.CharField(db_column='TAB_PLAN_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    budget_hours = models.FloatField(db_column='BUDGET_HOURS', blank=True, null=True)  # Field name made lowercase.
    execution_status = models.CharField(db_column='EXECUTION_STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_time_stamp = models.DateTimeField(db_column='DATE_TIME_STAMP', blank=True, null=True)  # Field name made lowercase.
    project_sid = models.CharField(db_column='PROJECT_SID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_warnings = models.IntegerField(db_column='TOTAL_WARNINGS', blank=True, null=True)  # Field name made lowercase.
    total_time_coding = models.FloatField(db_column='TOTAL_TIME_CODING', blank=True, null=True)  # Field name made lowercase.
    total_time_editing = models.FloatField(db_column='TOTAL_TIME_EDITING', blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUsageData'
