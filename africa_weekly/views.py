from django.shortcuts import render
from datetime import date

def weekly_guide(request):
    context = {
        'title': 'AWAG - Africa Weekly Guide',
        'today': date.today(),
        'public_note': 'PUBLIC APP - /awag/ - Accessible to all - Tides, Farming, Regions - not hidden!',
    }
    return render(request, 'africa_weekly/index.html', context)

def week_view(request, year, week):
    context = {'year': year, 'week': week}
    return render(request, 'africa_weekly/week.html', context)

def today_guide(request):
    return weekly_guide(request)
