from django.shortcuts import render

def weekly_guide(request):
    """AWAG - Africa Weekly Guide - PUBLIC"""
    context = {
        'title': 'AWAG - Africa Weekly Guide',
        'description': 'Weekly guide for Africa - public app - easily accessible to all',
    }
    return render(request, 'africa_weekly/index.html', context)

def week_view(request, year, week):
    context = {'year': year, 'week': week}
    return render(request, 'africa_weekly/week.html', context)

def today_guide(request):
    from datetime import date
    context = {'today': date.today()}
    return render(request, 'africa_weekly/today.html', context)
