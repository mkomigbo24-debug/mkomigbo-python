import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from religion.models import Religion, SacredText, Doctrine, Deity, EsotericTradition

# 1. ODINALA - Your main thesis
odinala, _ = Religion.objects.get_or_create(slug='odinala', defaults={
    'name': 'Odinala - Odinani',
    'type': 'ATR',
    'origin': 'Igbo Land - 9th century Igbo-Ukwu',
    'founder': 'N/A - Indigenous',
    'founded_date': 'Ancient - Pre 9th century',
    'overview': 'Odinala is Igbo traditional religion - thesis level documentation. Chukwu as Supreme, Alusi as deities, Chi as personal god, reincarnation, Ofo Na Ogu justice system.',
    'core_beliefs': 'Chukwu Okike (Creator), Alusi (deities), Mmuo (spirits), Chi (personal god), Eke na Ala, Reincarnation - Ilo Uwa, Ofo justice',
    'cosmology': 'Uwa (physical), Mmuo (spiritual), Chi interconnected. 4 market days Eke, Orie, Afo, Nkwo as cosmological principle.',
})

# Deities
Deity.objects.get_or_create(name='Chukwu', defaults={'religion': odinala, 'role': 'Supreme Creator - Chukwu Okike Abiama', 'is_alusi': False, 'symbolism': 'Creator of all, not worshipped directly'})
Deity.objects.get_or_create(name='Ani', defaults={'religion': odinala, 'role': 'Earth goddess - Mother Earth, morality', 'is_alusi': True})
Deity.objects.get_or_create(name='Amadioha', defaults={'religion': odinala, 'role': 'God of thunder and justice', 'is_alusi': True})
Deity.objects.get_or_create(name='Agwu', defaults={'religion': odinala, 'role': 'Alusi of divination and healing, patron of Dibia', 'is_alusi': True})

# Sacred text
SacredText.objects.get_or_create(title='Ofo Na Ogu', defaults={'religion': odinala, 'language_original': 'Igbo', 'summary': 'Igbo justice and moral code - symbol of truth'})

# 2. Other religions - thesis level comparison
christianity, _ = Religion.objects.get_or_create(slug='christianity', defaults={
    'name': 'Christianity',
    'type': 'Abrahamic',
    'origin': 'Jerusalem, 1st century',
    'founder': 'Jesus Christ',
    'overview': 'Abrahamic religion based on life of Jesus. Comparative thesis with Odinala - Chi vs Holy Spirit, reincarnation vs resurrection.',
    'core_beliefs': 'Trinity, salvation, resurrection',
    'cosmology': 'Heaven, Earth, Hell',
})

islam, _ = Religion.objects.get_or_create(slug='islam', defaults={
    'name': 'Islam',
    'type': 'Abrahamic',
    'origin': 'Mecca, 7th century',
    'founder': 'Prophet Muhammad',
    'overview': 'Submission to Allah. Comparative with Odinala Chukwu concept.',
    'core_beliefs': 'Five pillars, Tawhid',
    'cosmology': 'Dunya, Akhira',
})

# 3. ESOTERISM - Inner teachings
afa, _ = EsotericTradition.objects.get_or_create(name='Afa Divination', defaults={
    'origin_tradition': 'Igbo Afa',
    'parent_religion': odinala,
    'description': 'Igbo binary divination system - 256 Odu, thesis level inner teaching',
    'inner_teaching': 'Afa is Igbo metaphysical binary code - 8x8 = 256. Each Odu is a spiritual algorithm. Connection to Ifa, but distinct Igbo system.',
    'outer_teaching': 'Divination for guidance',
    'methods': 'Igo Ofo, Igba Afa, Odu interpretation',
})

print("=== RELIGION + ESOTERISM LOADED ===")
from religion.models import Religion, Deity, SacredText, EsotericTradition
print(f"Religions: {Religion.objects.count()} - Deities: {Deity.objects.count()} - Texts: {SacredText.objects.count()} - Esoteric: {EsotericTradition.objects.count()}")
for r in Religion.objects.all():
    print(f"- {r.name} ({r.type})")
