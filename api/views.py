# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv, io, os
from rest_framework import viewsets
from .models import Control
from .serializers import ControlSerializer
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# Creating view


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


# class view for controls
class ControlViewSet(BaseViewSet):
    serializer_class = ControlSerializer
    model = Control


# function view for exporting data into CSV format
def export_csv(request):
    model = Control
    items = model.objects.all()

    response = HttpResponse(content_type='text/csv')  # file type - csv
    response['Content-Disposition'] = 'attachment; filename="export.csv"'  # file name - export.csv

    writer = csv.writer(response, delimiter=',')  # separated by comma
    writer.writerow(['name', 'type', 'maximum_rabi_rate', 'polar_angle'])  # name of the column heading

    for obj in items:
        writer.writerow([obj.name, obj.type, obj.maximum_rabi_rate, obj.polar_angle])  # export data in a loop

    return response


# function view for importing data from CSV file
def import_csv(request):

        file_ = open(os.path.join(settings.BASE_DIR, 'export.csv'))

        print(file_.name)

        data_set = file_.read()  # .decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Control.objects.update_or_create(
                name=column[0],
                type=column[1],
                maximum_rabi_rate=column[2],
                polar_angle=column[3]
            )

        return HttpResponse('<h1>Success importing data!</h1>')

