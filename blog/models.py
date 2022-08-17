from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

FLARES2_CHOICES = (
    ("Politics", "Politics"),
    ("Tech", "Tech"),
    ("Programming", "Programming"),
    ("Python", "Python"),
    ("Django", "Django"),
    ("UI", "UI"),
    ("Reviews", "Reviews"),
    ("Opinions", "Opinions"),
    ("Rant", "Rant"),
    ("Uncategorized", "Uncategorized"),
    ("Random", "Random"),
)


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_description = models.CharField(max_length=150)
    post = models.TextField(max_length=1500)
    post_time = models.CharField(max_length=2)
    post_url_title = models.CharField(max_length=150)
    flare_choice = MultiSelectField(choices=FLARES2_CHOICES)