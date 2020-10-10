from django.shortcuts import render
from django.views.generic.dates import YearArchiveView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Jobs.models import Job
from .serializers import JobSerializer



class JobYearArchiveView(YearArchiveView):
    queryset = Job.objects.all()
    date_field = "expiry_date_time"
    make_object_list = True
    allow_future = True

class jobList(APIView):
    def get(self, request):
        job1 = Job.objects.all()
        serializer = JobSerializer(job1, many= True)
        return Response(serializer.data)
