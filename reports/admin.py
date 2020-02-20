from django.contrib import admin
from .models import Report,ProblemReporting

#admin site start here

admin.site.register(Report)
admin.site.register(ProblemReporting)
