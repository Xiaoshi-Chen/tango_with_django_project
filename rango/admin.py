# Register your models here.
from django.contrib import admin
from rango.models import Category, Page

## 在网页上创建 category and page
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interface
admin.site.register(Page, PageAdmin)