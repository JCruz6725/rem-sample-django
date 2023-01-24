from rest_framework import serializers 

from django.conf import settings as s

from django.contrib.auth import get_user_model
Account = get_user_model()

from info_api.models import Resume, Project, Education, Professional


#from info_api.models import Resume, Education, Project, Professional, Person
#from django.contrib.auth.models import User




class AccountSerializer (serializers.ModelSerializer):
    class Meta:
        model = Account
        #fields = ['email', 'full_name', 'location']


class ResumeSerializer (serializers.ModelSerializer):
    account_email = serializers.StringRelatedField() #serializers.CharField(source=("Account"), read_only=False)
    class Meta:
        model = Resume
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}}

class ProjectSerializer (serializers.ModelSerializer):
    account_email = serializers.StringRelatedField() #serializers.CharField(source=("Account.email"), read_only=False)
    resume_title = serializers.StringRelatedField()
    class Meta:
        model = Project
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}, 'resume_title':{'required': False} }


class EducationSerializer (serializers.ModelSerializer):
    account_email = serializers.StringRelatedField() #serializers.CharField(source=("user_email.email"))
    class Meta:
        model = Education
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}}

class ProfessionalSerializer (serializers.ModelSerializer):
    account_email = serializers.StringRelatedField() #CharField(source=("user_email.email"))
    resume_title = serializers.StringRelatedField()
    class Meta:
        model = Professional
        fields = "__all__"
        extra_kwargs = {'account_email': {'required': False}, 'resume_title':{'required': False} }

### Profile will be what is shown in the main section ###

class ProfileSerializer (serializers.ModelSerializer):
    resume = ResumeSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    project = ProjectSerializer(many=True, read_only=True)
    professional = ProfessionalSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['email', 'full_name', 'location', 'resume', 'professional', 'project', 'education']