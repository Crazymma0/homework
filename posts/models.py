from django.db import models


class Hashtag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Post(models.Model):
    preview = models.ImageField(upload_to='post_previews', blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rate = models.FloatField(default=5)

    """ references """
    hashtags = models.ManyToManyField(Hashtag, related_name="posts")

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


""" DATE_FIELD = YYYY-MM-DD """
""" DATETIME_FIELD = YYYY-MM-DD HH:mm:ss:ms """