from django.shortcuts import render
from tablib import Dataset
from .resources import SubscriberResource

def simple_upload(request):
    if request.method == 'POST':
        person_resource = SubscriberResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)

    return render(request, 'simple_upload.html')