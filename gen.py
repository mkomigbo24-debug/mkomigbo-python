import pathlib
base = pathlib.Path("africa_weekly")
base.mkdir(exist_ok=True)
(base / "templates" / "awag").mkdir(parents=True, exist_ok=True)
(base / "migrations").mkdir(parents=True, exist_ok=True)
(base / "__init__.py").write_text("", encoding="utf-8")
(base / "migrations" / "__init__.py").write_text("", encoding="utf-8")
(base / "apps.py").write_text("from django.apps import AppConfig\nclass AfricaWeeklyConfig(AppConfig):\n default_auto_field='django.db.models.BigAutoField'\n name='africa_weekly'\n verbose_name=\"AWAG\"\n", encoding="utf-8")
(base / "admin.py").write_text("from django.contrib import admin\n", encoding="utf-8")
(base / "models.py").write_text("from django.db import models\nclass Region(models.Model):\n code=models.CharField(max_length=30,unique=True)\n name=models.CharField(max_length=100)\n country=models.CharField(max_length=100)\n zone=models.CharField(max_length=100)\n zone_code=models.CharField(max_length=20)\n wind=models.CharField(max_length=200)\n rain=models.CharField(max_length=200)\n tide_port=models.CharField(max_length=200)\n lingua=models.CharField(max_length=10,default='en')\n element=models.CharField(max_length=50)\n activity=models.CharField(max_length=200)\n def __str__(self): return self.code\n", encoding="utf-8")
(base / "urls.py").write_text("from django.urls import path\nfrom . import views\nurlpatterns=[path('', views.awag_home, name='awag_home'), path('region/<path:code>/', views.awag_region, name='awag_region'), path('tides/', views.awag_tides, name='awag_tides'), path('tide-table/', views.awag_tide_table, name='awag_tide_table'), path('farmers/', views.awag_farmers, name='awag_farmers'), path('weekly/', views.awag_weekly, name='awag_weekly'), path('api/tides/', views.api_tides, name='api_tides'), path('api/moon/<str:date_str>/', views.api_moon, name='api_moon'), path('api/wind-rain/', views.api_wind_rain, name='api_wind_rain'), path('view/', views.awag_view, name='awag_view'), path('weekly-guide/', views.weekly_guide, name='weekly_guide'),]\n", encoding="utf-8")

