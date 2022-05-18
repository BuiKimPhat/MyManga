from tkinter import CASCADE
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Manga(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    thumbnail = models.URLField()
    status = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True)
    genres = models.ManyToManyField(Genre)
    views = models.PositiveIntegerField(default=0)
    chapters_number = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    modified_date = models.CharField(max_length=50)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {str(self.manga)}"

class Content(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField()
    link = models.URLField()

    def __str__(self):
        return f"Page {self.index} - {str(self.chapter)} - {self.link}"
