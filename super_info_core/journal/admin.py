from django.contrib import admin
from journal.models import Publication, Category, AboutMe
from ckeditor.widgets import CKEditorWidget



@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['descrption']

