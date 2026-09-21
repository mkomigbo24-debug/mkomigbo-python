from django.shortcuts import render
from datetime import date
REGIONS = ['Bight of Biafra','Sahel','Great Lakes','Horn','Southern']
FARMING_TIPS = ['Plant cassava early rains - Eke best','Fish tides: Spring 2 days after new/full moon','Orie best for selling','Harvest yam Onwa Alom Chi']

def weekly_guide(request):
    today=date.today()
    return render(request,'africa_weekly/index.html',{'title':'AWAG - Africa Weekly Guide','today':today,'week':today.isocalendar()[1],'year':today.year,'regions':REGIONS,'tides':{'high':'06:30 & 18:45 2.1m','low':'12:15 & 00:30 0.8m','spring':'Sept 23 New Moon'},'farming':FARMING_TIPS})

def week_view(request,year,week):
    return render(request,'africa_weekly/week.html',{'year':year,'week':week,'title':f'AWAG Week {week}'})

def today_guide(request):
    return weekly_guide(request)

def tides_view(request):
    return render(request,'africa_weekly/tides.html',{'title':'AWAG Tides - Bight of Biafra','today':date.today(),'tides':{'high':'06:30 & 18:45 2.1m Spring','low':'12:15 & 00:30 0.8m','spring':'Sept 23 New Moon - Onwa Mbu'}})

def farming_view(request):
    return render(request,'africa_weekly/farming.html',{'title':'AWAG Farming','tips':FARMING_TIPS})

def regions_view(request):
    return render(request,'africa_weekly/regions.html',{'title':'AWAG Regions','regions':REGIONS})
