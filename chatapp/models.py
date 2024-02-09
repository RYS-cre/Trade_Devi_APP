from django.db import models

# Create your models here.
class ChatSession(models.Model):
  created = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
  session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
  text = models.TextField()
  sender = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)