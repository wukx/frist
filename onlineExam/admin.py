from django.contrib import admin
from onlineExam.models import ExerCategory, ExerContent

# Register your models here.


class ExerCategoryAdmin(admin.ModelAdmin):
    pass


class ExerContentAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExerContent, ExerContentAdmin)
admin.site.register(ExerCategory, ExerCategoryAdmin)
