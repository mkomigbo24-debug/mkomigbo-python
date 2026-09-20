from django.core.management.base import BaseCommand
from datetime import date, timedelta
from awag.models import WeeklyGuide, Region
from awag.views import REGIONS_58, ELEMENTS
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Try get Amuzhi MarketDay for moon + element
        try:
            from amuzhi_calendar.models import MarketDay
            from amuzhi_calendar.views import get_today_market_day
            has_amuzhi = True
        except:
            has_amuzhi = False
            MarketDay = None

        today = date.today()
        monday = today - timedelta(days=today.weekday())

        # 12 weeks ahead - predictable
        for week_offset in range(12):
            week_start = monday + timedelta(weeks=week_offset)
            week_end = week_start + timedelta(days=6)

            # Moon phase for week - from Amuzhi if available
            if has_amuzhi:
                md = MarketDay.objects.filter(date_gregorian=week_start).first()
                if md:
                    moon_symbol = md.moon_symbol
                    moon_stage = md.moon_stage
                    illum = md.illumination
                    market = md.market_day
                else:
                    # fallback
                    moon_symbol = "🌒"
                    moon_stage = "Waxing Crescent"
                    illum = 32
                    market = ["EKE","ORIE","AFO","NKWO"][week_offset % 4]
            else:
                moon_symbol = "🌒"
                moon_stage = "Waxing Crescent"
                illum = 32
                market = ["EKE","ORIE","AFO","NKWO"][week_offset % 4]

            element = ELEMENTS.get(market, ELEMENTS['EKE'])

            for r_dict in REGIONS_58:
                # Find or create Region DB
                region, _ = Region.objects.get_or_create(
                    code=r_dict['code'],
                    defaults={'name_en':r_dict['name'],'lingua_franca':r_dict['lingua']}
                )

                # Farmers logic by rain locality
                rain = r_dict['rain'].lower()
                wind = r_dict['wind']
                if 'sahel' in rain and 'lake chad' in r_dict['tide_port'].lower():
                    planting = f"Sahel dry Lake Chad shrink {wind} - Soil too dry - Early rain expected late Jun if Kaskazi shifts, Late rain late Jul. Plant millet/sorghum/cowpea early {week_start.strftime('%b %d')} if soil optimal, else wait. Harvest fish when lake high 3.2m. Market {market} {element['emoji']} {element['element']}."
                elif 'guinea' in rain:
                    planting = f"Guinea 2 seasons {rain} - {wind} - Soil {'optimal' if 'Apr-Jul' in r_dict['rain'] else 'wet'} - Early rain Apr-Jul, Late Sep-Oct. Plant yam/cassava/maize early Apr if early rain, late Apr if late rain. Harvest Oct. Sell {market} {element['element']} day market rhythm Eke→Orie→Afo→Nkwo."
                elif 'long rains' in rain:
                    planting = f"Long rains Mar-May short Oct-Dec Monsoon {wind} - Soil wet - Plant maize/beans/sorghum Mar. Kusi SE 12kt. Harvest Jul. Transporters move when dry. Market {market}."
                elif 'med winter' in rain or 'med' in rain:
                    planting = f"Med winter rain Oct-Apr summer dry {wind} Mistral NW - Soil dry summer - Plant wheat/barley/olive Oct-Nov early rain, Dec late rain. Harvest Jun. Traders {market}."
                elif 'summer rain' in rain or 'rainy nov' in rain:
                    planting = f"Summer rain Nov-Mar Agulhas/Benguela {wind} - Soil optimal Nov - Plant maize/sunflower Nov early rain, Dec late rain. Cyclone season Nov-Apr caution. Harvest Apr."
                else:
                    planting = f"{r_dict['zone']} {rain} {wind} - Planting by moon {moon_symbol} {moon_stage} {illum}% {market} {element['emoji']} - Farmers reliable info whole Africa."

                # Fishermen logic by tide + moon
                tide_port = r_dict['tide_port']
                fishermen = f"Moon {moon_symbol} {moon_stage} {illum}% {market} {element['element']} - Tide {tide_port} - High tide best fishing {element['advice']} - {market}: {ELEMENTS[market]['advice'] if market in ELEMENTS else ''} - Preserve dried/smoked sell {['AFO Earth market day sell','ORIE Water stability','EKE Fire new beginnings','NKWO Air preservation'][['EKE','ORIE','AFO','NKWO'].index(market) if market in ['EKE','ORIE','AFO','NKWO'] else 0]}."

                # Transporters + Traders + Healers + Leaders
                transporters = f"Rain pattern {r_dict['rain']} - Wind {wind} - Predictable: Move goods when dry - Harmattan dusty visibility low, Monsoon Kusi SE 12kt transporters wait, Benguela fog. Equator reverse climate North dry South wet."
                traders = f"Traders {r_dict['activity']} - Market rhythm Eke→Orie→Afo→Nkwo 4-day Igbo week - {market} prominence Week {week_start.isocalendar()[1]} - Element {element['element']} {element['emoji']} - Economic predictable."
                hunters = f"Hunters {r_dict['zone']} - Equatorial forest vs savanna - Moon {moon_stage} hunting best waning - Healers herbs by moon {moon_stage} - Traditional healers leaves roots moon influence."
                leaders = f"Leaders {r_dict['activity']} - Leaders economic activities predictable - Weekly guide serving 2B in Lingua Franca {r_dict['lingua']} - Amuzhi 13 months Igbo calendar anchor Afo - Gregorian {week_start.year}."

                # Create weekly guide - 7 languages later
                for lang in [r_dict['lingua'], 'en']:
                    WeeklyGuide.objects.update_or_create(
                        region=region, week_start=week_start, language=lang,
                        defaults={
                            'week_end': week_end,
                            'moon_phase_week': f"{moon_symbol} {moon_stage} {illum}% - {market} {element['element']} - Week {week_start.isocalendar()[1]}/52 Greg 38/52 weeks",
                            'farmers_planting_en': planting,
                            'fishermen_moon_tide_en': fishermen,
                            'transporters_rain_pattern': transporters,
                            'traders_advice': traders,
                            'hunters_advice': hunters,
                            'healers_advice': f"Healers - Moon {moon_stage} - Herbs harvest {market} day - {element['meaning']}",
                            'leaders_advice': leaders,
                        }
                    )

        count = WeeklyGuide.objects.count()
        self.stdout.write(self.style.SUCCESS(f'AWAG Auto Weekly Guide generated - {count} guides - 12 weeks x 58 regions - Farmers early/late rain + Fishermen moon+tide + Transporters rain predictable - Serving 2B!'))