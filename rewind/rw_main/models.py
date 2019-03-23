from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    overview = models.TextField()
    poster_img = models.TextField()
    genre_id = models.TextField()
    release_date = models.TextField()
    
    # def __str__(self):
    #     return self.title