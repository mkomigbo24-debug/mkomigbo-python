from django.shortcuts import render, get_object_or_404
from .models import Podcast, Episode

def podcast_list(request):
    podcasts = Podcast.objects.filter(is_published=True)
    return render(request,'podcast/list.html',{'podcasts':podcasts})

def episode_list(request, podcast_slug):
    podcast = get_object_or_404(Podcast, slug=podcast_slug)
    episodes = podcast.episodes.filter(is_published=True)
    return render(request,'podcast/episodes.html',{'podcast':podcast,'episodes':episodes})

def episode_detail(request, podcast_slug, episode_slug):
    podcast = get_object_or_404(Podcast, slug=podcast_slug)
    episode = get_object_or_404(Episode, podcast=podcast, slug=episode_slug)
    return render(request,'podcast/episode.html',{'podcast':podcast,'episode':episode})
