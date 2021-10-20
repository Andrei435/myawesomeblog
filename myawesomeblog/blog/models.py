from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=150)
    blog_date = models.DateTimeField(auto_now = False , auto_now_add = False)
    blog_text = models.TextField(blank=True)
    blog_image = models.ImageField(upload_to='event_image/')
