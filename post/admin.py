from django.contrib import admin
from post .models import Post,Category,Comment

# Register your models here.


admin.site.register(Post)
admin.site.register(Category)


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)