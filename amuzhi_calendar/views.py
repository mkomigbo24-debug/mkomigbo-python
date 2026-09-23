from django.shortcuts import render
from datetime import date, timedelta, datetime

MARKET_DAYS = ['Eke','Orie','Afo','Nkwo']
MARKET_MEANING = {
    'Eke': 'Creation, East, beginnings - Chi, day of creation, Nri royalty',
    'Orie': 'Work, West, trade, Oye - industriousness',
    'Afo': 'Rest, North, community, healing, herbs',
    'Nkwo': 'Spirit, South, ancestors, divination, Igu Aro new year',
}

# FULL AUTHENTIC IGBO MONTHS - 13 Onwa with Deity, Farming, Festival, Season, Spiritual
IGBO_MONTHS_AUTH = [
    {
        'igbo': 'Ọnwa Mbụ', 'english': 'First Moon - New Year', 'greg': 'Feb–Mar', 'ordinal': '1st',
        'pronunciation': 'O-nwa Mbu', 'audio': 'onwa_mbu.mp3',
        'meaning': 'Igbo New Year - Igu Aro festival marks 1013th+ year of Nri calendar. Counting from Eri migration.',
        'deity': 'Chukwu Abiama & Nri Ancestors', 'deity_desc': 'Supreme creator, Eri, Nri priest-kings. New year proclaimed by Eze Nri on Nkwo day 3rd week Feb.',
        'farming': 'Land clearing, burning, preparation for planting. Counting yam barns, seed yam selection.',
        'season': 'Dry to early rains - Harmattan ending, hot season.', 'festival': 'Igu Aro - Counting of Year',
        'festival_desc': 'Nkwo day, 3rd week February. Eze Nri proclaims new year after sighting new moon.',
        'spiritual': 'Renewal, divination for year, cleansing.', 'color': '#FFD700', 'emoji': '🌱',
    },
    {
        'igbo': 'Ọnwa Abụọ', 'english': 'Second Moon - Cleaning', 'greg': 'Mar–Apr', 'ordinal': '2nd',
        'pronunciation': 'O-nwa Abuo', 'audio': 'onwa_abuo.mp3',
        'meaning': 'Cleaning and farming preparation - Ihu Anwu, sweeping compounds, clearing bushes.',
        'deity': 'Ani / Ala - Earth Goddess', 'deity_desc': 'Ala the earth goddess, mother of fertility, morality.',
        'farming': 'Farm clearing, mound making, staking, composting. First rains.',
        'season': 'Early rainy season begins, thunderstorms.', 'festival': 'Ihu Anwu - Face of Sun Cleaning',
        'festival_desc': 'Communal cleaning of villages, shrines, streams.', 'spiritual': 'Purification, preparation for planting.',
        'color': '#8BC34A', 'emoji': '🧹',
    },
    {
        'igbo': 'Ọnwa Ife Eke', 'english': 'Third Moon - Hunger / Fasting', 'greg': 'Apr–May', 'ordinal': '3rd',
        'pronunciation': 'O-nwa Ife Eke', 'audio': 'onwa_ife_eke.mp3',
        'meaning': 'Ugani - hunger period, fasting. Last yams reserved, hunger teaches endurance.',
        'deity': 'Eke & Ikenga', 'deity_desc': 'Eke - python deity of creation, Ikenga - god of achievement, wrestling.',
        'farming': 'Hunger gap - old yams finished, new yams not ready. Planting cocoyam, beans.',
        'season': 'Peak hunger, heavy rains start.', 'festival': 'Ugani & Ikenga Wrestling',
        'festival_desc': 'Fasting, wrestling contests, Ikenga shrine purification.', 'spiritual': 'Sacrifice, endurance, humility.',
        'color': '#FF5722', 'emoji': '🙏',
    },
    {
        'igbo': 'Ọnwa Anọ', 'english': 'Fourth Moon - Planting', 'greg': 'May–Jun', 'ordinal': '4th',
        'pronunciation': 'O-nwa Ano', 'audio': 'onwa_ano.mp3',
        'meaning': 'Planting seed yams - Iba ji, optimism, Ekeleke dance celebrates faith.',
        'deity': 'Igwe & Amadioha', 'deity_desc': 'Sky god, thunder deity Amadioha for rain.',
        'farming': 'Planting seed yams - most important farm work! Planting in mounds with rituals.',
        'season': 'Heavy rains, thunder, lightning.', 'festival': 'Ekeleke Dance & Iba Ji',
        'festival_desc': 'Ekeleke masquerade - optimism, colorful, youth dance for bountiful harvest.',
        'spiritual': 'Hope, faith, optimism.', 'color': '#4CAF50', 'emoji': '🌧️',
    },
    {
        'igbo': 'Ọnwa Agwụ', 'english': 'Fifth Moon - Spirit of Knowledge', 'greg': 'Jun–Jul', 'ordinal': '5th',
        'pronunciation': 'O-nwa Agwu', 'audio': 'onwa_agwu.mp3',
        'meaning': 'Traditional start of year in some areas, Alusi Agwu venerated - god of health, divination.',
        'deity': 'Agwu - God of Divination & Healing', 'deity_desc': 'Agwu - patron of Dibia, knowledge, wisdom, mental healing.',
        'farming': 'Weeding, tending yams, staking.', 'season': 'Rainy season peak, floods, lush green.',
        'festival': 'Agwu & Igochi Mmanwu', 'festival_desc': 'Adult masquerades perform, Dibia initiation, healing rituals.',
        'spiritual': 'Knowledge, healing, divination.', 'color': '#9C27B0', 'emoji': '🔮',
    },
    {
        'igbo': 'Ọnwa Ifejiọkụ', 'english': 'Sixth Moon - Yam Deity', 'greg': 'Jul–Aug', 'ordinal': '6th',
        'pronunciation': 'O-nwa Ifejioku', 'audio': 'onwa_ifejioku.mp3',
        'meaning': 'Dedicated to Ifejioku and Njoku Ji - yam deity, king of crops.',
        'deity': 'Ifejioku / Njoku Ji', 'deity_desc': 'Yam god - Njoku Ji. Yams are sacred, have spirits.',
        'farming': 'Yam vines growing, tending, guarding from thieves. New yams forming.',
        'season': 'Heavy rains, yam leaves lush.', 'festival': 'Pre-Iri Ji - Yam Rituals',
        'festival_desc': 'Prayers to Ifejioku, first yams inspected.', 'spiritual': 'Gratitude for yams, discipline.',
        'color': '#795548', 'emoji': '🍠',
    },
    {
        'igbo': 'Ọnwa Alọm Chi', 'english': 'Seventh Moon - Women & Ancestors', 'greg': 'Aug–early Sep', 'ordinal': '7th',
        'pronunciation': 'O-nwa Alom Chi', 'audio': 'onwa_alom_chi.mp3',
        'meaning': 'Yam harvesting preparation, prayer for women, Alom Chi shrine for ancestors.',
        'deity': 'Alom Chi & Nne Chukwu', 'deity_desc': 'Goddess of women, fertility, motherhood, ancestral mothers.',
        'farming': 'Early yam harvest for rituals, women harvest cocoyam.', 'season': 'Late rainy, August break - short dry.',
        'festival': 'August Meeting & Alom Chi', 'festival_desc': 'Umuada return home, women prayer, community development.',
        'spiritual': 'Female power, motherhood, ancestry.', 'color': '#E91E63', 'emoji': '👩‍👧‍👧',
    },
    {
        'igbo': 'Ọnwa Ilọ Mmụọ', 'english': 'Eighth Moon - Return of Spirits', 'greg': 'Late Sep', 'ordinal': '8th',
        'pronunciation': 'O-nwa Ilo Mmuo', 'audio': 'onwa_ilo_mmuo.mp3',
        'meaning': 'Onwa Asato - Eighth Month festival, spiritual return, ancestors return.',
        'deity': 'Ndi Ichie & Mmuo', 'deity_desc': 'Ancestors, spirits return. Portal open between living and dead.',
        'farming': 'New Yam Festival Iri Ji - MAIN HARVEST! Yam harvest peak.', 'season': 'Rain ending, harvest begins.',
        'festival': 'Onwa Asato & Iri Ji', 'festival_desc': 'BIGGEST FESTIVAL! New Yam eaten first time after rituals.',
        'spiritual': 'Thanksgiving, harvest, ancestors communion.', 'color': '#FF9800', 'emoji': '🎉',
    },
    {
        'igbo': 'Ọnwa Ala', 'english': 'Ninth Moon - Earth Goddess', 'greg': 'Oct', 'ordinal': '9th',
        'pronunciation': 'O-nwa Ala', 'audio': 'onwa_ala.mp3',
        'meaning': 'Ana/Ala earth goddess rituals commence - serious morality, Ofo na Ogu.',
        'deity': 'Ala / Ana - Earth Goddess', 'deity_desc': 'Most powerful Alusi - Ala - mother earth, custodian of morality.',
        'farming': 'Yam harvest continues, storage in barns.', 'season': 'Dry season approaching, harvest abundance.',
        'festival': 'Ana/Ala Rituals & Ofo', 'festival_desc': 'Rituals of purification, morality, Ofo staff blessing.',
        'spiritual': 'Morality, truth, Ofo na Ogu - justice.', 'color': '#3E2723', 'emoji': '🌍',
    },
    {
        'igbo': 'Ọnwa Okike', 'english': 'Tenth Moon - Creation', 'greg': 'Early Nov', 'ordinal': '10th',
        'pronunciation': 'O-nwa Okike', 'audio': 'onwa_okike.mp3',
        'meaning': 'Okike ritual - creation, creativity, Chi creation, beginning of dry season mysteries.',
        'deity': 'Chi & Okike', 'deity_desc': 'Chi - personal god, creation spirit, destiny.',
        'farming': 'Harvest complete, barns full, dry season farming.', 'season': 'Dry season starts, Harmattan wind.',
        'festival': 'Okike Ritual', 'festival_desc': 'Creation rituals, Chi shrine renewal, personal destiny rites.',
        'spiritual': 'Creation, destiny, personal Chi.', 'color': '#00BCD4', 'emoji': '✨',
    },
    {
        'igbo': 'Ọnwa Ajala', 'english': 'Eleventh Moon - Travel & Morality', 'greg': 'Late Nov', 'ordinal': '11th',
        'pronunciation': 'O-nwa Ajala', 'audio': 'onwa_ajala.mp3',
        'meaning': 'Ajala Alusi - god of travel, crossroads, morality tales, conscience.',
        'deity': 'Ajala - Travel & Morality', 'deity_desc': 'Ajala - traveler, moral storyteller, tests humans.',
        'farming': 'Dry season, hunting, palm oil processing, crafts.', 'season': 'Dry, Harmattan, dusty, clear skies.',
        'festival': 'Ajala & Travel Rites', 'festival_desc': 'Travelers prayers, crossroads rituals, moral stories.',
        'spiritual': 'Journey, morality, conscience, life path.', 'color': '#607D8B', 'emoji': '🧭',
    },
    {
        'igbo': 'Ọnwa Ede Ajala', 'english': 'Twelfth Moon - Cocoyam & End', 'greg': 'Late Nov–Dec', 'ordinal': '12th',
        'pronunciation': 'O-nwa Ede Ajala', 'audio': 'onwa_ede_ajala.mp3',
        'meaning': 'Ede - cocoyam, end of cycle, Ritual Ends, preparation for last month offering.',
        'deity': 'Ede & Ajala', 'deity_desc': 'Cocoyam goddess, female crop, completes cycle with Ajala.',
        'farming': 'Cocoyam harvest, dry season crops, hunting.', 'season': 'Dry season peak, cold mornings.',
        'festival': 'End of Okike & Ede Harvest', 'festival_desc': 'Closing rituals, cocoyam feast, end of year preparations.',
        'spiritual': 'Completion, harvest of female crops.', 'color': '#8D6E63', 'emoji': '🍂',
    },
    {
        'igbo': 'Ọnwa Ụzọ Arụshị', 'english': 'Thirteenth Moon - Sacred Door to Gods', 'greg': 'Jan–early Feb', 'ordinal': '13th',
        'pronunciation': 'O-nwa Uzo Arushi', 'audio': 'onwa_uzo_arushi.mp3',
        'meaning': 'Last month, Ụzọ Arụshị - Door to Alusi, intercalary month added every 3 years to align 13x28=364 days.',
        'deity': 'Arụshị - All Alusi & Door', 'deity_desc': 'Ụzọ - Door/Path to all gods. All Alusi appeased.',
        'farming': 'Rest, repair barns, tools, counting year harvest.', 'season': 'Peak dry, hottest, bush burning.',
        'festival': 'Alusi Offering & Intercalary Adjustment', 'festival_desc': 'Offerings to all Alusi, door ritual, calendar adjusted.',
        'spiritual': 'Closure, offering to all spirits, doorway to new year.', 'color': '#212121', 'emoji': '🚪',
    },
]

