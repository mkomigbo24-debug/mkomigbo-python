from django.shortcuts import render
from datetime import date, timedelta
import math

MARKET_DAYS = ['Eke', 'Orie', 'Afo', 'Nkwo']
MARKET_MEANING = {
    'Eke': 'Creation, East, beginnings - Chi creation',
    'Orie': 'Work, West, trade - community market',
    'Afo': 'Rest, North, community - ancestral rest',
    'Nkwo': 'Spirit, South, ancestors - spiritual',
}
IGBO_MONTHS = ['Onwa Mbu (1st)', 'Onwa Abua (2nd)', 'Onwa Ato (3rd)', 'Onwa Ano (4th)', 'Onwa Ise (5th)', 'Onwa Isii (6th)', 'Onwa Asaa (7th)', 'Onwa Asato (8th)', 'Onwa Iteghete (9th)', 'Onwa Iri (10th)', 'Onwa Iri na Otu (11th)', 'Onwa Iri na Abua (12th)', 'Onwa Iri na Ato (13th)']
MOON_PHASES = ['New Moon - Onwa Ohuru', 'Waxing Crescent', 'First Quarter', 'Waxing Gibbous', 'Full Moon - Onwa Okirikiri', 'Waning Gibbous', 'Last Quarter', 'Waning Crescent']

def get_market_day(d):
    ref = date(2024, 1, 1)
    delta = (d - ref).days % 4
    return MARKET_DAYS[(MARKET_DAYS.index('Afo') + delta) % 4]

def get_moon_phase(d):
    # Simple: known new moon 2024-01-11
    ref = date(2024, 1, 11)
    days = (d - ref).days % 29.53
    idx = int((days / 29.53) * 8) % 8
    return MOON_PHASES[idx], days

def get_tide(d):
    phase_name, age = get_moon_phase(d)
    if 'New Moon' in phase_name or 'Full Moon' in phase_name:
        return f"Spring Tide - High {age:.1f} days after new - 2.1m high"
    else:
        return f"Neap Tide - {phase_name} - 1.2m"

def calendar_view(request):
    today = date.today()
    market_today = get_market_day(today)
    moon_name, moon_age = get_moon_phase(today)
    tide_today = get_tide(today)

    month_num = (today.month - 1) % 13
    igbo_month = IGBO_MONTHS[month_num]

    # Next 28 days with rich facts
    month = []
    for i in range(28):
        d = today + timedelta(days=i)
        m = get_market_day(d)
        moon, age = get_moon_phase(d)
        tide = get_tide(d)
        month.append({
            'date': d,
            'market': m,
            'is_today': d==today,
            'moon': moon,
            'tide': tide,
            'fact': f"{m} day - {MARKET_MEANING[m][:30]}",
            'igbo_month': IGBO_MONTHS[(d.month-1)%13],
        })

    context = {
        'title': 'Amuzhi Calendar',
        'today': today,
        'market_today': market_today,
        'market_meaning': MARKET_MEANING[market_today],
        'market_days': MARKET_DAYS,
        'market_meaning_all': MARKET_MEANING,
        'month': month,
        'igbo_month': igbo_month,
        'moon_name': moon_name,
        'moon_age': round(moon_age,1),
        'tide_today': tide_today,
        'daily_fact': f"Today {today.strftime('%A')} is {market_today} - {MARKET_MEANING[market_today]} - Moon: {moon_name} - Tide: {tide_today}",
        'public_note': 'PUBLIC APP - Igbo 4-day week + Moon + Tide',
    }
    return render(request, 'amuzhi_calendar/index.html', context)

def today_view(request):
    return calendar_view(request)

def convert_view(request, day, month, year):
    try:
        d = date(year, month, day)
        m = get_market_day(d)
        moon, _ = get_moon_phase(d)
        tide = get_tide(d)
        context = {'date': d, 'market': m, 'meaning': MARKET_MEANING[m], 'moon': moon, 'tide': tide, 'igbo_month': IGBO_MONTHS[(d.month-1)%13]}
    except Exception as e:
        context = {'error': str(e)}
    return render(request, 'amuzhi_calendar/convert.html', context)
