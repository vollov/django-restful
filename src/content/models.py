from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        db_table = 'pages'