from django.contrib import admin

# Register your models here.
from imark.models import Set, Img, Note

admin.site.register(Set)
admin.site.register(Img)
admin.site.register(Note)