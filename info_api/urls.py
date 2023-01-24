from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import views

#Need to redo end points

urlpatterns = [
    #path('accounts/', views.AccountList.as_view()),
    #path('accounts/<str:username>/', views.AccountDetail.as_view()),

    #resume CRUD points
    path('resume/', views.UserResumeList.as_view()),
    path('resume/<str:title>', views.UserResumeDetailCRUD.as_view()),

    #project CRUD points
    path('project/', views.UserProjectList.as_view()),
    path('project/<str:project_name>', views.UserProjectDetailCRUD.as_view()),

    #education CRUD points
    path('education/', views.UserEducationList.as_view()),
    path('education/<str:institution_name>', views.UserEducationDetailCRUD.as_view()),

    #professional CRUD points
    path('professional/', views.UserProfessionalList.as_view()),
    path('professional/<str:employer_name>', views.UserProfessionalDetailCRUD.as_view()),

    #end point for [AllowAny] to view the profile and resume filter
    path('profile/<str:email>/', views.ProfileView.as_view()),
    path('profile/<str:email>/<str:title>', views.ProfileResumeView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)