raw=[
"Bonny NG|Bonny|Nigeria|Guinea|WA-G|Harmattan NE Dry 15kt|Guinea 2 seasons Rain Apr-Jul|Niger Delta Bonny Opobo Brass|en|Afo Earth|Traders fishermen oil",
"Lagos NG|Lagos|Nigeria|Guinea|WA-G|Harmattan NE Dry 12kt|Guinea 2 seasons Apr-Jul Oct|Lagos-Bar beach|en|Eke Fire|Traders transporters",
"Baga NG|Baga|Nigeria|Lake Chad|WA-LC|Harmattan NE Dry 18kt dusty|Sahel dry Lake Chad shrink|Baga Lake Chad inland|en|Afo Earth|Herders fishermen lake",
"Tema GH|Tema|Ghana|Guinea|WA-G|Harmattan SW 10kt|Guinea 2 seasons Apr-Jul Sep-Oct|Ghana Elmina|en|Orie Water|Traders fishermen",
"Accra GH|Accra|Ghana|Guinea|WA-G|Harmattan SW 10kt|Guinea 2 seasons Apr-Jul|Accra|en|Nkwo Air|Traders fishermen",
"Abidjan CI|Abidjan|Ivory Coast|Guinea|WA-G|Harmattan SW 8kt|Guinea heavy Apr-Jul|Ivory Coast lagoon|fr|Nkwo Air|Traders hunters",
"Dakar SN|Dakar|Senegal|Sahel Atlantic|WA-S|Harmattan NE Dry 15kt upwelling|Sahel rainy Jun-Oct|Senegal upwelling|fr|Eke Fire|Herders fishermen",
"Banjul GM|Banjul|Gambia|Sahel Atlantic|WA-S|Harmattan NE 12kt|Sahel Jun-Oct|Gambia River|en|Orie Water|Traders fishermen",
"Bissau GW|Bissau|Guinea-Bissau|Guinea|WA-G|Harmattan 12kt Bijagos|Guinea rainy May-Nov|Guinea-Bissau Bijagos|pt|Nkwo Air|Traders fishermen islands",
"Conakry GN|Conakry|Guinea|Guinea|WA-G|Harmattan 10kt|Guinea heavy May-Oct|Guinea Conakry|fr|Eke Fire|Traders miners",
"Freetown SL|Freetown|Sierra Leone|Guinea|WA-G|Harmattan SW|Guinea heavy May-Oct|Sierra Leone|en|Afo Earth|Traders fishermen",
"Monrovia LR|Monrovia|Liberia|Guinea|WA-G|Harmattan SW|Guinea rainy Apr-Oct|Liberia|en|Nkwo Air|Traders rubber",
"Cotonou BJ|Cotonou|Benin|Guinea|WA-G|Harmattan SW 10kt|Guinea 2 seasons|Benin|fr|Orie Water|Traders fishermen",
"Lome TG|Lome|Togo|Guinea|WA-G|Harmattan SW|Guinea 2 seasons|Togo|fr|Eke Fire|Traders",
"Douala CM|Douala|Cameroon|Central Guinea|CA-G|Harmattan 8kt equatorial|Guinea heavy Mar-Oct|Cameroon|fr|Orie Water|Traders hunters oil",
"Libreville GA|Libreville|Gabon|Central|CA|Equatorial SW 8kt|Equator rain year round|Gabon|fr|Nkwo Air|Hunters oil",
"Pointe-Noire CG|Pointe-Noire|Congo|Central|CA|Benguela edge SW 10kt|Equator 2 rains|Congo|fr|Afo Earth|Traders oil",
"Mopti ML|Mopti|Mali|Sahel Inner Delta|WA-S|Harmattan NE Dry 20kt dusty|Sahel Jun-Sep Niger Inner Delta|Mali Niger Inner Delta|fr|Afo Earth|Herders fishermen herders",
"Nouakchott MR|Nouakchott|Mauritania|Sahel Atlantic|WA-S|Harmattan NE 18kt Banc dArguin|Sahel arid Jun-Oct|Mauritania Banc dArguin|fr|Eke Fire|Herders fishermen",
"Luanda AO|Luanda|Angola|South Benguela|SA-B|Benguela SW 12kt North|South rainy Nov-Apr|Angola North|pt|Orie Water|Traders oil fishermen",
"Namibe AO|Namibe|Angola|South Benguela Desert|SA-B|Benguela SW 18kt desert|Desert arid Benguela fog|Angola South Benguela|pt|Eke Fire|Herders fishermen desert",
"Kinshasa CD|Kinshasa|DR Congo|Central Congo|CA|Congo Basin variable|Equator rain year|Congo River inland|fr|Nkwo Air|Traders healers leaders",
"Kalemie CD|Kalemie|DR Congo|Rift Tanganyika|Rift|Lake Tanganyika breeze 8kt|Rift short rains Oct-Dec long Mar-May|DR Congo Tanganyika|fr|Orie Water|Fishermen lake",
"Kigoma TZ|Kigoma|Tanzania|Rift Tanganyika|Rift|Lake Tanganyika breeze|Rift 2 seasons|Lake Tanganyika|sw|Nkwo Air|Fishermen traders",
"Mombasa KE|Mombasa|Kenya|East Monsoon|EA-M|Monsoon Kusi SE 12kt Kaskazi NE Dec-Mar|Long rains Mar-May short Oct-Dec|Kenya Swahili coast|sw|Afo Earth|Traders fishermen Swahili",
"Kisumu KE|Kisumu|Kenya|Lake Victoria|Rift|Lake Victoria breeze 10kt Winam Gulf|Lake Victoria long Mar-May|Lake Victoria Winam Gulf|sw|Orie Water|Fishermen lake traders",
"Turkana KE|Turkana|Kenya|Rift Desert Lake|Rift|Turkana Jet SE 20kt desert|Desert arid Rift|Lake Turkana Rudolf desert lake|sw|Eke Fire|Herders fishermen desert",
"Mwanza TZ|Mwanza|Tanzania|Lake Victoria|Rift|Lake Victoria breeze|Long rains Mar-May|Lake Victoria Tanzania|sw|Afo Earth|Fishermen",
"Dar es Salaam TZ|Dar es Salaam|Tanzania|East Monsoon|EA-M|Monsoon Kusi SE 12kt|Long rains Mar-May|Tanzania Dar|sw|Orie Water|Traders port",
"Zanzibar TZ|Zanzibar|Tanzania|East Monsoon Islands|EA-M|Monsoon Kusi SE 15kt spice|Long rains Mar-May|Zanzibar spice|sw|Nkwo Air|Traders spice fishermen",
"Mogadishu SO|Mogadishu|Somalia|East Monsoon Horn|EA-M|Monsoon Kaskazi NE 15kt longest coast|Arid 2 rains Gu Deyr|Somalia longest coast|ar|Eke Fire|Herders fishermen pastoral",
"Djibouti DJ|Djibouti|Djibouti|Red Sea Rift|RedSea|Khamsin Red Sea N 14kt|Arid Red Sea|Djibouti Red Sea|fr|Eke Fire|Traders port",
"Beira MZ|Beira|Mozambique|South East Monsoon|SE-M|Monsoon SE Sofala 12kt|Cyclone season Nov-Apr rainy|Mozambique North Sofala|pt|Orie Water|Traders fishermen cyclone",
"Maputo MZ|Maputo|Mozambique|South East|SE-M|Monsoon SE South 10kt|Rainy Nov-Mar dry winter|Mozambique South|pt|Afo Earth|Traders",
"Mahajanga MG|Mahajanga|Madagascar|Indian Ocean Island|Island|Monsoon NW Madagascar 12kt|Cyclone Nov-Apr rainy|Madagascar Madagasy|fr|Nkwo Air|Fishermen traders island",
"Antananarivo MG|Antananarivo|Madagascar|Highland Island|Island|Highland trade SE|Highland rainy Nov-Apr|Madagascar highland inland|fr|Afo Earth|Healers traders rice",
"Nairobi KE|Nairobi|Kenya|Highland East|EA-M|Highland SE 10kt|Long rains Mar-May|Kenya highland inland|sw|Eke Fire|Leaders traders",
"Addis Ababa ET|Addis Ababa|Ethiopia|Highland Horn|EA-M|Highland Rift SE|Kiremt Jun-Sep Belg Mar-May|Ethiopia highland inland|am|Afo Earth|Leaders herders",
"Kampala UG|Kampala|Uganda|Lake Victoria|Rift|Lake Victoria breeze|2 rains Mar-May Oct-Dec|Uganda Lake Victoria|en|Nkwo Air|Traders fishermen",
"Casablanca MA|Casablanca|Morocco|Med Atlantic-Med convergence|NA-Med|Mediterranean Mistral NW 10kt Atlantic convergence|Med winter rain Oct-Apr summer dry|Morocco Atlantic-Med convergence|ar|Orie Water|Traders fishermen",
"Algiers DZ|Algiers|Algeria|Med|NA-Med|Mistral NW Med 10kt|Med winter rain|Algeria Med|ar|Nkwo Air|Traders",
"Tunis TN|Tunis|Tunisia|Med|NA-Med|Mistral Med 12kt|Med winter rain Oct-Apr|Tunisia Med|ar|Eke Fire|Traders",
"Tripoli LY|Tripoli|Libya|Med Sahara|NA-Med|Ghibli Sirocco S 15kt Med|Med arid winter rain|Libya Med|ar|Orie Water|Traders herders",
"Alexandria EG|Alexandria|Egypt|Med Nile|NA-Med|Etesian NW Med 12kt|Med arid winter rain|Egypt Med|ar|Nkwo Air|Traders fishermen Nile",
"Hurghada EG|Hurghada|Egypt|Red Sea|RedSea|Khamsin N Red Sea 14kt|Arid Red Sea|Egypt Red Sea|ar|Eke Fire|Fishermen divers",
"Port Sudan SD|Port Sudan|Sudan|Red Sea|RedSea|Khamsin Red Sea N 14kt|Arid Red Sea rainy Nov-Jan|Sudan Red Sea|ar|Orie Water|Traders fishermen",
"Cairo EG|Cairo|Egypt|Nile Sahara|NA-Med|Khamsin hot SE 15kt|Desert arid|Egypt Nile inland|ar|Afo Earth|Leaders traders",
"Rabat MA|Rabat|Morocco|Med Atlantic|NA-Med|Atlantic Mistral NW|Med winter rain|Morocco Atlantic|ar|Eke Fire|Leaders",
"Khartoum SD|Khartoum|Sudan|Sahel Nile|WA-S|Harmattan NE dry|Sahel Jul-Sep|Sudan Nile inland|ar|Afo Earth|Herders traders Nile",
"Walvis Bay NA|Walvis Bay|Namibia|South Benguela Desert|SA-B|Benguela SW 18kt desert fog|Desert fog Benguela arid|Namibia|en|Orie Water|Fishermen desert herders",
"Windhoek NA|Windhoek|Namibia|South Benguela Desert|SA-B|Benguela SW 12kt inland|Desert rainy Jan-Apr|Namibia inland|en|Afo Earth|Herders leaders",
"Cape Town ZA|Cape Town|South Africa|South West convergence|SA-B|Cape Doctor SE 20kt SW winter|Winter rain Jun-Aug reverse Med|South Africa West convergence|en|Nkwo Air|Traders fishermen wine",
"Durban ZA|Durban|South Africa|South East Agulhas|SA-A|Agulhas SE 12kt East|Summer rain Nov-Mar|South Africa East Agulhas|en|Orie Water|Traders fishermen",
"Johannesburg ZA|Johannesburg|South Africa|Highveld|SA-A|Highveld SE|Summer rain Oct-Mar|South Africa highveld inland|en|Afo Earth|Leaders miners traders",
"Harare ZW|Harare|Zimbabwe|Highveld|SA-A|SE trade highveld|Summer rain Nov-Mar|Zimbabwe inland|en|Eke Fire|Traders farmers",
"Lusaka ZM|Lusaka|Zambia|Central Plateau|CA|SE trade plateau|Rainy Nov-Apr|Zambia inland|en|Afo Earth|Traders farmers",
"Yaounde CM|Yaounde|Cameroon|Central Forest|CA|Equatorial variable|2 rains Mar-Jun Sep-Nov|Cameroon inland|fr|Nkwo Air|Hunters healers",
"Brazzaville CG|Brazzaville|Congo|Central Congo|CA|Congo Basin variable|Equator 2 rains|Congo River inland|fr|Orie Water|Traders",
]
regs=[]
for l in raw:
    parts=l.split("|")
    regs.append({'code':parts[0],'name':parts[1],'country':parts[2],'zone':parts[3],'zone_code':parts[4],'wind':parts[5],'rain':parts[6],'tide_port':parts[7],'lingua':parts[8],'element':parts[9],'activity':parts[10]})

