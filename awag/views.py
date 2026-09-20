from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from datetime import date, datetime, timedelta
import random
import json
import os

# AWAG - Africas' Weekly Activities Guide
# 58 Regions - Trading Herders Hunters Healers Leaders Economic Influenced by Nature
# Wind locality: East Monsoon Kusi/Kaskazi, West Harmattan, South Benguela/Agulhas, North Mistral, Rift Lake Breeze, Red Sea Khamsin
# Rain locality: Guinea 2 seasons, Sahel Jun-Oct, Long rains Mar-May, Med winter, Winter reverse Jun-Aug, Cyclone Nov-Apr, Lake Chad shrink

REGIONS_58 = [
    {'code':'Bonny NG','name':'Bonny','country':'Nigeria','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan NE Dry 15kt','rain':'Guinea 2 seasons Rain Apr-Jul','tide_port':'Niger Delta Bonny Opobo Brass','lingua':'en','element':'Afo Earth','activity':'Traders fishermen oil'},
    {'code':'Lagos NG','name':'Lagos','country':'Nigeria','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan NE Dry 12kt','rain':'Guinea 2 seasons Apr-Jul Oct','tide_port':'Lagos-Bar beach','lingua':'en','element':'Eke Fire','activity':'Traders transporters'},
    {'code':'Baga NG','name':'Baga','country':'Nigeria','zone':'Lake Chad','zone_code':'WA-LC','wind':'Harmattan NE Dry 18kt dusty','rain':'Sahel dry Lake Chad shrink','tide_port':'Baga Lake Chad inland','lingua':'en','element':'Afo Earth','activity':'Herders fishermen lake'},
    {'code':'Tema GH','name':'Tema','country':'Ghana','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan SW 10kt','rain':'Guinea 2 seasons Apr-Jul Sep-Oct','tide_port':'Ghana Elmina','lingua':'en','element':'Orie Water','activity':'Traders fishermen'},
    {'code':'Abidjan CI','name':'Abidjan','country':'Ivory Coast','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan SW 8kt','rain':'Guinea heavy Apr-Jul','tide_port':'Ivory Coast lagoon','lingua':'fr','element':'Nkwo Air','activity':'Traders hunters'},
    {'code':'Dakar SN','name':'Dakar','country':'Senegal','zone':'Sahel Atlantic','zone_code':'WA-S','wind':'Harmattan NE Dry 15kt upwelling','rain':'Sahel rainy Jun-Oct','tide_port':'Senegal upwelling','lingua':'fr','element':'Eke Fire','activity':'Herders fishermen'},
    {'code':'Bissau GW','name':'Bissau','country':'Guinea-Bissau','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan 12kt Bijagos','rain':'Guinea rainy May-Nov','tide_port':'Guinea-Bissau Bijagos','lingua':'pt','element':'Nkwo Air','activity':'Traders fishermen islands'},
    {'code':'Conakry GN','name':'Conakry','country':'Guinea','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan 10kt','rain':'Guinea heavy May-Oct','tide_port':'Guinea Conakry','lingua':'fr','element':'Eke Fire','activity':'Traders miners'},
    {'code':'Freetown SL','name':'Freetown','country':'Sierra Leone','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan SW','rain':'Guinea heavy May-Oct','tide_port':'Sierra Leone','lingua':'en','element':'Afo Earth','activity':'Traders fishermen'},
    {'code':'Monrovia LR','name':'Monrovia','country':'Liberia','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan SW','rain':'Guinea rainy Apr-Oct','tide_port':'Liberia','lingua':'en','element':'Nkwo Air','activity':'Traders rubber'},
    {'code':'Cotonou BJ','name':'Cotonou','country':'Benin','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan SW 10kt','rain':'Guinea 2 seasons','tide_port':'Benin','lingua':'fr','element':'Orie Water','activity':'Traders fishermen'},
    {'code':'Lome TG','name':'Lome','country':'Togo','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan SW','rain':'Guinea 2 seasons','tide_port':'Togo','lingua':'fr','element':'Eke Fire','activity':'Traders'},
    {'code':'Douala CM','name':'Douala','country':'Cameroon','zone':'Central Guinea','zone_code':'CA-G','wind':'Harmattan 8kt equatorial','rain':'Guinea heavy Mar-Oct','tide_port':'Cameroon','lingua':'fr','element':'Orie Water','activity':'Traders hunters oil'},
    {'code':'Libreville GA','name':'Libreville','country':'Gabon','zone':'Central','zone_code':'CA','wind':'Equatorial SW 8kt','rain':'Equator rain year round','tide_port':'Gabon','lingua':'fr','element':'Nkwo Air','activity':'Hunters oil'},
    {'code':'Pointe-Noire CG','name':'Pointe-Noire','country':'Congo','zone':'Central','zone_code':'CA','wind':'Benguela edge SW 10kt','rain':'Equator 2 rains','tide_port':'Congo','lingua':'fr','element':'Afo Earth','activity':'Traders oil'},
    {'code':'Mopti ML','name':'Mopti','country':'Mali','zone':'Sahel Inner Delta','zone_code':'WA-S','wind':'Harmattan NE Dry 20kt dusty','rain':'Sahel Jun-Sep Niger Inner Delta','tide_port':'Mali Niger Inner Delta','lingua':'fr','element':'Afo Earth','activity':'Herders fishermen herders'},
    {'code':'Nouakchott MR','name':'Nouakchott','country':'Mauritania','zone':'Sahel Atlantic','zone_code':'WA-S','wind':'Harmattan NE 18kt Banc dArguin','rain':'Sahel arid Jun-Oct','tide_port':'Mauritania Banc dArguin','lingua':'fr','element':'Eke Fire','activity':'Herders fishermen'},
    {'code':'Luanda AO','name':'Luanda','country':'Angola','zone':'South Benguela','zone_code':'SA-B','wind':'Benguela SW 12kt North','rain':'South rainy Nov-Apr','tide_port':'Angola North','lingua':'pt','element':'Orie Water','activity':'Traders oil fishermen'},
    {'code':'Namibe AO','name':'Namibe','country':'Angola','zone':'South Benguela Desert','zone_code':'SA-B','wind':'Benguela SW 18kt desert','rain':'Desert arid Benguela fog','tide_port':'Angola South Benguela','lingua':'pt','element':'Eke Fire','activity':'Herders fishermen desert'},
    {'code':'Kinshasa CD','name':'Kinshasa','country':'DR Congo','zone':'Central Congo','zone_code':'CA','wind':'Congo Basin variable','rain':'Equator rain year','tide_port':'Congo River inland','lingua':'fr','element':'Nkwo Air','activity':'Traders healers leaders'},
    {'code':'Kalemie CD','name':'Kalemie','country':'DR Congo','zone':'Rift Tanganyika','zone_code':'Rift','wind':'Lake Tanganyika breeze 8kt','rain':'Rift short rains Oct-Dec long Mar-May','tide_port':'DR Congo Tanganyika','lingua':'fr','element':'Orie Water','activity':'Fishermen lake'},
    {'code':'Kigoma TZ','name':'Kigoma','country':'Tanzania','zone':'Rift Tanganyika','zone_code':'Rift','wind':'Lake Tanganyika breeze','rain':'Rift 2 seasons','tide_port':'Lake Tanganyika','lingua':'sw','element':'Nkwo Air','activity':'Fishermen traders'},
    {'code':'Mombasa KE','name':'Mombasa','country':'Kenya','zone':'East Monsoon','zone_code':'EA-M','wind':'Monsoon Kusi SE 12kt Kaskazi NE Dec-Mar','rain':'Long rains Mar-May short Oct-Dec','tide_port':'Kenya Swahili coast','lingua':'sw','element':'Afo Earth','activity':'Traders fishermen Swahili'},
    {'code':'Kisumu KE','name':'Kisumu','country':'Kenya','zone':'Lake Victoria','zone_code':'Rift','wind':'Lake Victoria breeze 10kt Winam Gulf','rain':'Lake Victoria long Mar-May','tide_port':'Lake Victoria Winam Gulf','lingua':'sw','element':'Orie Water','activity':'Fishermen lake traders'},
    {'code':'Turkana KE','name':'Turkana','country':'Kenya','zone':'Rift Desert Lake','zone_code':'Rift','wind':'Turkana Jet SE 20kt desert','rain':'Desert arid Rift','tide_port':'Lake Turkana Rudolf desert lake','lingua':'sw','element':'Eke Fire','activity':'Herders fishermen desert'},
    {'code':'Mwanza TZ','name':'Mwanza','country':'Tanzania','zone':'Lake Victoria','zone_code':'Rift','wind':'Lake Victoria breeze','rain':'Long rains Mar-May','tide_port':'Lake Victoria Tanzania','lingua':'sw','element':'Afo Earth','activity':'Fishermen'},
    {'code':'Dar es Salaam TZ','name':'Dar es Salaam','country':'Tanzania','zone':'East Monsoon','zone_code':'EA-M','wind':'Monsoon Kusi SE 12kt','rain':'Long rains Mar-May','tide_port':'Tanzania Dar','lingua':'sw','element':'Orie Water','activity':'Traders port'},
    {'code':'Zanzibar TZ','name':'Zanzibar','country':'Tanzania','zone':'East Monsoon Islands','zone_code':'EA-M','wind':'Monsoon Kusi SE 15kt spice','rain':'Long rains Mar-May','tide_port':'Zanzibar spice','lingua':'sw','element':'Nkwo Air','activity':'Traders spice fishermen'},
    {'code':'Mogadishu SO','name':'Mogadishu','country':'Somalia','zone':'East Monsoon Horn','zone_code':'EA-M','wind':'Monsoon Kaskazi NE 15kt longest coast','rain':'Arid 2 rains Gu Deyr','tide_port':'Somalia longest coast','lingua':'ar','element':'Eke Fire','activity':'Herders fishermen pastoral'},
    {'code':'Djibouti DJ','name':'Djibouti','country':'Djibouti','zone':'Red Sea Rift','zone_code':'RedSea','wind':'Khamsin Red Sea N 14kt','rain':'Arid Red Sea','tide_port':'Djibouti Red Sea','lingua':'fr','element':'Eke Fire','activity':'Traders port'},
    {'code':'Beira MZ','name':'Beira','country':'Mozambique','zone':'South East Monsoon','zone_code':'SE-M','wind':'Monsoon SE Sofala 12kt','rain':'Cyclone season Nov-Apr rainy','tide_port':'Mozambique North Sofala','lingua':'pt','element':'Orie Water','activity':'Traders fishermen cyclone'},
    {'code':'Maputo MZ','name':'Maputo','country':'Mozambique','zone':'South East','zone_code':'SE-M','wind':'Monsoon SE South 10kt','rain':'Rainy Nov-Mar dry winter','tide_port':'Mozambique South','lingua':'pt','element':'Afo Earth','activity':'Traders'},
    {'code':'Mahajanga MG','name':'Mahajanga','country':'Madagascar','zone':'Indian Ocean Island','zone_code':'Island','wind':'Monsoon NW Madagascar 12kt','rain':'Cyclone Nov-Apr rainy','tide_port':'Madagascar Madagasy','lingua':'fr','element':'Nkwo Air','activity':'Fishermen traders island'},
    {'code':'Antananarivo MG','name':'Antananarivo','country':'Madagascar','zone':'Highland Island','zone_code':'Island','wind':'Highland trade SE','rain':'Highland rainy Nov-Apr','tide_port':'Madagascar highland inland','lingua':'fr','element':'Afo Earth','activity':'Healers traders rice'},
    {'code':'Nairobi KE','name':'Nairobi','country':'Kenya','zone':'Highland East','zone_code':'EA-M','wind':'Highland SE 10kt','rain':'Long rains Mar-May','tide_port':'Kenya highland inland','lingua':'sw','element':'Eke Fire','activity':'Leaders traders'},
    {'code':'Addis Ababa ET','name':'Addis Ababa','country':'Ethiopia','zone':'Highland Horn','zone_code':'EA-M','wind':'Highland Rift SE','rain':'Kiremt Jun-Sep Belg Mar-May','tide_port':'Ethiopia highland inland','lingua':'am','element':'Afo Earth','activity':'Leaders herders'},
    {'code':'Kampala UG','name':'Kampala','country':'Uganda','zone':'Lake Victoria','zone_code':'Rift','wind':'Lake Victoria breeze','rain':'2 rains Mar-May Oct-Dec','tide_port':'Uganda Lake Victoria','lingua':'en','element':'Nkwo Air','activity':'Traders fishermen'},
    {'code':'Casablanca MA','name':'Casablanca','country':'Morocco','zone':'Med Atlantic-Med convergence','zone_code':'NA-Med','wind':'Mediterranean Mistral NW 10kt Atlantic convergence','rain':'Med winter rain Oct-Apr summer dry','tide_port':'Morocco Atlantic-Med convergence','lingua':'ar','element':'Orie Water','activity':'Traders fishermen'},
    {'code':'Algiers DZ','name':'Algiers','country':'Algeria','zone':'Med','zone_code':'NA-Med','wind':'Mistral NW Med 10kt','rain':'Med winter rain','tide_port':'Algeria Med','lingua':'ar','element':'Nkwo Air','activity':'Traders'},
    {'code':'Tunis TN','name':'Tunis','country':'Tunisia','zone':'Med','zone_code':'NA-Med','wind':'Mistral Med 12kt','rain':'Med winter rain Oct-Apr','tide_port':'Tunisia Med','lingua':'ar','element':'Eke Fire','activity':'Traders'},
    {'code':'Tripoli LY','name':'Tripoli','country':'Libya','zone':'Med Sahara','zone_code':'NA-Med','wind':'Ghibli Sirocco S 15kt Med','rain':'Med arid winter rain','tide_port':'Libya Med','lingua':'ar','element':'Orie Water','activity':'Traders herders'},
    {'code':'Alexandria EG','name':'Alexandria','country':'Egypt','zone':'Med Nile','zone_code':'NA-Med','wind':'Etesian NW Med 12kt','rain':'Med arid winter rain','tide_port':'Egypt Med','lingua':'ar','element':'Nkwo Air','activity':'Traders fishermen Nile'},
    {'code':'Hurghada EG','name':'Hurghada','country':'Egypt','zone':'Red Sea','zone_code':'RedSea','wind':'Khamsin N Red Sea 14kt','rain':'Arid Red Sea','tide_port':'Egypt Red Sea','lingua':'ar','element':'Eke Fire','activity':'Fishermen divers'},
    {'code':'Port Sudan SD','name':'Port Sudan','country':'Sudan','zone':'Red Sea','zone_code':'RedSea','wind':'Khamsin Red Sea N 14kt','rain':'Arid Red Sea rainy Nov-Jan','tide_port':'Sudan Red Sea','lingua':'ar','element':'Orie Water','activity':'Traders fishermen'},
    {'code':'Cairo EG','name':'Cairo','country':'Egypt','zone':'Nile Sahara','zone_code':'NA-Med','wind':'Khamsin hot SE 15kt','rain':'Desert arid','tide_port':'Egypt Nile inland','lingua':'ar','element':'Afo Earth','activity':'Leaders traders'},
    {'code':'Rabat MA','name':'Rabat','country':'Morocco','zone':'Med Atlantic','zone_code':'NA-Med','wind':'Atlantic Mistral NW','rain':'Med winter rain','tide_port':'Morocco Atlantic','lingua':'ar','element':'Eke Fire','activity':'Leaders'},
    {'code':'Khartoum SD','name':'Khartoum','country':'Sudan','zone':'Sahel Nile','zone_code':'WA-S','wind':'Harmattan NE dry','rain':'Sahel Jul-Sep','tide_port':'Sudan Nile inland','lingua':'ar','element':'Afo Earth','activity':'Herders traders Nile'},
    {'code':'Walvis Bay NA','name':'Walvis Bay','country':'Namibia','zone':'South Benguela Desert','zone_code':'SA-B','wind':'Benguela SW 18kt desert fog','rain':'Desert fog Benguela arid','tide_port':'Namibia','lingua':'en','element':'Orie Water','activity':'Fishermen desert herders'},
    {'code':'Cape Town ZA','name':'Cape Town','country':'South Africa','zone':'South West convergence','zone_code':'SA-B','wind':'Cape Doctor SE 20kt SW winter','rain':'Winter rain Jun-Aug reverse Med','tide_port':'South Africa West convergence','lingua':'en','element':'Nkwo Air','activity':'Traders fishermen wine'},
    {'code':'Durban ZA','name':'Durban','country':'South Africa','zone':'South East Agulhas','zone_code':'SA-A','wind':'Agulhas SE 12kt East','rain':'Summer rain Nov-Mar','tide_port':'South Africa East Agulhas','lingua':'en','element':'Orie Water','activity':'Traders fishermen'},
    {'code':'Johannesburg ZA','name':'Johannesburg','country':'South Africa','zone':'Highveld','zone_code':'SA-A','wind':'Highveld SE','rain':'Summer rain Oct-Mar','tide_port':'South Africa highveld inland','lingua':'en','element':'Afo Earth','activity':'Leaders miners traders'},
    {'code':'Harare ZW','name':'Harare','country':'Zimbabwe','zone':'Highveld','zone_code':'SA-A','wind':'SE trade highveld','rain':'Summer rain Nov-Mar','tide_port':'Zimbabwe inland','lingua':'en','element':'Eke Fire','activity':'Traders farmers'},
    {'code':'Lusaka ZM','name':'Lusaka','country':'Zambia','zone':'Central Plateau','zone_code':'CA','wind':'SE trade plateau','rain':'Rainy Nov-Apr','tide_port':'Zambia inland','lingua':'en','element':'Afo Earth','activity':'Traders farmers'},
    {'code':'Yaounde CM','name':'Yaounde','country':'Cameroon','zone':'Central Forest','zone_code':'CA','wind':'Equatorial variable','rain':'2 rains Mar-Jun Sep-Nov','tide_port':'Cameroon inland','lingua':'fr','element':'Nkwo Air','activity':'Hunters healers'},
    {'code':'Brazzaville CG','name':'Brazzaville','country':'Congo','zone':'Central Congo','zone_code':'CA','wind':'Congo Basin variable','rain':'Equator 2 rains','tide_port':'Congo River inland','lingua':'fr','element':'Orie Water','activity':'Traders'},
    {'code':'Brazzaville CG','name':'Brazzaville','country':'Congo','zone':'Central Congo','zone_code':'CA','wind':'Congo Basin variable','rain':'Equator 2 rains','tide_port':'Congo River inland','lingua':'fr','element':'Orie Water','activity':'Traders'},
    {'code':'Banjul GM','name':'Banjul','country':'Gambia','zone':'Guinea','zone_code':'WA-G','wind':'Harmattan 10kt River Gambia','rain':'Guinea rainy May-Oct','tide_port':'Gambia River Gambia','lingua':'en','element':'Orie Water','activity':'Traders fishermen rice-fish Mandinka river'},
    {'code':'Malabo GQ','name':'Malabo','country':'Equatorial Guinea','zone':'Central Guinea','zone_code':'CA-G','wind':'Monsoon SW 10kt island','rain':'Guinea heavy Mar-Nov','tide_port':'Equatorial Guinea Bioko','lingua':'es','element':'Nkwo Air','activity':'Traders oil fishermen'},
    {'code':'Sao Tome ST','name':'Sao Tome','country':'Sao Tome and Principe','zone':'Gulf Guinea','zone_code':'CA-G','wind':'Monsoon SW 8kt Gulf','rain':'Equator 2 rains','tide_port':'Sao Tome Gulf Guinea','lingua':'pt','element':'Afo Earth','activity':'Fishermen island cocoa traders'},
]

