from django.shortcuts import render
from datetime import date, timedelta

MARKET_DAYS = ['Eke','Orie','Afo','Nkwo']
MARKET_MEANING = {
    'Eke': 'Creation, East, beginnings - Chi',
    'Orie': 'Work, West, trade',
    'Afo': 'Rest, North, community',
    'Nkwo': 'Spirit, South, ancestors',
}

IGBO_MONTHS_AUTH = [
    {'igbo': 'Ọnwa Mbụ', 'greg': 'Feb–Mar', 'meaning': 'Igbo New Year, Igu Aro festival, Nri calendar year counting, 1013th year recorded', 'festival': 'Igu Aro - Nkwo day 3rd week Feb', 'audio': 'onwa_mbu.mp3', 'pronunciation': 'O-nwa Mbu'},
    {'igbo': 'Ọnwa Abụọ', 'greg': 'Mar–Apr', 'meaning': 'Cleaning and farming month, preparation', 'festival': 'Cleaning, farm clearing', 'audio': 'onwa_abuo.mp3', 'pronunciation': 'O-nwa Abuo'},
    {'igbo': 'Ọnwa Ife Eke', 'greg': 'Apr–May', 'meaning': 'Fasting period Ugani - hunger period, sacrificial harmony to Ani Earth goddess, Ikenga wrestling', 'festival': 'Ugani fasting, wrestling for Ikenga', 'audio': 'onwa_ife_eke.mp3', 'pronunciation': 'O-nwa Ife Eke'},
    {'igbo': 'Ọnwa Anọ', 'greg': 'May–Jun', 'meaning': 'Planting seed yams, Ekeleke dance festival - optimism, belief in God', 'festival': 'Ekeleke dance, yam planting', 'audio': 'onwa_ano.mp3', 'pronunciation': 'O-nwa Ano'},
    {'igbo': 'Ọnwa Agwụ', 'greg': 'Jun–Jul', 'meaning': 'Traditional start of year, adult masquerades Igochi na mmanwu, Alusi Agwu venerated by Dibia priests', 'festival': 'Agwu veneration, masquerades', 'audio': 'onwa_agwu.mp3', 'pronunciation': 'O-nwa Agwu'},
    {'igbo': 'Ọnwa Ifejiọkụ', 'greg': 'Jul–Aug', 'meaning': 'Dedicated to yam deity Ifejioku and Njoku Ji, yam rituals for New Yam Festival', 'festival': 'New Yam Festival rituals', 'audio': 'onwa_ifejioku.mp3', 'pronunciation': 'O-nwa Ifejioku'},
    {'igbo': 'Ọnwa Alọm Chi', 'greg': 'Aug–early Sep', 'meaning': 'Yam harvesting, prayer and meditation for women, Alom Chi shrine for ancestors, venerating mothers and motherhood, August meeting', 'festival': 'August meeting, Alom Chi', 'audio': 'onwa_alom_chi.mp3', 'pronunciation': 'O-nwa Alom Chi'},
    {'igbo': 'Ọnwa Ilọ Mmụọ', 'greg': 'Late Sep', 'meaning': 'Eighth Month festival Onwa Asato, spiritual return', 'festival': 'Onwa Asato festival', 'audio': 'onwa_ilo_mmuo.mp3', 'pronunciation': 'O-nwa Ilo Mmuo'},
    {'igbo': 'Ọnwa Ana', 'greg': 'Oct', 'meaning': 'Ana/Ala earth goddess rituals commence, named after her', 'festival': 'Ana rituals', 'audio': 'onwa_ana.mp3', 'pronunciation': 'O-nwa Ana'},
    {'igbo': 'Ọnwa Okike', 'greg': 'Early Nov', 'meaning': 'Okike ritual takes place', 'festival': 'Okike ritual', 'audio': 'onwa_okike.mp3', 'pronunciation': 'O-nwa Okike'},
    {'igbo': 'Ọnwa Ajana', 'greg': 'Late Nov', 'meaning': 'Okike ritual continues', 'festival': 'Okike continuation', 'audio': 'onwa_ajana.mp3', 'pronunciation': 'O-nwa Ajana'},
    {'igbo': 'Ọnwa Ede Ajana', 'greg': 'Late Nov–Dec', 'meaning': 'Ritual Ends', 'festival': 'End of Okike', 'audio': 'onwa_ede_ajana.mp3', 'pronunciation': 'O-nwa Ede Ajana'},
    {'igbo': 'Ọnwa Ụzọ Alụsị', 'greg': 'Jan–early Feb', 'meaning': 'Last month, offering to the Alusi, intercalary month added every few years to align lunar with seasonal', 'festival': 'Alusi offerings, intercalary adjustment'},
]

MOON_EMOJI = {
    'New Moon': '🌑',
    'Waxing Crescent': '🌒',
    'First Quarter': '🌓',
    'Waxing Gibbous': '🌔',
    'Full Moon': '🌕',
    'Waning Gibbous': '🌖',
    'Last Quarter': '🌗',
    'Waning Crescent': '🌘',
    'Ọnwa Ohuru': '🌑',
    'Ọnwa Okirikiri': '🌕',
}

MOON_PHASES = ['New Moon - Ọnwa Ohuru','Waxing Crescent','First Quarter','Waxing Gibbous','Full Moon - Ọnwa Okirikiri','Waning Gibbous','Last Quarter','Waning Crescent']

