from django.contrib import admin
from .models import Articles
from .models import Library

admin.site.register(Articles)
admin.site.register(Library)