ELEMENTS = {
    'EKE': {'element':'Fire','emoji':'🔥','color':'#ff4500','meaning':'Light New beginnings Creativity','advice':'Traders start, fishermen shore, farmers planting'},
    'ORIE': {'element':'Water','emoji':'💧','color':'#1e90ff','meaning':'Flow Stability Cleansing','advice':'Water, fishing best when high tide, stability'},
    'AFO': {'element':'Earth','emoji':'🌍','color':'#8B4513','meaning':'Grounding Harvest Abundance','advice':'Earth, harvest, market day sell'},
    'NKWO': {'element':'Air','emoji':'🌬','color':'#87ceeb','meaning':'Spirit Reflection Transition','advice':'Air, spirits, preservation, reflection'},
}

# AWAG Coding 678 loader
def load_awag_coding_groups():
    path = 'awag/data/awag_grouped.json'
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return {}

def awag_coding(request):
    groups = load_awag_coding_groups()
    mapped = []
    for r in REGIONS_58:
        activities = []
        for key, vals in groups.items():
            if r['name'].split()[0].lower() in key.lower() or r['code'].split()[0].lower() in key.lower() or r['country'].lower() in key.lower():
                activities.extend(vals)
        mapped.append({**r, 'activities': activities[:12], 'count': len(activities)})
    total_activities = sum(len(v) for v in groups.values()) if groups else 0
    return render(request, 'awag/coding.html', {'regions_58': mapped, 'total': len(groups), 'total_activities': total_activities})

