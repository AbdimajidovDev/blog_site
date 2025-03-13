from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):

    STATUC_CHOISE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(verbose_name='Title', max_length=200)
    slug = models.SlugField(verbose_name='Slug', max_length=200, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField(verbose_name='Body')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(verbose_name='Status', max_length=10, choices=STATUC_CHOISE, default='draft')

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title


    objects = models.Manager()
    published = PublishedManager()

    # def get_absolute_url(self):
    #     return reverse("")

posts = Post.objects.all()
p_post = Post.published.all()