from django.contrib import admin
from .models import Work, About, Tag, Contact

# Register your models here.

admin.site.register(Work)
admin.site.register(About)
admin.site.register(Tag)
admin.site.register(Contact)
