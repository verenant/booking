from django.contrib import admin
from .models import Vehicle, PostImage

#admin.site.register(Vehicle)
# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Vehicle)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Vehicle

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass