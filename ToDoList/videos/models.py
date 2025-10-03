from django.db import models

class Video(models.Model):
    youtube_url = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.youtube_url
