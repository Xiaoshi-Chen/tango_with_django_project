# Register your models here.
from django.contrib import admin
from rango.models import Category, Page

## 在网页上创建 category and page
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')
admin.site.register(Page, PageAdmin)