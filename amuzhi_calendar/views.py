from django.shortcuts import render
from datetime import date, timedelta, datetime

MARKET_DAYS = ['Eke','Orie','Afo','Nkwo']
MARKET_MEANING = {
    'Eke': 'Creation, East, beginnings - Chi',
    'Orie': 'Work, West, trade',
    'Afo': 'Rest, North, community',
    'Nkwo': 'Spirit, South, ancestors',
}

IGBO_MONTHS_AUTH = [
    {'igbo': 'Ọnwa Mbụ', 'greg': 'Feb–Mar', 'meaning': 'Igbo New Year, Igu Aro festival, Nri calendar year counting, 1013th year recorded', 'festival': 'Igu Aro - Nkwo day 3rd week Feb', 'audio': 'onwa_mbu.mp3', 'pronunciation': 'O-nwa Mbu', 'ordinal': '1st'},
    {'igbo': 'Ọnwa Abụọ', 'greg': 'Mar–Apr', 'meaning': 'Cleaning and farming month, preparation', 'festival': 'Cleaning, farm clearing', 'audio': 'onwa_abuo.mp3', 'pronunciation': 'O-nwa Abuo', 'ordinal': '2nd'},
    {'igbo': 'Ọnwa Ife Eke', 'greg': 'Apr–May', 'meaning': 'Fasting period Ugani - hunger period, sacrificial harmony to Ani Earth goddess, Ikenga wrestling', 'festival': 'Ugani fasting, wrestling', 'audio': 'onwa_ife_eke.mp3', 'pronunciation': 'O-nwa Ife Eke', 'ordinal': '3rd'},
    {'igbo': 'Ọnwa Anọ', 'greg': 'May–Jun', 'meaning': 'Planting seed yams, Ekeleke dance festival - optimism, belief in God', 'festival': 'Ekeleke dance, yam planting', 'audio': 'onwa_ano.mp3', 'pronunciation': 'O-nwa Ano', 'ordinal': '4th'},
    {'igbo': 'Ọnwa Agwụ', 'greg': 'Jun–Jul', 'meaning': 'Traditional start of year, adult masquerades Igochi na mmanwu, Alusi Agwu venerated', 'festival': 'Agwu veneration', 'audio': 'onwa_agwu.mp3', 'pronunciation': 'O-nwa Agwu', 'ordinal': '5th'},
    {'igbo': 'Ọnwa Ifejiọkụ', 'greg': 'Jul–Aug', 'meaning': 'Dedicated to yam deity Ifejioku and Njoku Ji, yam rituals for New Yam Festival', 'festival': 'New Yam rituals', 'audio': 'onwa_ifejioku.mp3', 'pronunciation': 'O-nwa Ifejioku', 'ordinal': '6th'},
    {'igbo': 'Ọnwa Alọm Chi', 'greg': 'Aug–early Sep', 'meaning': 'Yam harvesting, prayer for women, Alom Chi shrine for ancestors, mothers', 'festival': 'August meeting', 'audio': 'onwa_alom_chi.mp3', 'pronunciation': 'O-nwa Alom Chi', 'ordinal': '7th'},
    {'igbo': 'Ọnwa Ilọ Mmụọ', 'greg': 'Late Sep', 'meaning': 'Eighth Month festival Onwa Asato, spiritual return', 'festival': 'Onwa Asato', 'audio': 'onwa_ilo_mmuo.mp3', 'pronunciation': 'O-nwa Ilo Mmuo', 'ordinal': '8th'},
    {'igbo': 'Ọnwa Ana', 'greg': 'Oct', 'meaning': 'Ana/Ala earth goddess rituals commence', 'festival': 'Ana rituals', 'audio': 'onwa_ana.mp3', 'pronunciation': 'O-nwa Ana', 'ordinal': '9th'},
    {'igbo': 'Ọnwa Okike', 'greg': 'Early Nov', 'meaning': 'Okike ritual takes place', 'festival': 'Okike ritual', 'audio': 'onwa_okike.mp3', 'pronunciation': 'O-nwa Okike', 'ordinal': '10th'},
    {'igbo': 'Ọnwa Ajana', 'greg': 'Late Nov', 'meaning': 'Okike ritual continues', 'festival': 'Okike continuation', 'audio': 'onwa_ajana.mp3', 'pronunciation': 'O-nwa Ajana', 'ordinal': '11th'},
    {'igbo': 'Ọnwa Ede Ajana', 'greg': 'Late Nov–Dec', 'meaning': 'Ritual Ends', 'festival': 'End of Okike', 'audio': 'onwa_ede_ajana.mp3', 'pronunciation': 'O-nwa Ede Ajana', 'ordinal': '12th'},
    {'igbo': 'Ọnwa Ụzọ Alụsị', 'greg': 'Jan–early Feb', 'meaning': 'Last month, offering to the Alusi, intercalary month added every few years', 'festival': 'Alusi offering', 'audio': 'onwa_uzo_alusi.mp3', 'pronunciation': 'O-nwa Uzo Alusi', 'ordinal': '13th'},
]

