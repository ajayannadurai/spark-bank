from django.contrib import admin

from .models import account
from .models import history

admin.site.register(account)
admin.site.register(history)