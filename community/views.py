
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Post, Comment, Vote, CreatorProfile

def community_home(request):
    posts = Post.objects.all().order_by('-is_hot_topic','-created_at')[:50]
    hot = Post.objects.filter(is_hot_topic=True)[:6]
    return render(request, 'community/home.html', {'posts': posts, 'hot': hot})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    Post.objects.filter(id=post.id).update(views=F('views')+1)
    if request.method == 'POST' and request.user.is_authenticated:
        Comment.objects.create(post=post, author=request.user, body=request.POST.get('body','')[:1000])
        return redirect('community_detail', slug=slug)
    return render(request, 'community/detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title','')[:200]
        body = request.POST.get('body','')[:5000]
        p_type = request.POST.get('post_type','blog')
        subject_name = request.POST.get('subject_name','')[:100]
        is_hot = request.POST.get('is_hot_topic') == 'on'
        if title and body:
            post = Post.objects.create(author=request.user, title=title, body=body, post_type=p_type, subject_name=subject_name, is_hot_topic=is_hot)
            CreatorProfile.objects.get_or_create(user=request.user)
            return redirect('community_detail', slug=post.slug)
    return render(request, 'community/create.html')

@login_required
def post_vote(request, slug):
    post = get_object_or_404(Post, slug=slug)
    vote, created = Vote.objects.get_or_create(post=post, user=request.user, defaults={'value':1})
    if not created:
        vote.delete()
        Post.objects.filter(id=post.id).update(likes=F('likes')-1)
    else:
        Post.objects.filter(id=post.id).update(likes=F('likes')+1)
        profile, _ = CreatorProfile.objects.get_or_create(user=post.author)
        from django.db.models import F as F2
        CreatorProfile.objects.filter(id=profile.id).update(wallet_balance_usd=F2('wallet_balance_usd')+0.01, total_views=F2('total_views')+1)
        Post.objects.filter(id=post.id).update(revenue_usd=F2('revenue_usd')+0.01)
    return redirect('community_detail', slug=slug)

def leaderboard(request):
    creators = CreatorProfile.objects.order_by('-wallet_balance_usd')[:20]
    return render(request, 'community/leaderboard.html', {'creators': creators})
