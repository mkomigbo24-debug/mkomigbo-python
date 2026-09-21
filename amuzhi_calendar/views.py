from django.shortcuts import render
from datetime import date

MARKET_DAYS = ['Eke', 'Orie', 'Afo', 'Nkwo']

def get_market_day(d):
    ref = date(2024, 1, 1) # Jan 1 2024 = Afo
    delta = (d - ref).days % 4
    idx = (MARKET_DAYS.index('Afo') + delta) % 4
    return MARKET_DAYS[idx]

def calendar_view(request):
    today = date.today()
    context = {
        'title': 'Amuzhi Calendar',
        'today': today,
        'market_today': get_market_day(today),
        'market_days': MARKET_DAYS,
        'public_note': 'PUBLIC APP - /amuzhi/ - Accessible to all - not hidden!',
    }
    return render(request, 'amuzhi_calendar/index.html', context)

def today_view(request):
    return calendar_view(request)

def convert_view(request, day, month, year):
    try:
        d = date(year, month, day)
        context = {'date': d, 'market': get_market_day(d)}
    except Exception as e:
        context = {'error': str(e)}
    return render(request, 'amuzhi_calendar/convert.html', context)