code='from django.shortcuts import render\nfrom django.http import JsonResponse\nfrom datetime import date\nREGIONS_58=[\n'
for x in regs:
    code+=f' {repr(x)},\n'
code+=''']\nELEMENTS={'EKE':{'element':'Fire','emoji':'\\U0001f525','color':'#ff4500','meaning':'Light New beginnings','advice':'Traders start if preferred'},'ORIE':{'element':'Water','emoji':'\\U0001f4a7','color':'#1e90ff','meaning':'Flow Stability','advice':'Water, fishing best if preferred'},'AFO':{'element':'Earth','emoji':'\\U0001f30d','color':'#8B4513','meaning':'Grounding Harvest','advice':'Earth, harvest if preferred'},'NKWO':{'element':'Air','emoji':'\\U0001f32c','color':'#87ceeb','meaning':'Spirit Reflection','advice':'Air, reflection if preferred'}}\n\ndef get_element_info(market_day):\n return ELEMENTS.get((market_day or 'EKE').upper(), ELEMENTS['EKE'])\n\ndef get_wind_for_region(code):\n for r in REGIONS_58:\n  if r['code']==code:\n   return r\n return REGIONS_58[0]\n\ndef awag_home(request):\n try:\n  from amuzhi_calendar.views import get_today_market_day\n  today_market=get_today_market_day()\n except:\n  today_market=None\n zone=request.GET.get('zone')\n regions_filtered=[r for r in REGIONS_58 if not zone or r['zone_code']==zone or r['zone']==zone] if zone else REGIONS_58\n lang=request.GET.get('lang','en')\n langs=[('en','English'),('fr','French'),('pt','Portuguese'),('sw','Swahili'),('ar','Arabic'),('ig','Igbo')]\n today_element=get_element_info(today_market.market_day if today_market and hasattr(today_market,'market_day') else 'EKE')\n return render(request,'awag/home.html',{'regions_58':regions_filtered,'regions':regions_filtered,'guides':[],'tides':[],'moon_today':None,'today_market':today_market,'today_element':today_element,'elements':ELEMENTS,'lang':lang,'langs':langs,'total_regions':len(REGIONS_58),'zones':sorted(set(r['zone'] for r in REGIONS_58)),'zone_codes':sorted(set(r['zone_code'] for r in REGIONS_58)),'selected_zone':zone,'today':today_market})\n\ndef awag_region(request,code):\n region_dict=get_wind_for_region(code)\n return render(request,'awag/region.html',{'region':region_dict,'region_dict':region_dict,'regions_58':REGIONS_58,'lang':region_dict.get('lingua','en'),'element_info':get_element_info(region_dict.get('element','EKE').split()[0]),'elements':ELEMENTS})\n\ndef awag_tides(request):\n return render(request,'awag/tides.html',{'tides':[],'regions_58':REGIONS_58})\n\ndef awag_tide_table(request):\n return render(request,'awag/tide_table.html',{'tides':[],'ports':[],'selected_port':'Bonny','regions_58':REGIONS_58})\n\ndef awag_farmers(request):\n return render(request,'awag/farmers.html',{'regions_58':REGIONS_58,'guides':[],'lang':'en','zone':None,'week_start':date.today()})\n\ndef api_tides(request):\n return JsonResponse({'port':request.GET.get('port','Bonny'),'tides':[]})\n\ndef api_moon(request,date_str):\n return JsonResponse({'date':date_str,'market_day':'EKE','element':get_element_info('EKE')})\n\ndef api_wind_rain(request):\n zone=request.GET.get('zone')\n data=[r for r in REGIONS_58 if not zone or r['zone_code']==zone] if zone else REGIONS_58\n return JsonResponse({'total':len(data),'regions':data,'elements':ELEMENTS})\n\ndef awag_weekly(request):\n return render(request,'awag/weekly.html',{'week_start':date.today(),'week_end':date.today(),'market_today':'EKE','element':get_element_info('EKE'),'regions_58':REGIONS_58,'zones':sorted(set(r['zone'] for r in REGIONS_58))})\n\ndef awag_view(request):\n return awag_home(request)\n\ndef weekly_guide(request):\n return awag_home(request)\n'''

pathlib.Path("africa_weekly/views.py").write_text(code, encoding="utf-8")
print(f"Wrote {len(regs)} regions - OK")
