from django.shortcuts import render, get_object_or_404
from.models import AmuzhiYear, AmuzhiMonth, MarketDay, MONTH_REGISTRY, MARKET_CYCLE, days_in_igbo_month, igbo_year_start_new_moon, moon_phase_info, is_gregorian_leap_year
from datetime import date, timedelta
from django.http import Http404

def get_today():
    today = MarketDay.objects.filter(is_today=True).first()
    if not today:
        today = MarketDay.objects.filter(date_gregorian=date.today()).first()
        if today:
            MarketDay.objects.update(is_today=False)
            today.is_today = True
            today.save()
    if not today:
        today = MarketDay.objects.filter(date_gregorian__gte=date.today()).first()
    return today

def generate_year_on_fly(greg_year):
    """Ad infinitum - generate any year past/future without DB pre-population - for decades planning, centuries records"""
    is_leap = is_gregorian_leap_year(greg_year)
    start = igbo_year_start_new_moon(greg_year)

    # Try get from DB, if not, create in memory structure for template
    y_obj, created = AmuzhiYear.objects.get_or_create(
        gregorian_year=greg_year,
        defaults={
            'igbo_year': greg_year,
            'is_leap': is_leap,
            'year_start_gregorian': start,
            'anchor_market_day': 'Afo'
        }
    )

    # If newly created or no months, build months and days
    if created or y_obj.months.count() == 0:
        current = start
        market_idx = MARKET_CYCLE.index('Afo')
        for m in range(1, 14):
            days = days_in_igbo_month(m, is_leap)
            reg = MONTH_REGISTRY[m]
            end = current + timedelta(days=days-1)
            month_obj, _ = AmuzhiMonth.objects.get_or_create(
                year=y_obj, number=m,
                defaults={
                    'name_igbo': reg['name'], 'gloss': reg['gloss'], 'theme': reg['theme'],
                    'days_in_month': days, 'gregorian_start': current, 'gregorian_end': end
                }
            )
            # Build days if not exist
            if month_obj.days.count() < days:
                for d in range(1, days+1):
                    moon = moon_phase_info(current)
                    md = MARKET_CYCLE[market_idx]
                    MarketDay.objects.get_or_create(
                        date_gregorian=current,
                        defaults={
                            'market_day': md[:4].upper(), 'igbo_day': d, 'month': month_obj,
                            'weekday': current.strftime('%A'), 'moon_symbol': moon['symbol'],
                            'moon_stage': moon['stage'], 'illumination': moon['illum']
                        }
                    )
                    current += timedelta(days=1)
                    market_idx = (market_idx + 1) % 4
            else:
                current += timedelta(days=days)
                market_idx = (market_idx + days) % 4
    else:
        # Year exists, ensure days exist
        if y_obj.months.count() > 0:
            total_days = sum([m.days.count() for m in y_obj.months.all()])
            if total_days == 0:
                # Rebuild
                current = start
                market_idx = MARKET_CYCLE.index('Afo')
                for month_obj in y_obj.months.order_by('number'):
                    days = month_obj.days_in_month
                    for d in range(1, days+1):
                        moon = moon_phase_info(current)
                        md = MARKET_CYCLE[market_idx]
                        MarketDay.objects.get_or_create(
                            date_gregorian=current,
                            defaults={
                                'market_day': md[:4].upper(), 'igbo_day': d, 'month': month_obj,
                                'weekday': current.strftime('%A'), 'moon_symbol': moon['symbol'],
                                'moon_stage': moon['stage'], 'illumination': moon['illum']
                            }
                        )
                        current += timedelta(days=1)
                        market_idx = (market_idx + 1) % 4

    return AmuzhiYear.objects.get(gregorian_year=greg_year)

def amuzhi_home(request):
    years = AmuzhiYear.objects.order_by('-gregorian_year')[:20] # Last 20
    today = get_today()
    # For ad infinitum navigation
    current_year = date.today().year
    year_range = list(range(current_year-5, current_year+6)) # 5 past, 5 future for quick jump
    return render(request, 'amuzhi_calendar/home.html', {
        'years': years,
        'today': today,
        'total_days': MarketDay.objects.count(),
        'year_range': year_range,
        'current_year': current_year,
        'all_years_range': list(range(1900, 2100)) # 1900-2100 for planning decades, centuries
    })

def amuzhi_year(request, year):
    # Ad infinitum - any year past or future
    if year < 1 or year > 9999:
        raise Http404("Year out of range - ad infinitum supports 1-9999")

    y = generate_year_on_fly(year)
    months = y.months.order_by('number').prefetch_related('days')
    today = get_today()

    # Navigation for ad infinitum
    prev_year = year - 1
    next_year = year + 1

    return render(request, 'amuzhi_calendar/year.html', {
        'year': y,
        'months': months,
        'today': today,
        'prev_year': prev_year,
        'next_year': next_year,
        'is_ad_infinitum': True
    })

def amuzhi_today(request):
    today = get_today()
    return render(request, 'amuzhi_calendar/today.html', {'today': today})

def amuzhi_search(request):
    """Search Eke or Afo day whether past or future - for planning"""
    query = request.GET.get('q', '')
    market = request.GET.get('market', '')
    year = request.GET.get('year', '')

    days = MarketDay.objects.all()
    if market:
        days = days.filter(market_day=market.upper())
    if year:
        try:
            y = int(year)
            # Generate year if not exist for search
            generate_year_on_fly(y)
            days = days.filter(month__year__gregorian_year=y)
        except:
            pass
    if query:
        days = days.filter(date_gregorian__icontains=query) | days.filter(month__name_igbo__icontains=query)

    days = days.order_by('date_gregorian')[:100]
    today = get_today()
    return render(request, 'amuzhi_calendar/search.html', {'days': days, 'query': query, 'today': today, 'market': market, 'year': year})