from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.html import mark_safe


class Category(models.Model):
    """Blog post category model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:category_posts', args=[self.slug])


class Post(models.Model):
    """Blog post model"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    featured_image = models.ImageField(upload_to='blog/featured_images/%Y/%m/', blank=True, null=True,
                                      help_text="Optional featured image for the blog post")
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True,
                             help_text="A short excerpt or summary of the post. If left blank, the first 50 words will be used.")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate unique slug
            original_slug = slugify(self.title)
            queryset = Post.objects.all()
            if self.id:
                queryset = queryset.exclude(id=self.id)
            
            slug = original_slug
            num = 1
            while queryset.filter(slug=slug).exists():
                slug = f"{original_slug}-{num}"
                num += 1
            
            self.slug = slug
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
        
    def get_excerpt(self):
        """Return the excerpt or the first 50 words of content"""
        if self.excerpt:
            return self.excerpt
        return ' '.join(self.content.split()[:50]) + '...'
        
    def image_preview(self):
        """Display thumbnail in admin"""
        if self.featured_image:
            return mark_safe(f'<img src="{self.featured_image.url}" width="150" />')
        return mark_safe('<span style="color:#ccc">No Image</span>')
    
    image_preview.short_description = 'Featured Image'
