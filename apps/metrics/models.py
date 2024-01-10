from django.db import models


######################################### Models For iDataGenerator #################################################

class AvgTime(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_sid = models.CharField(db_column='PROJECT_SID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avg_time = models.FloatField(db_column='AVG_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVG_TIME'


class Version(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    program_name = models.CharField(db_column='Program Name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    version = models.FloatField(db_column='Version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Version'


class Tblcortex(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    question = models.TextField(db_column='Question')  # Field name made lowercase.
    options = models.TextField(db_column='Options')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblCortex'



class Tbluserdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    project_sid = models.CharField(db_column='PROJECT_SID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    average_time = models.CharField(db_column='AVERAGE_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_links = models.TextField(db_column='NUMBER_OF_LINKS', blank=True, null=True)  # Field name made lowercase.
    date_time_stamp = models.DateTimeField(db_column='DATE_TIME_STAMP', blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    length_of_interview = models.CharField(db_column='LENGTH_OF_INTERVIEW', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUserData'

    

######################################### Models For iQTabs #################################################

class iQTabs_Version(models.Model):
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


class iQTabs_Tblusagedata(models.Model):
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