# SCIENTIFIC MOON - educative - real vs human eye
MOON_SCIENCE = {
    'New Moon': {'emoji':'🌑','igbo':'Ọnwa Ọhụrụ - Anya Anaghị Ahụ','visible':'0% illuminated - hemisphere in shadow','real_vs_eye':'Astronomical New: Moon between Earth & Sun, invisible. Human eye first crescent appears 1-2 days later as Waxing Crescent!','science':'Conjunction: Sun-Moon-Earth aligned. Far side lit, near side dark. Not visible.','igbo_meaning':'New cycle, Ani renewal, planting intentions'},
    'Waxing Crescent': {'emoji':'🌒','igbo':'Ọnwa Na-Eto Obere','visible':'1-49% - small sliver right side','real_vs_eye':'First visible to human eye! People call this New, but real New was 1-2 days before!','science':'Moon moving from Sun, Waxing=growing.','igbo_meaning':'Hope rising, first light'},
    'First Quarter': {'emoji':'🌓','igbo':'Ọnwa Ọkara Mbụ','visible':'50% - half moon right lit','real_vs_eye':'Half visible, 7.4 days after New','science':'Moon 90° from Sun. Neap tide low.','igbo_meaning':'Decision time, action'},
    'Waxing Gibbous': {'emoji':'🌔','igbo':'Ọnwa Na-Eto Ukwuu','visible':'51-99% - almost full','real_vs_eye':'Gibbous=humpback, growing to full','science':'More than half lit, shadow shrinking.','igbo_meaning':'Preparation, building energy'},
    'Full Moon': {'emoji':'🌕','igbo':'Ọnwa Oju','visible':'100% - fully lit face','real_vs_eye':'Real Full vs eye: appears full 1 day before/after peak!','science':'Opposition: Earth between Sun & Moon. Spring tide 2.5m.','igbo_meaning':'Full power, harvest, Agwu active'},
    'Waning Gibbous': {'emoji':'🌖','igbo':'Ọnwa Na-Ada Ukwuu','visible':'99-51% - decreasing','real_vs_eye':'Waning=shrinking after full','science':'Shadow growing from right.','igbo_meaning':'Gratitude, sharing'},
    'Last Quarter': {'emoji':'🌗','igbo':'Ọnwa Ọkara Ikpeazụ','visible':'50% - left side lit','real_vs_eye':'Third Quarter, half visible again','science':'Moon 270° from Sun.','igbo_meaning':'Release, forgiveness, cleansing'},
    'Waning Crescent': {'emoji':'🌘','igbo':'Ọnwa Na-Ada Obere - Ikpeazụ Anya','visible':'49-1% - thin sliver left, disappearing','real_vs_eye':'Last visible to eye! Real Last (shadow hemisphere) invisible 1-2 days AFTER this! Eye last ≠ real last!','science':'Final visible phase before invisible New Moon conjunction.','igbo_meaning':'Rest, reflection, ancestors wisdom'},
}

def get_moon_phase(target_date):
    if isinstance(target_date, datetime):
        target_date = target_date.date()
    known_new = date(2024, 1, 11)
    diff = (target_date - known_new).days
    lunar = 29.53058867
    phase_days = diff % lunar
    if phase_days < 1.5: key='New Moon'
    elif phase_days < 7.0: key='Waxing Crescent'
    elif phase_days < 8.5: key='First Quarter'
    elif phase_days < 14.0: key='Waxing Gibbous'
    elif phase_days < 16.0: key='Full Moon'
    elif phase_days < 21.5: key='Waning Gibbous'
    elif phase_days < 23.0: key='Last Quarter'
    else: key='Waning Crescent'
    return key, phase_days

