from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from mainapp.models import Blog,Category,Tag,Blog_images,Services,Portfolio,Portfolio_category,Message
# Register your models here.
# class MyModelAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': CKEditorWidget(config_name='default')},
#     }
#     exclude = ('content_without_ck','content','name','bottomcontent','sidename','sidecontent','bottomname')
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Blog_images)
admin.site.register(Services)
admin.site.register(Portfolio_category)
admin.site.register(Portfolio)
admin.site.register(Message)
