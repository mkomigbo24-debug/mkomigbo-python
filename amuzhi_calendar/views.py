from django.shortcuts import render
from datetime import date, timedelta

MARKET_DAYS = ['Eke', 'Orie', 'Afo', 'Nkwo']
MARKET_MEANING = {
    'Eke': 'Creation, market, first day - associated with East, beginnings',
    'Orie': 'Work, trade, second day - associated with West',
    'Afo': 'Rest, community, third day - associated with North',
    'Nkwo': 'Spirit, ancestors, fourth day - associated with South',
}

def get_market_day(d):
    ref = date(2024, 1, 1) # Jan 1 2024 = Afo
    delta = (d - ref).days % 4
    idx = (MARKET_DAYS.index('Afo') + delta) % 4
    return MARKET_DAYS[idx]

def calendar_view(request):
    today = date.today()
    market_today = get_market_day(today)
    # Next 28 days = 1 Igbo month (7 weeks x 4 days)
    month = []
    for i in range(28):
        d = today + timedelta(days=i)
        month.append({'date': d, 'market': get_market_day(d), 'is_today': d==today})

    context = {
        'title': 'Amuzhi Calendar',
        'today': today,
        'market_today': market_today,
        'market_meaning': MARKET_MEANING[market_today],
        'market_days': MARKET_DAYS,
        'market_meaning_all': MARKET_MEANING,
        'month': month,
        'izu': 7, # 7 market weeks = 28 days
        'public_note': 'PUBLIC APP - /amuzhi/ - Igbo 4-day week - not hidden!',
    }
    return render(request, 'amuzhi_calendar/index.html', context)

def today_view(request):
    return calendar_view(request)

def convert_view(request, day, month, year):
    try:
        d = date(year, month, day)
        market = get_market_day(d)
        context = {'date': d, 'market': market, 'meaning': MARKET_MEANING[market]}
    except Exception as e:
        context = {'error': str(e)}
    return render(request, 'amuzhi_calendar/convert.html', context)
