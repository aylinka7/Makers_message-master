from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Subscriber
from .resources import SubscriberResource


@admin.register(Subscriber)
class SubscriberAdmin(ImportExportModelAdmin):
    resource_class = SubscriberResource