# SCIENTIFIC MOON - BOSS OBSERVATION: 3-day Full + Pitch Darkness!
MOON_SCIENCE = {
    'Dark Night - Oji Ogbi': {
        'emoji':'⬛',
        'igbo':'Ọnwa Oji Ukwu - Abani - Pitch Darkness',
        'visible':'0% - NO MOON - pitch darkness, total black night!',
        'real_vs_eye':'YOUR OBSERVATION CONFIRMED! Between last crescent and first crescent - 1 night of total darkness! Visible only in SE Nigeria dry season clear sky, no light pollution! Igbo elders called this Oji Ogbi - Great Darkness!',
        'science':'Conjunction peak: Moon-Sun-Earth exact line, far side fully lit, near side 0%. No reflection. Light 0%.',
        'igbo_meaning':'Great void, ancestors passage, deep rest, Afa divination night, planning new cycle. Most spiritual night.'
    },
    'New Moon - Astronomical': {
        'emoji':'🌑',
        'igbo':'Ọnwa Ọhụrụ Astronomical - Anya Anaghị Ahụ',
        'visible':'0-2% - hemisphere in shadow, invisible',
        'real_vs_eye':'Astronomical New: Moon between Earth & Sun, invisible. Human eye cannot see yet. This is 1 day after pitch dark night!',
        'science':'Conjunction: Sun-Moon-Earth aligned. Far side lit, near side dark. Not visible. Age 0-1.5 days.',
        'igbo_meaning':'New cycle hidden, Ani renewal, planting intentions in dark'
    },
    'Waxing Crescent - First Tiny': {
        'emoji':'🌒✨',
        'igbo':'Ọnwa Ọhụrụ Mbụ Pụtara - Tiny First Sight',
        'visible':'1-3% - very tiny sliver right side, first visible after 3-day dark!',
        'real_vs_eye':'First visible to human eye after pitch dark night! People call this New, but real New was 2 days before + 1 pitch dark night!',
        'science':'Moon 12° from Sun, first crescent visible low on western horizon after sunset for ~30 mins.',
        'igbo_meaning':'Hope first appears after darkness, tiny light victory'
    },
    'Waxing Crescent': {
        'emoji':'🌒',
        'igbo':'Ọnwa Na-Eto Obere',
        'visible':'4-49% - small sliver right side growing',
        'real_vs_eye':'Growing crescent, easy to see. Still called New by many, but actually 3-7 days old!',
        'science':'Moon moving from Sun, Waxing=growing, illuminated % increasing.',
        'igbo_meaning':'Hope rising, first light building'
    },
    'First Quarter': {
        'emoji':'🌓',
        'igbo':'Ọnwa Ọkara Mbụ',
        'visible':'50% - half moon right lit',
        'real_vs_eye':'Half visible, 7.4 days after New. Clear half.',
        'science':'Moon 90° from Sun. Neap tide low.',
        'igbo_meaning':'Decision time, action, half way to full'
    },
    'Waxing Gibbous': {
        'emoji':'🌔',
        'igbo':'Ọnwa Na-Eto Ukwuu',
        'visible':'51-97% - almost full, humpback',
        'real_vs_eye':'Gibbous=humpback, growing to full. Looks almost full 1 day before!',
        'science':'More than half lit, shadow shrinking.',
        'igbo_meaning':'Preparation, building energy to peak'
    },
    'Full Moon - 3 Days': {
        'emoji':'🌕🌕🌕',
        'igbo':'Ọnwa Oju - 3 Days Full - Oju 3 Abali',
        'visible':'98-100% - 3 nights look FULL to human eye! 3-day full!',
        'real_vs_eye':'YOUR OBSERVATION CONFIRMED! Full lasts 3 days to eye! Day before 99%, day 100%, day after 99% - all look full! 3rd seeming full is actually first waning gibbous but eye cannot see 1% shadow! Science confirms - human eye cannot detect <2% change!',
        'science':'Opposition ±1 day still 98%+ illumination. Peak 100% is 1 instant, but 98-100% looks identical to eye. 3-day visual full.',
        'igbo_meaning':'Peak power 3 nights - harvest, masquerade, Agwu active 3 days, brightest, no darkness, spirits full active. Ike kachasị!'
    },
    'Waning Gibbous': {
        'emoji':'🌖',
        'igbo':'Ọnwa Na-Ada Ukwuu',
        'visible':'97-51% - decreasing after 3-day full',
        'real_vs_eye':'Waning=shrinking after 3-day full. First sign of shadow appears day 4.',
        'science':'Shadow growing from right, illumination dropping below 97% now visible.',
        'igbo_meaning':'Gratitude after peak, sharing harvest, beginning to wane'
    },
    'Last Quarter': {
        'emoji':'🌗',
        'igbo':'Ọnwa Ọkara Ikpeazụ',
        'visible':'50% - left side lit',
        'real_vs_eye':'Third Quarter, half visible again but left side.',
        'science':'Moon 270° from Sun.',
        'igbo_meaning':'Release, forgiveness, cleansing, half gone'
    },
    'Waning Crescent - Last Visible': {
        'emoji':'🌘',
        'igbo':'Ọnwa Na-Ada Obere - Ikpeazụ Anya',
        'visible':'49-5% - thin sliver left, disappearing',
        'real_vs_eye':'Last visible to eye! Will disappear tomorrow!',
        'science':'Final visible phase before fading.',
        'igbo_meaning':'Fading, ancestors calling, preparation for darkness'
    },
    'Waning Crescent - Fading to Dark': {
        'emoji':'🌘⬛',
        'igbo':'Ọnwa Na-Ala - Entering Darkness',
        'visible':'5-0.5% - extremely tiny sliver, fading to pitch dark',
        'real_vs_eye':'Last 2 days before pitch dark night! Very hard to see, only in clear SE Nigeria dry season! Tomorrow = total darkness Oji Ogbi!',
        'science':'Last crescent before conjunction, <5% illuminated, low on eastern horizon before sunrise.',
        'igbo_meaning':'Final light before void, entering Abani darkness, rest'
    },
}

