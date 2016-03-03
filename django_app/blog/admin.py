from django.contrib import admin

from .models import Post,User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','description']

    class Meta:
        model = Post


class UserAdmin(admin.ModelAdmin):
    list_display=['user_name','title']
    fields=('user_name','title')

    class Meta:
        model = User


admin.site.register(Post,PostAdmin)
admin.site.register(User,UserAdmin)
