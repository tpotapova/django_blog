from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','text')
    list_filter = ['pub_date']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)

