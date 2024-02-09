from django.contrib import admin
from .models import post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# we can use decorators here for registration
# but we don't need to do it for now
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date' 
    empty_value_display = "-empty-"
    list_display = ('title', 'author', 'published_date','created_date' , 'status' , 'counted_view','login_required')
    list_filter = ('status',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)



class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ('name' , 'post' , 'subject','approved')
    list_filter = ('subject','approved')



# register the tables in ORM admin panel 
admin.site.register(post , PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)