def get_element_info(market_day):
    return ELEMENTS.get(market_day.upper(), ELEMENTS['EKE'])

def get_wind_for_region(code):
    for r in REGIONS_58:
        if r['code']==code:
            return r
    return REGIONS_58[0]

def awag_home(request):
    try:
        from amuzhi_calendar.models import MarketDay
        from amuzhi_calendar.views import get_today_market_day
        today_market = get_today_market_day()
    except:
        today_market = None
    zone = request.GET.get('zone')
    regions_filtered = [r for r in REGIONS_58 if r['zone_code']==zone or r['zone']==zone] if zone else REGIONS_58
    lang = request.GET.get('lang', 'en')
    langs = [('en','English'),('fr','French'),('es','Spanish'),('pt','Portuguese'),('sw','Swahili'),('ar','Arabic'),('ig','Igbo'),('am','Amharic')]
    try:
        from.models import Region, WeeklyGuide, Tide, MoonCycle
        regions_db = Region.objects.all()
        guides = WeeklyGuide.objects.filter(language=lang).order_by('-week_start')[:10] if WeeklyGuide.objects.exists() else []
        tides = Tide.objects.order_by('datetime')[:10] if Tide.objects.exists() else []
        moon_today = MoonCycle.objects.filter(date=date.today()).first() if MoonCycle.objects.exists() else None
        total = regions_db.count() if regions_db else len(REGIONS_58)
    except:
        regions_db = []
        guides = []
        tides = []
        moon_today = None
        total = len(REGIONS_58)
    today_element = None
    if today_market:
        today_element = get_element_info(today_market.market_day)
    return render(request, 'awag/home.html', {
        'regions_58': regions_filtered,
        'regions': regions_db or regions_filtered,
        'guides': guides,
        'tides': tides,
        'moon_today': moon_today,
        'today_market': today_market,
        'today_element': today_element,
        'elements': ELEMENTS,
        'lang': lang,
        'langs': langs,
        'total_regions': total,
        'zones': sorted(set(r['zone'] for r in REGIONS_58)),
        'zone_codes': sorted(set(r['zone_code'] for r in REGIONS_58)),
        'selected_zone': zone,
        'today': today_market,
    })