# BOSS OBSERVATION IMPLEMENTATION: 3-day Full + 3-day Dark with Pitch Night
def get_moon_phase(target_date):
    if isinstance(target_date, datetime):
        target_date = target_date.date()
    known_new = date(2024, 1, 11)  # Known astronomical new moon
    diff = (target_date - known_new).days
    lunar = 29.53058867
    phase_days = diff % lunar

    # YOUR OBSERVATION: Full = 3 days visual, Dark = 3 days with 1 pitch dark night
    if phase_days < 0.75 or phase_days > 28.8:
        key = 'Dark Night - Oji Ogbi'  # 1.5 days total pitch darkness!
    elif phase_days < 1.5:
        key = 'New Moon - Astronomical'
    elif phase_days < 3.0:
        key = 'Waxing Crescent - First Tiny'
    elif phase_days < 6.5:
        key = 'Waxing Crescent'
    elif phase_days < 8.5:
        key = 'First Quarter'
    elif phase_days < 13.0:
        key = 'Waxing Gibbous'
    elif phase_days < 16.5:  # 3.5 days FULL to eye! Your observation!
        key = 'Full Moon - 3 Days'
    elif phase_days < 21.0:
        key = 'Waning Gibbous'
    elif phase_days < 23.5:
        key = 'Last Quarter'
    elif phase_days < 27.0:
        key = 'Waning Crescent - Last Visible'
    else:
        key = 'Waning Crescent - Fading to Dark'

    return key, phase_days

