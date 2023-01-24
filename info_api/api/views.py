from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



#from .serializers import UserSerializer, ProjectSerializer
from info_api.api.serializers import (AccountSerializer, 
                                    ResumeSerializer, 
                                    ProjectSerializer, 
                                    EducationSerializer, 
                                    ProfessionalSerializer,
                                    ProfileSerializer )

from info_api.models import Resume, Project, Professional, Education
from django.conf import settings #for *settings.AUTH_USER_MODEL*
from django.contrib.auth import get_user_model
Account = get_user_model()




# update will not update the fk will need to implement this here to
# https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers


# Need to fix permisionss 
# Need to fix authenications


#delete this...?
'''
class AccountList(APIView):
    #permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

class AccountDetail(APIView):
    permission_classes = [AllowAny]
    #permission_classes = [IsAuthenticated]

    def get_object(self, username):
        try:
            return Account.objects.get(username=username)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        account = self.get_object(username)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
'''
##################################################
### For Current user to get/post/UPDATE/DELETE ###
##################################################

### User Resume
class UserResumeList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        resume = Resume.objects.filter(account_email=request.user)
        serializer = ResumeSerializer(resume, many=True)
        return Response(serializer.data)

    #CREATE
    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        resume = Resume.objects.create(account_email=account)
        serializer = ResumeSerializer(resume, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserResumeDetailCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    #READ
    def get(self, request, title, format=None):
        account = Account.objects.get(email=request.user)
        resume = Resume.objects.get(title=title, account_email=account)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data)

    #UPDATE
    def put(self, request, title, format=None):
        resume = Resume.objects.get(title=title)
        serializer = ResumeSerializer(resume, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    def delete(self, request, title, format=None):
        resume = Resume.objects.get(title=title)
        resume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### User Projects
class UserProjectList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        project = Project.objects.filter(account_email=request.user)
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
    
    #CREATE
    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        resume = Resume.objects.get(title=request.data['resume_title'])
        project = Project.objects.create(account_email=account, resume_title=resume)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProjectDetailCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    #READ
    def get(self, request, project_name,format=None):
        project = Project.objects.get(project_name=project_name, account_email=request.user)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    #UPDATE
    def put(self, request, project_name, format=None):
        project = Project.objects.get(project_name=project_name)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    def delete(self, request, project_name, format=None):
        project = Project.objects.get(project_name=project_name)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### User Education
class UserEducationList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        education = Education.objects.filter(account_email=request.user)
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)

    #CREATE
    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        education = Education.objects.create(account_email=account)
        serializer = EducationSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserEducationDetailCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    #READ
    def get(self, request, institution_name, format=None):
        account = Account.objects.get(email=request.user)
        education = Education.objects.get(institution_name=institution_name, account_email=account)
        serializer = EducationSerializer(education)
        return Response(serializer.data)

    #UPDATE
    def put(self, request, institution_name, format=None):
        education = Education.objects.get(project_name=project_name)
        serializer = ProjectSerializer(education, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    def delete(self, request, institution_name, format=None):
        education = Education.objects.get(institution_name=institution_name)
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


### User Professional 
class UserProfessionalList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, format=None):
        professional = Professional.objects.filter(account_email=request.user)
        serializer = ProfessionalSerializer(professional, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account = Account.objects.get(email=request.user)
        professional = Professional.objects.create(account_email=account)
        serializer = ProfessionalSerializer(professional, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, format=None):
        pass

class UserProfessionalDetailCRUD(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    #READ
    def get(self, request, employer_name, format=None):
        account = Account.objects.get(email=request.user)
        p = Professional.objects.get(employer_name=employer_name, account_email=request.user)
        serializer = ProfessionalSerializer(p)
        return Response(serializer.data)

    #UPDATE
    def put(self, request, employer_name, format=None):
        p = Professional.objects.get(employer_name=employer_name)
        serializer = ProfessionalSerializer(p, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE
    def delete(self, request, employer_name, format=None):
        p = Professional.objects.get(employer_name=employer_name)
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


######################################
### For any non authenticated user ###
######################################
class ProfileView(APIView):
    permission_classes = [AllowAny]

    def get_account_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, email, format=None):
        account = self.get_account_object(email)
        serializer = ProfileSerializer(account)
        return Response(serializer.data)

### Use this to filter between endpoints
class ProfileResumeView(APIView):
    permission_classes = [AllowAny]

    def get_account_object(self, email):
        try:
            return Account.objects.get(email=email)
        except Account.DoesNotExist:
            raise Http404

    def filter_by_resume(self, title, serializer):

        #filter Resume
        res_filter = 'No resume matching ' + title
        for r in range (0 , len(serializer.data['resume'])):
            if (serializer.data['resume'][r]['title'] == title ):
                res_filter = serializer.data['resume'][r]
        serializer.data['resume'].clear()
        serializer.data['resume'].append(res_filter)


        #filter Professional exp
        professional_filter = []
        for p in range (0 , len(serializer.data['professional'])):
            if (serializer.data['professional'][p]['resume_title'] == title ):
                professional_filter.append(serializer.data['professional'][p])
        serializer.data['professional'].clear()
        for p in professional_filter:
            serializer.data['professional'].append(p)


        #filter Project
        project_filter = []
        for p in range (0 , len(serializer.data['project'])):
            if (serializer.data['project'][p]['resume_title'] == title ):
                project_filter.append(serializer.data['project'][p])
        serializer.data['project'].clear()
        for p in project_filter:
            serializer.data['project'].append(p)


        return serializer

    def filter(self, string_catagory, string_filter):
        #filter Project
        c_filter = []
        for p in range (0 , len(serializer.data[string_catagory])):
            if (serializer.data[string_catagory][p]['resume_title'] == string_filter ):
                c_filter.append(serializer.data[string_catagory][p])
        serializer.data[string_catagory].clear()
        for p in c_filter:
            serializer.data[string_catagory].append(p)


        return serializer
        

    def get(self, request, email, title, format=None):
        account = self.get_account_object(email)
        serializer = ProfileSerializer(account)
        serializer = self.filter_by_resume(title, serializer)
        return Response(serializer.data)