def awag_region(request, code):
    region_dict = get_wind_for_region(code)
    try:
        from.models import Region
        region_db = get_object_or_404(Region, code=code)
    except:
        region_db = region_dict
    lang = request.GET.get('lang', region_dict.get('lingua','en') if isinstance(region_dict, dict) else 'en')
    try:
        from.models import WeeklyGuide
        guides = WeeklyGuide.objects.filter(region=region_db).order_by('-week_start') if hasattr(region_db, 'id') else []
    except:
        guides = []
    element_info = get_element_info(region_dict.get('element','EKE').split()[0] if isinstance(region_dict, dict) else 'EKE')
    return render(request, 'awag/region.html', {
        'region': region_db,
        'region_dict': region_dict,
        'guides': guides,
        'lang': lang,
        'element_info': element_info,
        'elements': ELEMENTS,
    })

def awag_tides(request):
    try:
        from.models import Tide
        tides = Tide.objects.order_by('datetime')[:50]
    except:
        tides = []
        base = datetime.now()
        for r in REGIONS_58[:20]:
            tides.append({
                'port': r['tide_port'],
                'code': r['code'],
                'high': (base + timedelta(hours=random.randint(1,12))).strftime('%H:%M'),
                'low': (base + timedelta(hours=random.randint(13,23))).strftime('%H:%M'),
                'height': round(random.uniform(0.8,3.2),1),
                'wind': r['wind'],
                'rain': r['rain'],
            })
    return render(request, 'awag/tides.html', {'tides': tides, 'regions_58': REGIONS_58})

