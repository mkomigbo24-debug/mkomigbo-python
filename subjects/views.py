from django.shortcuts import render
from .models import Subject, Page, Script

def home(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/home.html', {'subjects': subjects})

def subjects_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})

def subject_detail(request, slug):
    subject = Subject.objects.get(slug=slug)
    pages = subject.pages.all()
    return render(request, 'subjects/detail.html', {'subject': subject, 'pages': pages})

def page_detail(request, subject_slug, page_slug):
    subject = Subject.objects.get(slug=subject_slug)
    page = Page.objects.get(subject=subject, slug=page_slug)
    return render(request, 'subjects/page.html', {'subject': subject, 'page': page})

def script_detail(request, slug):
    return render(request, 'subjects/scripts.html', {'slug': slug})

def ndebe_49(request):
    return render(request, 'subjects/ndebe_49.html')

def ndebe_glyphs(request):
    return render(request, 'subjects/ndebe_glyphs.html')  # H effect - 49 glyphs hover

def h_effect(request):
    return render(request, 'subjects/h_effect.html')

def h_effect_comprehensive(request):
    return render(request, 'subjects/h_effect_final.html')