def get_moon_detail(target_date):
    name, age = get_moon_phase(target_date)
    d = MOON_SCIENCE.get(name, MOON_SCIENCE['Full Moon - 3 Days'])
    return {
        'phase': name, 'age': age, 'emoji': d['emoji'], 'igbo': d['igbo'],
        'visible': d['visible'], 'real_vs_eye': d['real_vs_eye'],
        'science': d['science'], 'igbo_meaning': d['igbo_meaning'],
        'moon_emoji': d['emoji'], 'moon_phase': name, 'moon_igbo': d['igbo'],
        'moon_visible': d['visible'], 'moon_real_vs_eye': d['real_vs_eye'],
        'moon_science': d['science'], 'moon_name': name,
    }

def get_market_day(target_date):
    ref = date(2024, 1, 1)  # Eke
    diff = (target_date - ref).days
    idx = diff % 4
    return MARKET_DAYS[idx], MARKET_MEANING[MARKET_DAYS[idx]]

def calendar_view(request):
    today = date.today()
    market_today, market_meaning = get_market_day(today)
    moon_name, moon_age = get_moon_phase(today)
    moon_detail = get_moon_detail(today)
    month_num = (today.month - 2) % 13
    igbo_month = IGBO_MONTHS_AUTH[month_num]
    month_data = []
    for i in range(28):
        d = today + timedelta(days=i)
        m_day, _ = get_market_day(d)
        md = get_moon_detail(d)
        month_data.append({
            'date': d, 'market': m_day, 'is_today': d==today,
            'moon_emoji': md['emoji'], 'moon_phase': md['phase'],
            'moon_igbo': md['igbo'], 'moon_visible': md['visible'],
            'moon_real_vs_eye': md['real_vs_eye'], 'moon_science': md['science'],
            'moon_meaning': md['igbo_meaning'],
        })
    context = {
        'title': 'Amuzhi Calendar - 3-Day Full + Pitch Dark Night - Igbo Eye Observation',
        'today': today, 'market_today': market_today, 'market_meaning': market_meaning,
        'igbo_month': igbo_month, 'igbo_months_all': IGBO_MONTHS_AUTH,
        'moon_name': moon_name, 'moon_age': moon_age,
        'moon_emoji': moon_detail['emoji'], 'moon_detail': moon_detail,
        'tide_today': 'Neap Tide 1.2m' if 'Quarter' in moon_name else 'Spring Tide 2.5m' if 'Full' in moon_name or 'Dark' in moon_name or 'New' in moon_name else 'Moderate Tide',
        'month': month_data,
    }
    return render(request, 'amuzhi_calendar/index.html', context)

