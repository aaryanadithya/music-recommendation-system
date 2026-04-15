from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Song

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def search_songs(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mood = data.get('mood', '').lower()
        
        # Search songs by mood
        songs = Song.objects.filter(mood__icontains=mood)
        
        songs_list = [{
            'id': song.id,
            'title': song.title,
            'artist': song.artist,
            'mood': song.mood,
            'audio_url': song.audio_url if song.audio_url else song.audio_file.url if song.audio_file else None,
            'duration': song.duration
        } for song in songs]
        
        return JsonResponse({'songs': songs_list})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_all_songs(request):
    songs = Song.objects.all()
    songs_list = [{
        'id': song.id,
        'title': song.title,
        'artist': song.artist,
        'mood': song.mood,
        'audio_url': song.audio_url if song.audio_url else song.audio_file.url if song.audio_file else None,
        'duration': song.duration
    } for song in songs]
    
    return JsonResponse({'songs': songs_list})

