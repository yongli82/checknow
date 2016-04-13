from django.contrib import admin

# Register your models here.
from models import *

admin.site.register(AlarmProduct)
admin.site.register(AlarmProductItem)
admin.site.register(AlarmOrder)
admin.site.register(AlarmBalance)
admin.site.register(AlarmTrigger)

