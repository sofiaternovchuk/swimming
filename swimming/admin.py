from django.contrib import admin
from .models import AboutMe, Staff, Classmate, Review

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_display_links = ('name',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone')

@admin.register(Classmate)
class ClassmateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('author', 'content')

from .models import PageContent

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'category', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('page_name', 'title', 'content')