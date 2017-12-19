from django.contrib import admin
from onlineExam.models import ExerCategory, ExerContent, ImportFile
from .utils import import_user

# Register your models here.


class ImportFileAdmin(admin.ModelAdmin):

    list_display = ('file','linkExerCategory',)
    list_filter = ['file',]

    def save_model(self, request, obj, form, change):

        re = super(ImportFileAdmin, self).save_model(request, obj, form, change)
        import_user(self, request, obj, change)
        return re


class ExerCategoryAdmin(admin.ModelAdmin):
    pass


class ExerContentAdmin(admin.ModelAdmin):

    list_display = ('title', 'option', 'style', 'linkExerCategory',)
    list_filter = ['style', 'linkExerCategory']


admin.site.register(ExerContent, ExerContentAdmin)
admin.site.register(ExerCategory, ExerCategoryAdmin)
admin.site.register(ImportFile, ImportFileAdmin)
