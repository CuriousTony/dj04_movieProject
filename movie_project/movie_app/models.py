from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=30, blank=False)
    year = models.CharField(max_length=6, blank=False)
    genre = models.CharField(max_length=30, blank=False)
    intro = models.TextField(max_length=500, blank=False)
    poster = models.ImageField(upload_to='posters/', blank=False)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.name
