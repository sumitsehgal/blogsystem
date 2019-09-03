from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post, Comment
from django.db.models import Count


#Post Admin - Separate Admin
class PostAdminSite(AdminSite):
    site_header = "My Post Area"
    site_title = "My Post title"
    index_title = "Welcome to My Post area"
postadmin = PostAdminSite(name="post_admin")
postadmin.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "comment_count","is_published",)
    list_filter = ("ispublished",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _comment_count=Count("comment", distinct=True),
        )
        return queryset

    def comment_count(self, obj):
        return obj._comment_count

    def is_published(self, obj):
        return 'Published' if obj.ispublished else "Draft"

    comment_count.admin_order_field = '_comment_count'

#Main Admin
admin.site.register(Comment)

admin.site.unregister(User)
admin.site.unregister(Group)