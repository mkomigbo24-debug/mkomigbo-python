"""
AWAG Moon Phase Engine - For fishing, farming, healing, trading
Calculates moon phase + Igbo market day guidance
Add this to africa_weekly/views.py
"""
from datetime import datetime, timedelta
import math

# Known new moon: 2024-01-11 11:57 UTC - reference
KNOWN_NEW_MOON = datetime(2024, 1, 11, 11, 57)
LUNAR_CYCLE = 29.53058867

PHASES = [
    (0, 1, "New Moon - Ọnwa Ọhụrụ", "🌑", "Dark - Rest if preferred", {"fishing": "Low - Rest nets", "farming": "Rest soil - Eke planning", "healing": "Cleansing, Nkwo Air - Spirit reflection"}),
    (1, 6.5, "Waxing Crescent - Ọnwa na-eto eto", "🌒", "Growing light - Start if preferred", {"fishing": "Improving - Orie Water", "farming": "Plant leafy - Eke Fire new beginnings", "healing": "New herbs - Afo Earth"}),
    (6.5, 8.5, "First Quarter - Ọnwa Nkera mbu", "🌓", "Half light - Build if preferred", {"fishing": "Good - Tide rising", "farming": "Plant fruits - Nkwo Air", "healing": "Strength building - Eke Fire"}),
    (8.5, 13.5, "Waxing Gibbous - Ọnwa na-achawanye", "🌔", "Brightening - Nurture if preferred", {"fishing": "Very Good - Orie Water high", "farming": "Fertilize - Orie Water irrigation", "healing": "Gather leaves - Orie Water"}),
    (13.5, 16.5, "Full Moon - Ọnwa zuru oke", "🌕", "Full light - Harvest if preferred", {"fishing": "Best - Full tide - Bonny, Mombasa peak", "farming": "Harvest - Afo Earth grounding", "healing": "Powerful - Full potency - Afo Earth"}),
    (16.5, 21.5, "Waning Gibbous - Ọnwa na-ebelata", "🌖", "Fading light - Share if preferred", {"fishing": "Good - Still high", "farming": "Harvest roots - Afo Earth", "healing": "Dry herbs - Eke Fire drying"}),
    (21.5, 23.5, "Last Quarter - Ọnwa Nkera ikpeazu", "🌗", "Half dark - Release if preferred", {"fishing": "Moderate - Lower tide", "farming": "Weed, prune - Nkwo Air planning", "healing": "Release, cleanse - Nkwo Air"}),
    (23.5, 29.54, "Waning Crescent - Ọnwa na-ala", "🌘", "Dim - Rest if preferred", {"fishing": "Low - Rest - Prepare nets", "farming": "Rest soil - Afo Earth rest", "healing": "Rest - Grounding - Afo Earth"}),
]

IGBO_DAYS = {
    "EKE": {"element": "Fire 🔥", "meaning": "Light New beginnings", "good_for": "Planting, traders start if preferred, traders, new markets"},
    "ORIE": {"element": "Water 💧", "meaning": "Flow Stability", "good_for": "Fishing, irrigation, fishermen, Orie Water days best for fishing"},
    "AFO": {"element": "Earth 🌍", "meaning": "Grounding Harvest", "good_for": "Harvest, healers, Afo Earth harvest and healing"},
    "NKWO": {"element": "Air 🌬️", "meaning": "Spirit Reflection", "good_for": "Planning, reflection, Nkwo Air spirit, markets"},
}

def get_moon_phase(date=None):
    if date is None:
        date = datetime.now()
    # days since known new moon
    delta = date - KNOWN_NEW_MOON
    days = delta.total_seconds() / 86400
    # normalize to cycle
    phase_age = days % LUNAR_CYCLE
    illumination = (1 - math.cos(2 * math.pi * phase_age / LUNAR_CYCLE)) / 2 * 100
    
    for start, end, name, emoji, desc, guidance in PHASES:
        if start <= phase_age < end:
            return {
                "age": round(phase_age,1),
                "name": name,
                "emoji": emoji,
                "description": desc,
                "illumination": round(illumination),
                "guidance": guidance,
                "days_until_full": round((13.5 - phase_age) % LUNAR_CYCLE,1)
            }
    # fallback
    return {"age": phase_age, "name": "Waxing", "emoji": "🌙", "description": "", "illumination": round(illumination), "guidance": {}, "days_until_full": 0}

def get_weekly_moon_phases(start_date=None):
    if start_date is None:
        start_date = datetime.now()
    week = []
    for i in range(14):  # 2 weeks for farming/fishing planning
        d = start_date + timedelta(days=i)
        mp = get_moon_phase(d)
        # Igbo day cycle: Eke, Orie, Afo, Nkwo rotating
        igbo_cycle = ["EKE", "ORIE", "AFO", "NKWO"]
        # Use known reference: 2024-01-01 was EKE
        ref = datetime(2024,1,1)
        diff = (d.date() - ref.date()).days
        igbo_day = igbo_cycle[diff % 4]
        week.append({
            "date": d.strftime("%Y-%m-%d"),
            "day_name": d.strftime("%a %d %b"),
            "moon": mp,
            "igbo_day": igbo_day,
            "igbo_info": IGBO_DAYS[igbo_day]
        })
    return week

# Example usage for Django view context
def awag_moon_context():
    today = get_moon_phase()
    week = get_weekly_moon_phases()
    today_igbo = week[0]
    return {
        "today_moon": today,
        "today_igbo": today_igbo["igbo_day"],
        "today_element": today_igbo["igbo_info"],
        "week_moon": week,
        "moon_phases_list": PHASES,
    }

if __name__ == "__main__":
    ctx = awag_moon_context()
    print(f"Today: {ctx['today_moon']['emoji']} {ctx['today_moon']['name']} {ctx['today_moon']['illumination']}%")
    print(f"Igbo: {ctx['today_igbo']} - {ctx['today_element']['element']} - {ctx['today_element']['good_for']}")
    for day in ctx['week_moon'][:7]:
        print(f"{day['day_name']} {day['igbo_day']} {day['moon']['emoji']} {day['moon']['name']} {day['moon']['illumination']}% - Fishing: {day['moon']['guidance']['fishing']}")
