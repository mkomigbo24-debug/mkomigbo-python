from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.contrib.auth.decorators import login_required
from.models import Post, Comment, Vote, CreatorProfile

def community_home(request):
    post_type = request.GET.get('type')
    if post_type:
        posts = Post.objects.filter(post_type=post_type).order_by('-created_at')[:50]
    else:
        posts = Post.objects.all().order_by('-is_hot_topic','-created_at')[:50]
    hot = Post.objects.filter(is_hot_topic=True)[:6]
    wallet = None
    if request.user.is_authenticated:
        profile, _ = CreatorProfile.objects.get_or_create(user=request.user)
        wallet = profile
    return render(request, 'community/home.html', {'posts': posts, 'hot': hot, 'wallet': wallet, 'filter_type': post_type})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f'/accounts/login/?next=/community/{slug}/')
        Comment.objects.create(post=post, author=request.user, body=request.POST.get('body','')[:1000])
        return redirect('community_detail', slug=slug)
    rates = {'blog':0.001,'forum':0.001,'thread':0.002,'reel':0.003,'podcast':0.002,'poll':0.001,'news':0.002,'market':0.001,'job':0.001,'event':0.002}
    rate = rates.get(post.post_type, 0.001)
    Post.objects.filter(id=post.id).update(views=F('views')+1, revenue_usd=F('revenue_usd')+rate)
    profile, _ = CreatorProfile.objects.get_or_create(user=post.author)
    CreatorProfile.objects.filter(id=profile.id).update(wallet_balance_usd=F('wallet_balance_usd')+rate*0.6, total_views=F('total_views')+1)
    post.refresh_from_db()
    poll_options = []
    if post.post_type == 'poll':
        lines = [l.strip() for l in post.body.split('\n') if l.strip()][:6]
        poll_options = lines[1:] if len(lines)>1 else []
    return render(request, 'community/detail.html', {'post': post, 'poll_options': poll_options})

@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        body = request.POST.get('body','').strip()
        post_type = request.POST.get('post_type','thread')
        subject = request.POST.get('subject_name','')[:100]
        is_hot = bool(request.POST.get('is_hot_topic'))
        if title and body:
            Post.objects.create(title=title, body=body, post_type=post_type, subject_name=subject, is_hot_topic=is_hot, author=request.user)
            return redirect('/community/')
    return render(request, 'community/create.html')

def leaderboard(request):
    top = CreatorProfile.objects.order_by('-wallet_balance_usd')[:20]
    return render(request, 'community/leaderboard.html', {'top_creators': top})

@login_required(login_url='/accounts/login/')
def wallet(request):
    profile, _ = CreatorProfile.objects.get_or_create(user=request.user)
    my_posts = Post.objects.filter(author=request.user).order_by('-created_at')[:20]
    return render(request, 'community/wallet.html', {'wallet': profile, 'my_posts': my_posts})

def post_vote(request, slug):
    if not request.user.is_authenticated:
        return redirect(f'/accounts/login/?next=/community/{slug}/')
    post = get_object_or_404(Post, slug=slug)
    Vote.objects.get_or_create(post=post, user=request.user)
    return redirect('community_detail', slug=slug)

def poll_vote(request, slug, option):
    if not request.user.is_authenticated:
        return redirect(f'/accounts/login/?next=/community/{slug}/')
    post = get_object_or_404(Post, slug=slug)
    Vote.objects.get_or_create(post=post, user=request.user)
    return redirect('community_detail', slug=slug)

