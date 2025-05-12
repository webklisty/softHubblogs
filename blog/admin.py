from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'created_at', 'updated_at', 'image_preview']
    list_filter = ['published', 'created_at', 'updated_at', 'categories']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'created_at'
    list_editable = ['published']
    filter_horizontal = ['categories']
    readonly_fields = ['image_preview']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'excerpt')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Featured Image', {
            'fields': ('featured_image', 'image_preview'),
            'classes': ('collapse',),
        }),
        ('Publication', {
            'fields': ('published', 'categories')
        }),
    )
