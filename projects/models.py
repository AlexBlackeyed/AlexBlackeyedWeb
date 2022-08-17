from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

FLARES_CHOICES = [
    ('Django','Django'),
    ('Python','Python'),
    ('HTML','HTML'),
    ('CSS','CSS'),
    ('TailwindCSS','TailwindCSS'),
    ('Javascript','Javascript'),
]
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    flare = MultiSelectField(choices=FLARES_CHOICES)
    github_link = models.CharField(max_length=350)