def get_moon_detail(target_date):
    name, age = get_moon_phase(target_date)
    d = MOON_SCIENCE[name]
    return {
        'phase': name,
        'age': age,
        'emoji': d['emoji'],
        'igbo': d['igbo'],
        'visible': d['visible'],
        'real_vs_eye': d['real_vs_eye'],
        'science': d['science'],
        'igbo_meaning': d['igbo_meaning'],
        'moon_emoji': d['emoji'],
        'moon_phase': name,
        'moon_igbo': d['igbo'],
        'moon_visible': d['visible'],
        'moon_real_vs_eye': d['real_vs_eye'],
        'moon_science': d['science'],
        'moon_name': name,
    }

def get_market_day(target_date):
    ref = date(2024, 1, 1) # Eke
    diff = (target_date - ref).days
    idx = diff % 4
    return MARKET_DAYS[idx], MARKET_MEANING[MARKET_DAYS[idx]]

def calendar_view(request):
    today = date.today()
    market_today, market_meaning = get_market_day(today)
    moon_name, moon_age = get_moon_phase(today)
    moon_detail = get_moon_detail(today)
    month_num = (today.month - 2) % 13 # Feb=0
    igbo_month = IGBO_MONTHS_AUTH[month_num]

    # Next 28 days with scientific moon
    month_data = []
    for i in range(28):
        d = today + timedelta(days=i)
        m_day, _ = get_market_day(d)
        md = get_moon_detail(d)
        month_data.append({
            'date': d,
            'market': m_day,
            'is_today': d==today,
            'moon_emoji': md['emoji'],
            'moon_phase': md['phase'],
            'moon_igbo': md['igbo'],
            'moon_visible': md['visible'],
            'moon_real_vs_eye': md['real_vs_eye'],
            'moon_science': md['science'],
            'moon_meaning': md['igbo_meaning'],
        })

    context = {
        'title': 'Amuzhi Calendar',
        'today': today,
        'market_today': market_today,
        'market_meaning': market_meaning,
        'igbo_month': igbo_month,
        'igbo_months_all': IGBO_MONTHS_AUTH,
        'moon_name': moon_name,
        'moon_age': moon_age,
        'moon_emoji': moon_detail['emoji'],
        'moon_detail': moon_detail,
        'tide_today': 'Neap Tide 1.2m - First Quarter' if 'Quarter' in moon_name else 'Spring Tide 2.5m' if 'Full' in moon_name or 'New' in moon_name else 'Moderate Tide',
        'month': month_data,
    }
    return render(request, 'amuzhi_calendar/index.html', context)

def today_view(request):
    return calendar_view(request)

def year_view(request, year):
    return render(request, 'amuzhi_calendar/year.html', {'year': year, 'igbo_months': IGBO_MONTHS_AUTH})

def month_view(request, year, month):
    return render(request, 'amuzhi_calendar/month.html', {'year': year, 'month': month})

def convert_view(request, day, month, year):
    d = date(year, month, day)
    market, meaning = get_market_day(d)
    moon = get_moon_detail(d)
    return render(request, 'amuzhi_calendar/convert.html', {'date': d, 'market': market, 'meaning': meaning, 'moon': moon})

def market_calculator_view(request):
    result = None
    if request.method == 'POST':
        try:
            d = int(request.POST.get('day'))
            m = int(request.POST.get('month'))
            y = int(request.POST.get('year'))
            target = date(y, m, d)
            market, meaning = get_market_day(target)
            result = {'date': target, 'market': market, 'meaning': meaning}
        except Exception as e:
            result = {'error': str(e)}
    return render(request, 'amuzhi_calendar/calculator.html', {'result': result})

def quiz_view(request):
    return render(request, 'amuzhi_calendar/quiz.html', {'months': IGBO_MONTHS_AUTH})

def festival_view(request):
    return render(request, 'amuzhi_calendar/festival.html', {'months': IGBO_MONTHS_AUTH})
