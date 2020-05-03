from django.contrib import admin
from first_app.models import Webpage, AccessRecord, Topic, User

# Register your models here.

admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(User)

