# subjects/views.py - List 21 subjects, 121 pages
from django.shortcuts import render, get_object_or_404
from .models import Subject, Page

def subject_list(request):
    subjects = Subject.objects.prefetch_related('pages').all().order_by('name')
    total_pages = Page.objects.count()
    return render(request, 'subjects/subject_list.html', {
        'subjects': subjects,
        'total_pages': total_pages,
        'total_subjects': subjects.count(),
    })

def subject_detail(request, subject_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    pages = subject.pages.filter(is_published=True).order_by('order')
    return render(request, 'subjects/subject_detail.html', {
        'subject': subject,
        'pages': pages,
    })

def page_detail(request, subject_slug, page_slug):
    subject = get_object_or_404(Subject, slug=subject_slug)
    page = get_object_or_404(Page, slug=page_slug, subject=subject)
    # Get next/prev
    pages = list(subject.pages.filter(is_published=True).order_by('order'))
    idx = pages.index(page) if page in pages else -1
    next_page = pages[idx+1] if idx >=0 and idx < len(pages)-1 else None
    prev_page = pages[idx-1] if idx > 0 else None
    return render(request, 'subjects/page_detail.html', {
        'subject': subject,
        'page': page,
        'next_page': next_page,
        'prev_page': prev_page,
    })