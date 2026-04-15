from django.db import models

class Song(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('energetic', 'Energetic'),
        ('calm', 'Calm'),
        ('romantic', 'Romantic'),
    ]
    
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    audio_url = models.URLField(blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    duration = models.IntegerField(help_text="Duration in seconds")
    
    def __str__(self):
        return f"{self.title} - {self.artist}"