from django.contrib import admin
from django.contrib.auth.models import Group
from .models import (
    Department,
    Employee,
    Laptop
)

# register Profile
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Laptop)

admin.site.site_header = 'Bakertilly Asset Tracker'
admin.site.site_title = 'Bakertilly Asset Tracker'
admin.site.index_title = 'Admin'

# the reference: https://stackoverflow.com/questions/13229235/django-admin-page-removing-group
admin.site.unregister(Group)