def today_view(request): return calendar_view(request)
def year_view(request, year): return render(request, 'amuzhi_calendar/year.html', {'year': year, 'igbo_months': IGBO_MONTHS_AUTH})
def month_view(request, year, month): return render(request, 'amuzhi_calendar/month.html', {'year': year, 'month': month})
def convert_view(request, day, month, year):
    d = date(year, month, day)
    market, meaning = get_market_day(d)
    moon = get_moon_detail(d)
    return render(request, 'amuzhi_calendar/convert.html', {'date': d, 'market': market, 'meaning': meaning, 'moon': moon})
def market_calculator_view(request):
    result = None
    if request.method == 'POST':
        try:
            d = int(request.POST.get('day')); m = int(request.POST.get('month')); y = int(request.POST.get('year'))
            target = date(y, m, d)
            market, meaning = get_market_day(target)
            result = {'date': target, 'market': market, 'meaning': meaning}
        except Exception as e:
            result = {'error': str(e)}
    return render(request, 'amuzhi_calendar/calculator.html', {'result': result})
def quiz_view(request): return render(request, 'amuzhi_calendar/quiz.html', {'months': IGBO_MONTHS_AUTH})
def festival_view(request): return render(request, 'amuzhi_calendar/festival.html', {'months': IGBO_MONTHS_AUTH})
