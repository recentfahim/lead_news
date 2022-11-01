from django.db import models


class News(models.Model):
    source_id = models.CharField(max_length=128, null=True, blank=True)
    source_name = models.CharField(max_length=128, null=True, blank=True)
    author_name = models.CharField(max_length=128, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=255)
    image_url = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField()
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
        db_table = 'news'
        ordering = ['-published_at']
        unique_together = ['source_name', 'author_name', 'title', 'published_at']

    def __str__(self):
        return self.source_name + self.title
