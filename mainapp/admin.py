from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from mainapp.models import Blog,Category,Tag,Services,Portfolio,Portfolio_category,Message

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget(config_name='default')},
    }
    # exclude = ('content_without_ck','content','name','bottomcontent','sidename','sidecontent','bottomname')
    
    
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog,MyModelAdmin)
admin.site.register(Services,MyModelAdmin)
admin.site.register(Portfolio_category)
admin.site.register(Portfolio,MyModelAdmin)
admin.site.register(Message)
