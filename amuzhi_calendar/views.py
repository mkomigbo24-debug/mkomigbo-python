from django.shortcuts import render

def calendar_view(request):
    """Amuzhi Calendar - Igbo 4-day market calendar - PUBLIC"""
    context = {
        'title': 'Amuzhi Calendar - Igbo Market Days',
        'market_days': ['Eke', 'Orie', 'Afo', 'Nkwo'],
        'description': 'Traditional Igbo 4-day week calendar - public app - easily accessible',
    }
    return render(request, 'amuzhi_calendar/index.html', context)

def today_view(request):
    from datetime import date
    context = {'today': date.today(), 'market_day': 'Eke'}
    return render(request, 'amuzhi_calendar/today.html', context)

def convert_view(request, day, month, year):
    context = {'day': day, 'month': month, 'year': year}
    return render(request, 'amuzhi_calendar/convert.html', context)
