from django.contrib import admin
from .models import *
from .models import Search

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Search)