def awag_tide_table(request):
    from.models import Tide
    port = request.GET.get('port','Bonny Opobo Brass')
    tides = Tide.objects.filter(location__icontains=port).order_by('datetime')[:28]
    ports = ['Bonny Opobo Brass','Calabar','Lagos-Bar','Mombasa','Dakar','Tema','Abidjan','Cotonou','Lome','Douala','Beira','Maputo','Djibouti','Port Sudan','Alexandria','Casablanca','Cape Town','Durban','Walvis Bay','Luanda']
    return render(request, 'awag/tide_table.html', {'tides':tides,'ports':ports,'selected_port':port,'regions_58':REGIONS_58})

def awag_farmers(request):
    lang = request.GET.get('lang','en')
    zone = request.GET.get('zone')
    regions = [r for r in REGIONS_58 if not zone or r['zone_code']==zone]
    try:
        from.models import WeeklyGuide
        week_start = date.today() - timedelta(days=date.today().weekday())
        guides = WeeklyGuide.objects.filter(week_start=week_start, language=lang) if WeeklyGuide.objects.exists() else []
    except:
        guides = []
        week_start = date.today() - timedelta(days=date.today().weekday())
    return render(request, 'awag/farmers.html', {'regions_58':regions,'guides':guides,'lang':lang,'zone':zone,'week_start':week_start})

