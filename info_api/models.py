from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
import uuid
# refer to DB ralation diagram for full explination


class AccountManager (BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")

        if not username:
            raise ValueError("username is required")

        new_account = self.model(
            email=self.normalize_email(email), username=username)
        new_account.set_password(password)
        new_account.save(using=self._db)
        return new_account

    def create_superuser(self, email, username, password=None):
        new_account = self.create_user(
            email, username=username, password=password)
        new_account.id = uuid.uuid4()
        new_account.is_admin = True
        new_account.is_superuser = True
        new_account.is_staff = True
        new_account.save(using=self._db)
        return new_account


class Account (AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=63, unique=True)
    full_name = models.CharField(max_length=63, unique=False)
    location = models.CharField(max_length=63, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # this is user for the login
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Resume (models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='resume',  on_delete=models.CASCADE)
    title = models.CharField(max_length=32, default='',
                             null=False, blank=False)
    summary = models.CharField(
        max_length=1024, default='', null=False, blank=False)
    # programming_skills = models.CharField(
    # max_length=1024, default='', null=False, blank=False)
    # industry_tools = models.CharField(
    # max_length=1024, default='', null=False, blank=False)
    # office_tools = models.CharField(
    # max_length=1024, default='', null=False, blank=False)
    # related_courses = models.CharField(
    # max_length=1024, default='', null=False, blank=False)

    def __str__(self):
        return self.title


class Project (models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='project', on_delete=models.CASCADE)
    resume_id = models.ForeignKey(
        Resume, related_name='project_rt', on_delete=models.CASCADE)
    project_name = models.CharField(
        max_length=32, default='', null=False, blank=False)
    title_on_project = models.CharField(
        max_length=32, default='', null=False, blank=False)
    tech_used = models.CharField(
        max_length=32, default='', null=False, blank=False)
    summary = models.CharField(
        max_length=1024, default='', null=False, blank=False)
    external_link = models.CharField(
        max_length=32, default='https://github.com/', null=False, blank=False)

    def __str__(self):
        return self.project_name


class Education (models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='education', on_delete=models.CASCADE)
    resume_id = models.ForeignKey(
        Resume, related_name='resume', on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=64, null=False, blank=False)
    degree = models.CharField(max_length=128, null=False, blank=False)
    time_at = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.institution_name


class Professional (models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='professional', on_delete=models.CASCADE)
    resume_id = models.ForeignKey(
        Resume, related_name='professional_rt', on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=32, null=False, blank=False)
    position = models.CharField(max_length=32, null=False, blank=False)
    time_at = models.CharField(max_length=32, null=False, blank=False)
    title_of_project = models.CharField(max_length=32, null=False, blank=False)
    tech_used = models.CharField(max_length=64, null=False, blank=False)
    summary = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return self.title_of_project