def ordinal(n):
    if 10 <= n % 100 <= 20:
        return f"{n}th"
    return f"{n}{ {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"

def get_market_day(d):
    ref = date(2024,1,1)
    return MARKET_DAYS[(MARKET_DAYS.index('Afo') + (d-ref).days) % 4]

def get_moon_phase(d):
    ref = date(2024,1,11)
    days = (d-ref).days % 29.53
    idx = int((days/29.53)*8) % 8
    return MOON_PHASES[idx], days

def get_moon_emoji(phase_name):
    for k,v in MOON_EMOJI.items():
        if k in phase_name:
            return v
    return '🌙'

def get_tide(d):
    name, age = get_moon_phase(d)
    if 'New Moon' in name or 'Full Moon' in name:
        return f"Spring Tide 2.1m - {age:.1f}d"
    return f"Neap Tide 1.2m - {name[:15]}"

def calendar_view(request):
    today = date.today()
    market_today = get_market_day(today)
    moon_name, moon_age = get_moon_phase(today)
    tide_today = get_tide(today)
    month_idx = 0
    if today.month==3 or (today.month==4 and today.day<15): month_idx=1
    elif today.month==4 or (today.month==5 and today.day<15): month_idx=2
    elif today.month==5 or (today.month==6 and today.day<15): month_idx=3
    elif today.month==6 or (today.month==7 and today.day<15): month_idx=4
    elif today.month==7 or (today.month==8 and today.day<10): month_idx=5
    elif today.month==8 or (today.month==9 and today.day<10): month_idx=6
    elif today.month==9: month_idx=7
    elif today.month==10: month_idx=8
    elif today.month==11 and today.day<15: month_idx=9
    elif today.month==11: month_idx=10
    elif today.month==12: month_idx=11
    elif today.month==1: month_idx=12
    igbo_month_current = {**IGBO_MONTHS_AUTH[month_idx], 'ordinal': ordinal(month_idx+1), 'num': month_idx+1}
    month=[]
    for i in range(28):
        d = today+timedelta(days=i)
        moon_n,_ = get_moon_phase(d)
        month.append({'date':d,'market':get_market_day(d),'is_today':d==today,'moon':moon_n,'moon_emoji':get_moon_emoji(moon_n),'tide':get_tide(d)})
    return render(request,'amuzhi_calendar/index.html',{
        'title':'Amuzhi Calendar',
        'today':today,
        'market_today':market_today,
        'market_meaning':MARKET_MEANING[market_today],
        'market_meaning_all':MARKET_MEANING,
        'month':month,
        'igbo_month':igbo_month_current,
        'igbo_months_all':IGBO_MONTHS_AUTH,
        'moon_name':moon_name,
        'moon_age':round(moon_age,1),
        'moon_emoji':get_moon_emoji(moon_name),
        'tide_today':tide_today,
        'daily_fact':f"Today {today} is {market_today} - {igbo_month_current['igbo']} ({igbo_month_current['ordinal']})",
        'public_note':'PUBLIC APP - Authentic 13-month Onwa with audio + moon',
    })

def today_view(request):
    return calendar_view(request)

def year_view(request, year):
    months=[]
    for idx, m in enumerate(IGBO_MONTHS_AUTH):
        try:
            d=date(year,(idx+1)%12+1,21)
            months.append({'igbo':m['igbo'],'greg':m['greg'],'meaning':m['meaning'],'festival':m['festival'],'date':d,'market':get_market_day(d),'ordinal':ordinal(idx+1),'num':idx+1})
        except:
            months.append({'igbo':m['igbo'],'greg':m['greg'],'meaning':m['meaning'],'festival':m['festival'],'date':date(year,1,1),'market':'Eke','ordinal':ordinal(idx+1),'num':idx+1})
    return render(request,'amuzhi_calendar/year.html',{'year':year,'months':months,'title':f'Amuzhi {year} - 13 Onwa'})

def month_view(request, year, month):
    days=[]
    for i in range(31):
        try:
            dd=date(year,month,1)+timedelta(days=i)
            if dd.month!=month: break
            days.append({'date':dd,'market':get_market_day(dd)})
        except: break
    igbo_m = {**IGBO_MONTHS_AUTH[(month-1)%13], 'ordinal': ordinal((month-1)%13+1)} if month<=13 else {**IGBO_MONTHS_AUTH[0], 'ordinal': ordinal(1)}
    return render(request,'amuzhi_calendar/month.html',{'year':year,'month':month,'days':days,'igbo_month':igbo_m,'title':f"{igbo_m['igbo']} {year}"})

def convert_view(request, day, month, year):
    try:
        d=date(year,month,day)
        m=get_market_day(d)
        moon,_=get_moon_phase(d)
        igbo_m = {**IGBO_MONTHS_AUTH[(month-1)%13], 'ordinal': ordinal((month-1)%13+1)}
        return render(request,'amuzhi_calendar/convert.html',{'date':d,'market':m,'meaning':MARKET_MEANING[m],'moon':moon,'moon_emoji':get_moon_emoji(moon),'tide':get_tide(d),'igbo_month':igbo_m})
    except Exception as e:
        return render(request,'amuzhi_calendar/convert.html',{'error':str(e)})