def api_tides(request):
    port = request.GET.get('port','Bonny')
    from.models import Tide
    tides = Tide.objects.filter(location__icontains=port).order_by('datetime')[:14].values('location','datetime','high_height_m','low_height_m','advice_en')
    return JsonResponse({'port':port,'tides':list(tides)})

def api_moon(request, date_str):
    try:
        d = datetime.strptime(date_str, '%Y-%m-%d').date()
        try:
            from amuzhi_calendar.models import MarketDay
            md = MarketDay.objects.filter(date_gregorian=d).first()
            if md:
                return JsonResponse({'date': date_str,'moon_symbol': md.moon_symbol,'moon_stage': md.moon_stage,'illumination': md.illumination,'market_day': md.market_day,'element': get_element_info(md.market_day)})
        except:
            pass
        from.models import moon_phase_info
        info = moon_phase_info(d)
        return JsonResponse(info)
    except Exception as e:
        return JsonResponse({'error': 'Invalid date', 'detail': str(e)}, status=400)

def api_wind_rain(request):
    zone = request.GET.get('zone')
    data = [r for r in REGIONS_58 if not zone or r['zone_code']==zone or r['zone']==zone]
    return JsonResponse({'total': len(data), 'regions': data, 'elements': ELEMENTS})

def awag_weekly(request):
    today = date.today()
    try:
        from amuzhi_calendar.views import get_today_market_day
        today_md = get_today_market_day()
        market_today = today_md.market_day if today_md else 'EKE'
    except:
        market_today = 'EKE'
    element = get_element_info(market_today)
    return render(request, 'awag/weekly.html', {
        'week_start': today - timedelta(days=today.weekday()),
        'week_end': today + timedelta(days=6-today.weekday()),
        'market_today': market_today,
        'element': element,
        'regions_58': REGIONS_58,
        'zones': sorted(set(r['zone'] for r in REGIONS_58)),
    })