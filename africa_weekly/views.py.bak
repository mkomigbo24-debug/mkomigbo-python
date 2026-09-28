from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
REGIONS_58=[
 {'code': 'Bonny NG', 'name': 'Bonny', 'country': 'Nigeria', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan NE Dry 15kt', 'rain': 'Guinea 2 seasons Rain Apr-Jul', 'tide_port': 'Niger Delta Bonny Opobo Brass', 'lingua': 'en', 'element': 'Afo Earth', 'activity': 'Traders fishermen oil'},
 {'code': 'Lagos NG', 'name': 'Lagos', 'country': 'Nigeria', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan NE Dry 12kt', 'rain': 'Guinea 2 seasons Apr-Jul Oct', 'tide_port': 'Lagos-Bar beach', 'lingua': 'en', 'element': 'Eke Fire', 'activity': 'Traders transporters'},
 {'code': 'Baga NG', 'name': 'Baga', 'country': 'Nigeria', 'zone': 'Lake Chad', 'zone_code': 'WA-LC', 'wind': 'Harmattan NE Dry 18kt dusty', 'rain': 'Sahel dry Lake Chad shrink', 'tide_port': 'Baga Lake Chad inland', 'lingua': 'en', 'element': 'Afo Earth', 'activity': 'Herders fishermen lake'},
 {'code': 'Tema GH', 'name': 'Tema', 'country': 'Ghana', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW 10kt', 'rain': 'Guinea 2 seasons Apr-Jul Sep-Oct', 'tide_port': 'Ghana Elmina', 'lingua': 'en', 'element': 'Orie Water', 'activity': 'Traders fishermen'},
 {'code': 'Accra GH', 'name': 'Accra', 'country': 'Ghana', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW 10kt', 'rain': 'Guinea 2 seasons Apr-Jul', 'tide_port': 'Accra', 'lingua': 'en', 'element': 'Nkwo Air', 'activity': 'Traders fishermen'},
 {'code': 'Abidjan CI', 'name': 'Abidjan', 'country': 'Ivory Coast', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW 8kt', 'rain': 'Guinea heavy Apr-Jul', 'tide_port': 'Ivory Coast lagoon', 'lingua': 'fr', 'element': 'Nkwo Air', 'activity': 'Traders hunters'},
 {'code': 'Dakar SN', 'name': 'Dakar', 'country': 'Senegal', 'zone': 'Sahel Atlantic', 'zone_code': 'WA-S', 'wind': 'Harmattan NE Dry 15kt upwelling', 'rain': 'Sahel rainy Jun-Oct', 'tide_port': 'Senegal upwelling', 'lingua': 'fr', 'element': 'Eke Fire', 'activity': 'Herders fishermen'},
 {'code': 'Banjul GM', 'name': 'Banjul', 'country': 'Gambia', 'zone': 'Sahel Atlantic', 'zone_code': 'WA-S', 'wind': 'Harmattan NE 12kt', 'rain': 'Sahel Jun-Oct', 'tide_port': 'Gambia River', 'lingua': 'en', 'element': 'Orie Water', 'activity': 'Traders fishermen'},
 {'code': 'Bissau GW', 'name': 'Bissau', 'country': 'Guinea-Bissau', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan 12kt Bijagos', 'rain': 'Guinea rainy May-Nov', 'tide_port': 'Guinea-Bissau Bijagos', 'lingua': 'pt', 'element': 'Nkwo Air', 'activity': 'Traders fishermen islands'},
 {'code': 'Conakry GN', 'name': 'Conakry', 'country': 'Guinea', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan 10kt', 'rain': 'Guinea heavy May-Oct', 'tide_port': 'Guinea Conakry', 'lingua': 'fr', 'element': 'Eke Fire', 'activity': 'Traders miners'},
 {'code': 'Freetown SL', 'name': 'Freetown', 'country': 'Sierra Leone', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW', 'rain': 'Guinea heavy May-Oct', 'tide_port': 'Sierra Leone', 'lingua': 'en', 'element': 'Afo Earth', 'activity': 'Traders fishermen'},
 {'code': 'Monrovia LR', 'name': 'Monrovia', 'country': 'Liberia', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW', 'rain': 'Guinea rainy Apr-Oct', 'tide_port': 'Liberia', 'lingua': 'en', 'element': 'Nkwo Air', 'activity': 'Traders rubber'},
 {'code': 'Cotonou BJ', 'name': 'Cotonou', 'country': 'Benin', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW 10kt', 'rain': 'Guinea 2 seasons', 'tide_port': 'Benin', 'lingua': 'fr', 'element': 'Orie Water', 'activity': 'Traders fishermen'},
 {'code': 'Lome TG', 'name': 'Lome', 'country': 'Togo', 'zone': 'Guinea', 'zone_code': 'WA-G', 'wind': 'Harmattan SW', 'rain': 'Guinea 2 seasons', 'tide_port': 'Togo', 'lingua': 'fr', 'element': 'Eke Fire', 'activity': 'Traders'},
 {'code': 'Douala CM', 'name': 'Douala', 'country': 'Cameroon', 'zone': 'Central Guinea', 'zone_code': 'CA-G', 'wind': 'Harmattan 8kt equatorial', 'rain': 'Guinea heavy Mar-Oct', 'tide_port': 'Cameroon', 'lingua': 'fr', 'element': 'Orie Water', 'activity': 'Traders hunters oil'},
 {'code': 'Libreville GA', 'name': 'Libreville', 'country': 'Gabon', 'zone': 'Central', 'zone_code': 'CA', 'wind': 'Equatorial SW 8kt', 'rain': 'Equator rain year round', 'tide_port': 'Gabon', 'lingua': 'fr', 'element': 'Nkwo Air', 'activity': 'Hunters oil'},
 {'code': 'Pointe-Noire CG', 'name': 'Pointe-Noire', 'country': 'Congo', 'zone': 'Central', 'zone_code': 'CA', 'wind': 'Benguela edge SW 10kt', 'rain': 'Equator 2 rains', 'tide_port': 'Congo', 'lingua': 'fr', 'element': 'Afo Earth', 'activity': 'Traders oil'},
 {'code': 'Mopti ML', 'name': 'Mopti', 'country': 'Mali', 'zone': 'Sahel Inner Delta', 'zone_code': 'WA-S', 'wind': 'Harmattan NE Dry 20kt dusty', 'rain': 'Sahel Jun-Sep Niger Inner Delta', 'tide_port': 'Mali Niger Inner Delta', 'lingua': 'fr', 'element': 'Afo Earth', 'activity': 'Herders fishermen herders'},
 {'code': 'Nouakchott MR', 'name': 'Nouakchott', 'country': 'Mauritania', 'zone': 'Sahel Atlantic', 'zone_code': 'WA-S', 'wind': 'Harmattan NE 18kt Banc dArguin', 'rain': 'Sahel arid Jun-Oct', 'tide_port': 'Mauritania Banc dArguin', 'lingua': 'fr', 'element': 'Eke Fire', 'activity': 'Herders fishermen'},
 {'code': 'Luanda AO', 'name': 'Luanda', 'country': 'Angola', 'zone': 'South Benguela', 'zone_code': 'SA-B', 'wind': 'Benguela SW 12kt North', 'rain': 'South rainy Nov-Apr', 'tide_port': 'Angola North', 'lingua': 'pt', 'element': 'Orie Water', 'activity': 'Traders oil fishermen'},
 {'code': 'Namibe AO', 'name': 'Namibe', 'country': 'Angola', 'zone': 'South Benguela Desert', 'zone_code': 'SA-B', 'wind': 'Benguela SW 18kt desert', 'rain': 'Desert arid Benguela fog', 'tide_port': 'Angola South Benguela', 'lingua': 'pt', 'element': 'Eke Fire', 'activity': 'Herders fishermen desert'},
 {'code': 'Kinshasa CD', 'name': 'Kinshasa', 'country': 'DR Congo', 'zone': 'Central Congo', 'zone_code': 'CA', 'wind': 'Congo Basin variable', 'rain': 'Equator rain year', 'tide_port': 'Congo River inland', 'lingua': 'fr', 'element': 'Nkwo Air', 'activity': 'Traders healers leaders'},
 {'code': 'Kalemie CD', 'name': 'Kalemie', 'country': 'DR Congo', 'zone': 'Rift Tanganyika', 'zone_code': 'Rift', 'wind': 'Lake Tanganyika breeze 8kt', 'rain': 'Rift short rains Oct-Dec long Mar-May', 'tide_port': 'DR Congo Tanganyika', 'lingua': 'fr', 'element': 'Orie Water', 'activity': 'Fishermen lake'},
 {'code': 'Kigoma TZ', 'name': 'Kigoma', 'country': 'Tanzania', 'zone': 'Rift Tanganyika', 'zone_code': 'Rift', 'wind': 'Lake Tanganyika breeze', 'rain': 'Rift 2 seasons', 'tide_port': 'Lake Tanganyika', 'lingua': 'sw', 'element': 'Nkwo Air', 'activity': 'Fishermen traders'},
 {'code': 'Mombasa KE', 'name': 'Mombasa', 'country': 'Kenya', 'zone': 'East Monsoon', 'zone_code': 'EA-M', 'wind': 'Monsoon Kusi SE 12kt Kaskazi NE Dec-Mar', 'rain': 'Long rains Mar-May short Oct-Dec', 'tide_port': 'Kenya Swahili coast', 'lingua': 'sw', 'element': 'Afo Earth', 'activity': 'Traders fishermen Swahili'},
 {'code': 'Kisumu KE', 'name': 'Kisumu', 'country': 'Kenya', 'zone': 'Lake Victoria', 'zone_code': 'Rift', 'wind': 'Lake Victoria breeze 10kt Winam Gulf', 'rain': 'Lake Victoria long Mar-May', 'tide_port': 'Lake Victoria Winam Gulf', 'lingua': 'sw', 'element': 'Orie Water', 'activity': 'Fishermen lake traders'},
 {'code': 'Turkana KE', 'name': 'Turkana', 'country': 'Kenya', 'zone': 'Rift Desert Lake', 'zone_code': 'Rift', 'wind': 'Turkana Jet SE 20kt desert', 'rain': 'Desert arid Rift', 'tide_port': 'Lake Turkana Rudolf desert lake', 'lingua': 'sw', 'element': 'Eke Fire', 'activity': 'Herders fishermen desert'},
 {'code': 'Mwanza TZ', 'name': 'Mwanza', 'country': 'Tanzania', 'zone': 'Lake Victoria', 'zone_code': 'Rift', 'wind': 'Lake Victoria breeze', 'rain': 'Long rains Mar-May', 'tide_port': 'Lake Victoria Tanzania', 'lingua': 'sw', 'element': 'Afo Earth', 'activity': 'Fishermen'},
 {'code': 'Dar es Salaam TZ', 'name': 'Dar es Salaam', 'country': 'Tanzania', 'zone': 'East Monsoon', 'zone_code': 'EA-M', 'wind': 'Monsoon Kusi SE 12kt', 'rain': 'Long rains Mar-May', 'tide_port': 'Tanzania Dar', 'lingua': 'sw', 'element': 'Orie Water', 'activity': 'Traders port'},
 {'code': 'Zanzibar TZ', 'name': 'Zanzibar', 'country': 'Tanzania', 'zone': 'East Monsoon Islands', 'zone_code': 'EA-M', 'wind': 'Monsoon Kusi SE 15kt spice', 'rain': 'Long rains Mar-May', 'tide_port': 'Zanzibar spice', 'lingua': 'sw', 'element': 'Nkwo Air', 'activity': 'Traders spice fishermen'},
 {'code': 'Mogadishu SO', 'name': 'Mogadishu', 'country': 'Somalia', 'zone': 'East Monsoon Horn', 'zone_code': 'EA-M', 'wind': 'Monsoon Kaskazi NE 15kt longest coast', 'rain': 'Arid 2 rains Gu Deyr', 'tide_port': 'Somalia longest coast', 'lingua': 'ar', 'element': 'Eke Fire', 'activity': 'Herders fishermen pastoral'},
 {'code': 'Djibouti DJ', 'name': 'Djibouti', 'country': 'Djibouti', 'zone': 'Red Sea Rift', 'zone_code': 'RedSea', 'wind': 'Khamsin Red Sea N 14kt', 'rain': 'Arid Red Sea', 'tide_port': 'Djibouti Red Sea', 'lingua': 'fr', 'element': 'Eke Fire', 'activity': 'Traders port'},
 {'code': 'Beira MZ', 'name': 'Beira', 'country': 'Mozambique', 'zone': 'South East Monsoon', 'zone_code': 'SE-M', 'wind': 'Monsoon SE Sofala 12kt', 'rain': 'Cyclone season Nov-Apr rainy', 'tide_port': 'Mozambique North Sofala', 'lingua': 'pt', 'element': 'Orie Water', 'activity': 'Traders fishermen cyclone'},
 {'code': 'Maputo MZ', 'name': 'Maputo', 'country': 'Mozambique', 'zone': 'South East', 'zone_code': 'SE-M', 'wind': 'Monsoon SE South 10kt', 'rain': 'Rainy Nov-Mar dry winter', 'tide_port': 'Mozambique South', 'lingua': 'pt', 'element': 'Afo Earth', 'activity': 'Traders'},
 {'code': 'Mahajanga MG', 'name': 'Mahajanga', 'country': 'Madagascar', 'zone': 'Indian Ocean Island', 'zone_code': 'Island', 'wind': 'Monsoon NW Madagascar 12kt', 'rain': 'Cyclone Nov-Apr rainy', 'tide_port': 'Madagascar Madagasy', 'lingua': 'fr', 'element': 'Nkwo Air', 'activity': 'Fishermen traders island'},
 {'code': 'Antananarivo MG', 'name': 'Antananarivo', 'country': 'Madagascar', 'zone': 'Highland Island', 'zone_code': 'Island', 'wind': 'Highland trade SE', 'rain': 'Highland rainy Nov-Apr', 'tide_port': 'Madagascar highland inland', 'lingua': 'fr', 'element': 'Afo Earth', 'activity': 'Healers traders rice'},
 {'code': 'Nairobi KE', 'name': 'Nairobi', 'country': 'Kenya', 'zone': 'Highland East', 'zone_code': 'EA-M', 'wind': 'Highland SE 10kt', 'rain': 'Long rains Mar-May', 'tide_port': 'Kenya highland inland', 'lingua': 'sw', 'element': 'Eke Fire', 'activity': 'Leaders traders'},
 {'code': 'Addis Ababa ET', 'name': 'Addis Ababa', 'country': 'Ethiopia', 'zone': 'Highland Horn', 'zone_code': 'EA-M', 'wind': 'Highland Rift SE', 'rain': 'Kiremt Jun-Sep Belg Mar-May', 'tide_port': 'Ethiopia highland inland', 'lingua': 'am', 'element': 'Afo Earth', 'activity': 'Leaders herders'},
 {'code': 'Kampala UG', 'name': 'Kampala', 'country': 'Uganda', 'zone': 'Lake Victoria', 'zone_code': 'Rift', 'wind': 'Lake Victoria breeze', 'rain': '2 rains Mar-May Oct-Dec', 'tide_port': 'Uganda Lake Victoria', 'lingua': 'en', 'element': 'Nkwo Air', 'activity': 'Traders fishermen'},
 {'code': 'Casablanca MA', 'name': 'Casablanca', 'country': 'Morocco', 'zone': 'Med Atlantic-Med convergence', 'zone_code': 'NA-Med', 'wind': 'Mediterranean Mistral NW 10kt Atlantic convergence', 'rain': 'Med winter rain Oct-Apr summer dry', 'tide_port': 'Morocco Atlantic-Med convergence', 'lingua': 'ar', 'element': 'Orie Water', 'activity': 'Traders fishermen'},
 {'code': 'Algiers DZ', 'name': 'Algiers', 'country': 'Algeria', 'zone': 'Med', 'zone_code': 'NA-Med', 'wind': 'Mistral NW Med 10kt', 'rain': 'Med winter rain', 'tide_port': 'Algeria Med', 'lingua': 'ar', 'element': 'Nkwo Air', 'activity': 'Traders'},
 {'code': 'Tunis TN', 'name': 'Tunis', 'country': 'Tunisia', 'zone': 'Med', 'zone_code': 'NA-Med', 'wind': 'Mistral Med 12kt', 'rain': 'Med winter rain Oct-Apr', 'tide_port': 'Tunisia Med', 'lingua': 'ar', 'element': 'Eke Fire', 'activity': 'Traders'},
 {'code': 'Tripoli LY', 'name': 'Tripoli', 'country': 'Libya', 'zone': 'Med Sahara', 'zone_code': 'NA-Med', 'wind': 'Ghibli Sirocco S 15kt Med', 'rain': 'Med arid winter rain', 'tide_port': 'Libya Med', 'lingua': 'ar', 'element': 'Orie Water', 'activity': 'Traders herders'},
 {'code': 'Alexandria EG', 'name': 'Alexandria', 'country': 'Egypt', 'zone': 'Med Nile', 'zone_code': 'NA-Med', 'wind': 'Etesian NW Med 12kt', 'rain': 'Med arid winter rain', 'tide_port': 'Egypt Med', 'lingua': 'ar', 'element': 'Nkwo Air', 'activity': 'Traders fishermen Nile'},
 {'code': 'Hurghada EG', 'name': 'Hurghada', 'country': 'Egypt', 'zone': 'Red Sea', 'zone_code': 'RedSea', 'wind': 'Khamsin N Red Sea 14kt', 'rain': 'Arid Red Sea', 'tide_port': 'Egypt Red Sea', 'lingua': 'ar', 'element': 'Eke Fire', 'activity': 'Fishermen divers'},
 {'code': 'Port Sudan SD', 'name': 'Port Sudan', 'country': 'Sudan', 'zone': 'Red Sea', 'zone_code': 'RedSea', 'wind': 'Khamsin Red Sea N 14kt', 'rain': 'Arid Red Sea rainy Nov-Jan', 'tide_port': 'Sudan Red Sea', 'lingua': 'ar', 'element': 'Orie Water', 'activity': 'Traders fishermen'},
 {'code': 'Cairo EG', 'name': 'Cairo', 'country': 'Egypt', 'zone': 'Nile Sahara', 'zone_code': 'NA-Med', 'wind': 'Khamsin hot SE 15kt', 'rain': 'Desert arid', 'tide_port': 'Egypt Nile inland', 'lingua': 'ar', 'element': 'Afo Earth', 'activity': 'Leaders traders'},
 {'code': 'Rabat MA', 'name': 'Rabat', 'country': 'Morocco', 'zone': 'Med Atlantic', 'zone_code': 'NA-Med', 'wind': 'Atlantic Mistral NW', 'rain': 'Med winter rain', 'tide_port': 'Morocco Atlantic', 'lingua': 'ar', 'element': 'Eke Fire', 'activity': 'Leaders'},
 {'code': 'Khartoum SD', 'name': 'Khartoum', 'country': 'Sudan', 'zone': 'Sahel Nile', 'zone_code': 'WA-S', 'wind': 'Harmattan NE dry', 'rain': 'Sahel Jul-Sep', 'tide_port': 'Sudan Nile inland', 'lingua': 'ar', 'element': 'Afo Earth', 'activity': 'Herders traders Nile'},
 {'code': 'Walvis Bay NA', 'name': 'Walvis Bay', 'country': 'Namibia', 'zone': 'South Benguela Desert', 'zone_code': 'SA-B', 'wind': 'Benguela SW 18kt desert fog', 'rain': 'Desert fog Benguela arid', 'tide_port': 'Namibia', 'lingua': 'en', 'element': 'Orie Water', 'activity': 'Fishermen desert herders'},
 {'code': 'Windhoek NA', 'name': 'Windhoek', 'country': 'Namibia', 'zone': 'South Benguela Desert', 'zone_code': 'SA-B', 'wind': 'Benguela SW 12kt inland', 'rain': 'Desert rainy Jan-Apr', 'tide_port': 'Namibia inland', 'lingua': 'en', 'element': 'Afo Earth', 'activity': 'Herders leaders'},
 {'code': 'Cape Town ZA', 'name': 'Cape Town', 'country': 'South Africa', 'zone': 'South West convergence', 'zone_code': 'SA-B', 'wind': 'Cape Doctor SE 20kt SW winter', 'rain': 'Winter rain Jun-Aug reverse Med', 'tide_port': 'South Africa West convergence', 'lingua': 'en', 'element': 'Nkwo Air', 'activity': 'Traders fishermen wine'},
 {'code': 'Durban ZA', 'name': 'Durban', 'country': 'South Africa', 'zone': 'South East Agulhas', 'zone_code': 'SA-A', 'wind': 'Agulhas SE 12kt East', 'rain': 'Summer rain Nov-Mar', 'tide_port': 'South Africa East Agulhas', 'lingua': 'en', 'element': 'Orie Water', 'activity': 'Traders fishermen'},
 {'code': 'Johannesburg ZA', 'name': 'Johannesburg', 'country': 'South Africa', 'zone': 'Highveld', 'zone_code': 'SA-A', 'wind': 'Highveld SE', 'rain': 'Summer rain Oct-Mar', 'tide_port': 'South Africa highveld inland', 'lingua': 'en', 'element': 'Afo Earth', 'activity': 'Leaders miners traders'},
 {'code': 'Harare ZW', 'name': 'Harare', 'country': 'Zimbabwe', 'zone': 'Highveld', 'zone_code': 'SA-A', 'wind': 'SE trade highveld', 'rain': 'Summer rain Nov-Mar', 'tide_port': 'Zimbabwe inland', 'lingua': 'en', 'element': 'Eke Fire', 'activity': 'Traders farmers'},
 {'code': 'Lusaka ZM', 'name': 'Lusaka', 'country': 'Zambia', 'zone': 'Central Plateau', 'zone_code': 'CA', 'wind': 'SE trade plateau', 'rain': 'Rainy Nov-Apr', 'tide_port': 'Zambia inland', 'lingua': 'en', 'element': 'Afo Earth', 'activity': 'Traders farmers'},
 {'code': 'Yaounde CM', 'name': 'Yaounde', 'country': 'Cameroon', 'zone': 'Central Forest', 'zone_code': 'CA', 'wind': 'Equatorial variable', 'rain': '2 rains Mar-Jun Sep-Nov', 'tide_port': 'Cameroon inland', 'lingua': 'fr', 'element': 'Nkwo Air', 'activity': 'Hunters healers'},
 {'code': 'Brazzaville CG', 'name': 'Brazzaville', 'country': 'Congo', 'zone': 'Central Congo', 'zone_code': 'CA', 'wind': 'Congo Basin variable', 'rain': 'Equator 2 rains', 'tide_port': 'Congo River inland', 'lingua': 'fr', 'element': 'Orie Water', 'activity': 'Traders'},
]
ELEMENTS={'EKE':{'element':'Fire','emoji':'\U0001f525','color':'#ff4500','meaning':'Light New beginnings','advice':'Traders start if preferred'},'ORIE':{'element':'Water','emoji':'\U0001f4a7','color':'#1e90ff','meaning':'Flow Stability','advice':'Water, fishing best if preferred'},'AFO':{'element':'Earth','emoji':'\U0001f30d','color':'#8B4513','meaning':'Grounding Harvest','advice':'Earth, harvest if preferred'},'NKWO':{'element':'Air','emoji':'\U0001f32c','color':'#87ceeb','meaning':'Spirit Reflection','advice':'Air, reflection if preferred'}}

def get_element_info(market_day):
 return ELEMENTS.get((market_day or 'EKE').upper(), ELEMENTS['EKE'])

def get_wind_for_region(code):
 for r in REGIONS_58:
  if r['code']==code:
   return r
 return REGIONS_58[0]

def awag_home(request):
 try:
  from amuzhi_calendar.views import get_today_market_day
  today_market=get_today_market_day()
 except:
  today_market=None
 zone=request.GET.get('zone')
 regions_filtered=[r for r in REGIONS_58 if not zone or r['zone_code']==zone or r['zone']==zone] if zone else REGIONS_58
 lang=request.GET.get('lang','en')
 langs=[('en','English'),('fr','French'),('pt','Portuguese'),('sw','Swahili'),('ar','Arabic'),('ig','Igbo')]
 today_element=get_element_info(today_market.market_day if today_market and hasattr(today_market,'market_day') else 'EKE')
 return render(request,'awag/home.html',{'regions_58':regions_filtered,'regions':regions_filtered,'guides':[],'tides':[],'moon_today':None,'today_market':today_market,'today_element':today_element,'elements':ELEMENTS,'lang':lang,'langs':langs,'total_regions':len(REGIONS_58),'zones':sorted(set(r['zone'] for r in REGIONS_58)),'zone_codes':sorted(set(r['zone_code'] for r in REGIONS_58)),'selected_zone':zone,'today':today_market})

def awag_region(request,code):
 region_dict=get_wind_for_region(code)
 return render(request,'awag/region.html',{'region':region_dict,'region_dict':region_dict,'regions_58':REGIONS_58,'lang':region_dict.get('lingua','en'),'element_info':get_element_info(region_dict.get('element','EKE').split()[0]),'elements':ELEMENTS})

def awag_tides(request):
 return render(request,'awag/tides.html',{'tides':[],'regions_58':REGIONS_58})

def awag_tide_table(request):
 return render(request,'awag/tide_table.html',{'tides':[],'ports':[],'selected_port':'Bonny','regions_58':REGIONS_58})

def awag_farmers(request):
 return render(request,'awag/farmers.html',{'regions_58':REGIONS_58,'guides':[],'lang':'en','zone':None,'week_start':date.today()})

def api_tides(request):
 return JsonResponse({'port':request.GET.get('port','Bonny'),'tides':[]})

def api_moon(request,date_str):
 return JsonResponse({'date':date_str,'market_day':'EKE','element':get_element_info('EKE')})

def api_wind_rain(request):
 zone=request.GET.get('zone')
 data=[r for r in REGIONS_58 if not zone or r['zone_code']==zone] if zone else REGIONS_58
 return JsonResponse({'total':len(data),'regions':data,'elements':ELEMENTS})

def awag_weekly(request):
 return render(request,'awag/weekly.html',{'week_start':date.today(),'week_end':date.today(),'market_today':'EKE','element':get_element_info('EKE'),'regions_58':REGIONS_58,'zones':sorted(set(r['zone'] for r in REGIONS_58))})

def awag_view(request):
 return awag_home(request)

def weekly_guide(request):
 return awag_home(request)
