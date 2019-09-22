from import_export import resources
from .models import Subscriber

class SubscriberResource(resources.ModelResource):
    class Meta:
        model = Subscriber
        exclude = ('date_birth', 'course_id')
        fields = ('name', 'surname', 'date_birth', 'number', 'e_mail', 'course_id')
        export_order = ('e_mail', 'number')
