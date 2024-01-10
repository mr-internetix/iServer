from django.contrib import admin

from . import models


# registering models for iDataGenerator
admin.site.register(models.Tbluserdata)
admin.site.register(models.Version)
admin.site.register(models.Tblcortex)
admin.site.register(models.AvgTime)


# registering models for iQtabs

admin.site.register(models.iQTabs_Version)
admin.site.register(models.Tblexecutionlogs)
admin.site.register(models.Password)
admin.site.register(models.iQTabs_Tblusagedata)
