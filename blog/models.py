from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from djrichtextfield.models import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug  = models.SlugField(unique=True, max_length=255)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    ispublished = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title+' '+self.slug

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Posts' #Name for admin
        def __unicode__(self):
            return self.title



class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name