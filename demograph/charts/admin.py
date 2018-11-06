from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import IncomeLevel, EducationLevel, Gender, IncomeData, County, State

admin.site.register(IncomeLevel)
admin.site.register(EducationLevel)
admin.site.register(Gender)
admin.site.register(IncomeData)
admin.site.register(County)
admin.site.register(State)




