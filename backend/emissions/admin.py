from django.contrib import admin

# Register your models here.
from .models import DataSource, RawRecord

admin.site.register(DataSource)
admin.site.register(RawRecord)