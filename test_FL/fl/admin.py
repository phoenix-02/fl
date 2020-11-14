from django.contrib import admin
from . import models as m

admin.site.register(m.Project)
admin.site.register(m.CustomUser)
# Register your models here.
