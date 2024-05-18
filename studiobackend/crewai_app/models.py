from django.db import models
from django.contrib.auth.models import User

class CrewAIInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_text = models.TextField()
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
