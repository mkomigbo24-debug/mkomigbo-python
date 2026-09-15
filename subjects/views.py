from django.shortcuts import render, get_object_or_404
from .models import Subject, Page

def home(request):
    subjects = Subject.objects.all().order_by('nav_order')
    return render(request, 'subjects/home.html', {'subjects': subjects, 'present_count': subjects.count()})

def subjects_list(request):
    subjects = Subject.objects.all().order_by('nav_order')
    return render(request, 'subjects/list.html', {'subjects': subjects})

def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    pages = subject.pages.all().order_by('nav_order')
    return render(request, 'subjects/detail.html', {'subject': subject, 'pages': pages})

def page_detail(request, subject_slug, page_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    page = get_object_or_404(Page, subject=subject, slug=page_slug)
    return render(request, 'subjects/page.html', {'subject': subject, 'page': page})