from django.shortcuts import render
from datetime import date, timedelta

REGIONS = ['Bight of Biafra', 'Sahel', 'Great Lakes', 'Horn', 'Southern']
FARMING_TIPS = [
    'Plant cassava early rains - Eke day best for planting',
    'Fish tides: Spring tide 2 days after new/full moon',
    'Market day Orie - best for selling produce',
]

def weekly_guide(request):
    today = date.today()
    week_num = today.isocalendar()[1]
    context = {
        'title': 'AWAG - Africa Weekly Guide',
        'today': today,
        'week': week_num,
        'year': today.year,
        'regions': REGIONS,
        'tides': {'high': '06:30 & 18:45', 'low': '12:15 & 00:30', 'spring': 'Sept 23'},
        'farming': FARMING_TIPS,
        'public_note': 'PUBLIC APP - /awag/ - Tides, Farming, Regions - Weekly thesis for Africa',
    }
    return render(request, 'africa_weekly/index.html', context)

def week_view(request, year, week):
    context = {'year': year, 'week': week, 'title': f'AWAG Week {week}'}
    return render(request, 'africa_weekly/week.html', context)

def today_guide(request):
    return weekly_guide(request)
