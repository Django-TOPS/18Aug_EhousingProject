from django.contrib import admin
from mywebsite.models import signup
from mywebsite.models import complain
from mywebsite.models import contact



# Register your models here.
admin.site.register(signup)
admin.site.register(complain)
admin.site.register(contact)



