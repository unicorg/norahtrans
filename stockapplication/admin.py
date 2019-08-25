from django.contrib import admin

# Register your models here.
from stockapplication.models import Stock, Bond, Investor
# Register your models here.
admin.site.register(Stock)
admin.site.register(Bond)
admin.site.register(Investor)
