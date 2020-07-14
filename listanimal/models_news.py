from django.db import models
from django.contrib.postgres.fields import ArrayField

class AnimalNews(models.Model,):
    url_news= models.URLField()
    description_news= models.TextField()
    heading= models.TextField()
    main_text = models.TextField(null=True)
    url_media = models.URLField(null=True)
    time_post = models.CharField(max_length=20)
    gallery_img = ArrayField(models.URLField(),blank=True)

    def __str__(self):
        return self.description_news