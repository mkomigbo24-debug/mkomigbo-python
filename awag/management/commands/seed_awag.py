from django.core.management.base import BaseCommand
from awag.models import Region, WeeklyGuide, Tide
from datetime import date, timedelta, datetime
from django.utils import timezone
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Farmers + Regions (keep as is)
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        # Tide 40 ports - Beira to Luanda now populated
        ports_all = [
            'Bonny Opobo Brass','Calabar','Lagos-Bar','Mombasa','Dakar','Tema','Abidjan','Cotonou','Lome','Douala',
            'Beira','Maputo','Djibouti','Port Sudan','Alexandria','Casablanca','Cape Town','Durban','Walvis Bay','Luanda',
            'Freetown','Conakry','Bissau','Monrovia','Nouakchott','Baga Lake Chad','Kisumu Winam Gulf','Mwanza','Kigoma','Kalemie',
            'Zanzibar','Mogadishu','Dar es Salaam','Nairobi','Kampala','Mahajanga','Pointe-Noire','Libreville','Kinshasa','Hurghada'
        ]
        base = timezone.now()
        for port in ports_all:
            for i in range(7):
                dt = base + timedelta(days=i)
                high_hour = random.randint(6,18)
                high_dt = dt.replace(hour=high_hour, minute=random.randint(0,59), second=0, microsecond=0)
                low_dt = high_dt - timedelta(hours=random.randint(4,8))
                Tide.objects.update_or_create(
                    location=port, datetime=dt.replace(hour=12, minute=0, second=0, microsecond=0),
                    defaults={
                        'high_tide_time': high_dt,
                        'low_tide_time': low_dt,
                        'high_height_m': round(random.uniform(1.0,3.2),1),
                        'low_height_m': round(random.uniform(0.2,1.0),1),
                        'advice_en': f'Fishing best {port} - High {high_dt.strftime("%H:%M")} Low {low_dt.strftime("%H:%M")} - Moon Waxing Crescent - Wind locality',
                        'fishing_best': f'Best fishing window High tide {high_dt.strftime("%H:%M")} + Moon phase'
                    }
                )
        self.stdout.write(self.style.SUCCESS(f'AWAG seeded - 40 ports tide table - Beira to Luanda now populated - no blank!'))