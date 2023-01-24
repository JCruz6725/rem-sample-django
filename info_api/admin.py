from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



#from .models import Person, Resume, Education, Project, Professional, Account
from .models import Account, Resume, Project, Education, Professional



class AccountAdmin (BaseUserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin')
    search_fields = (['email'])
    
    #readonly_fields = ('data_joined', 'last_login')
    readonly_fields = ()

    list_filter = ()
    fieldsets = ()
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)


class ResumeAdmin(BaseUserAdmin):
    list_display = ('title', 'account_email')
    #search_fields = ('title')

    #need these if not then django will get ANGRY!
    ordering = ()
    readonly_fields = ()
    list_filter = ()
    fieldsets = ()
    filter_horizontal = ()

admin.site.register(Resume) #need to fix this, breaks when adding the admin part 

class ProjectAdmin(BaseUserAdmin):
    list_display = ('project_name', 'account_email')
    #search_fields = ('title')

    #need these if not then django will get ANGRY!
    ordering = ()
    readonly_fields = ()
    list_filter = ()
    fieldsets = ()
    filter_horizontal = ()

admin.site.register(Project)#need to fix this, breaks when adding the admin part 



#admin.site.register(Person)
#admin.site.register(Resume)
admin.site.register(Education)
#admin.site.register(Project)
admin.site.register(Professional)

