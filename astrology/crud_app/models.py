from django.db import models

# Create your models here.
# astrology/models.py
from django.db import models

class Prediction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_predicted = models.DateField()

    def __str__(self):
        return self.title
