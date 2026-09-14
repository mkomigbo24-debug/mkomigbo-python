import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from religion.models import Religion, SacredText, Deity

odinala, _ = Religion.objects.get_or_create(slug='odinala', defaults={
    'name': 'Odinala - Odinani',
    'type': 'ATR',
    'origin': 'Igbo Land',
    'overview': 'Odinala thesis',
    'core_beliefs': 'Chukwu, Alusi, Chi',
    'cosmology': 'Uwa, Mmuo',
})
Deity.objects.get_or_create(name='Chukwu', defaults={'religion': odinala, 'role': 'Supreme Creator'})
Deity.objects.get_or_create(name='Ani', defaults={'religion': odinala, 'role': 'Earth goddess', 'is_alusi': True})
print(f"Religions: {Religion.objects.count()}")
