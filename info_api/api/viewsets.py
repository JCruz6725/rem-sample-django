from info_api.models import *
from  .serializers import *
from rest_framework import viewsets, authentication, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


'''
class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
'''



'''
class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProfessionalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
'''
