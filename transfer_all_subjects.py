"""
Transfer ALL 21 subjects + Nsibidi into mkomigbo-python
Subjects: Igbo, Ndebe, Nsibidi, Amuzhi, AWAG, Odinala, etc.
"""
import json
import os
from pathlib import Path

# 21 subjects + Nsibidi = 22
SUBJECTS_21_PLUS_NSIBIDI = [
    {"slug":"igbo-language","name":"Igbo Language","description":"Igbo asụsụ - 4 dialects","icon":"🗣️","nav_order":1},
    {"slug":"ndebe-49","name":"Ndebe 49","description":"49 Ndebe glyphs - base script","icon":"🔤","nav_order":2},
    {"slug":"ndebe-glyphs","name":"Ndebe Glyphs H Effect","description":"H effect 27 minimal pairs B BH CH etc","icon":"✍️","nav_order":3},
    {"slug":"nsibidi","name":"Nsibidi","description":"Nsibidi ideographs - 500+ symbols, Calabar, Ejagham, Igbo","icon":"🪶","nav_order":4},  # MUST INCLUDE!
    {"slug":"amuzhi-calendar","name":"Amuzhi Calendar","description":"13 months + 4 market days Eke Orie Afo Nkwo","icon":"📅","nav_order":5},
    {"slug":"awag","name":"AWAG - Africa Weekly Guide","description":"58 regions wind locality farmers fishermen","icon":"🌍","nav_order":6},
    {"slug":"odinala","name":"Odinala","description":"Odinala religion - Chi, Ala, Amadioha","icon":"⛪","nav_order":7},
    {"slug":"history-ndigbo","name":"History Ndigbo","description":"History of Ndigbo - migration","icon":"📜","nav_order":8},
    {"slug":"culture","name":"Igbo Culture","description":"Culture - masquerade, marriage, title","icon":"🎭","nav_order":9},
    {"slug":"proverbs","name":"Ilu - Proverbs","description":"Igbo proverbs","icon":"💬","nav_order":10},
    {"slug":"folktales","name":"Akuko - Folktales","description":"Folktales","icon":"📖","nav_order":11},
    {"slug":"medicine","name":"Ogwu - Medicine","description":"Traditional medicine","icon":"🌿","nav_order":12},
    {"slug":"astronomy","name":"Igbo Astronomy","description":"Igbo astronomy - kpakpando","icon":"⭐","nav_order":13},
    {"slug":"mathematics","name":"Igbo Mathematics","description":"Mgbako - counting, Onu ogugu","icon":"🔢","nav_order":14},
    {"slug":"music","name":"Igbo Music","description":"Egwu - instruments","icon":"🥁","nav_order":15},
    {"slug":"dance","name":"Igbo Dance","description":"Igba egwu","icon":"💃","nav_order":16},
    {"slug":"art","name":"Igbo Art","description":"Nka - Uli, pottery","icon":"🎨","nav_order":17},
    {"slug":"food","name":"Igbo Food","description":"Nri - Ji, Ofe","icon":"🍲","nav_order":18},
    {"slug":"governance","name":"Igbo Governance","description":"Ochi ochichi - Umunna, Eze","icon":"⚖️","nav_order":19},
    {"slug":"language2","name":"Language2","description":"Second language data","icon":"📚","nav_order":20},
    {"slug":"esoteric","name":"Esoteric","description":"Esoteric knowledge","icon":"🔮","nav_order":21},
    {"slug":"thesis","name":"MkomIgbo Thesis","description":"CH Fallacy Thesis PDF","icon":"🎓","nav_order":22},
]

def run():
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
    django.setup()
    from subjects.models import Subject
    
    print(f"Creating {len(SUBJECTS_21_PLUS_NSIBIDI)} subjects including Nsibidi...")
    for data in SUBJECTS_21_PLUS_NSIBIDI:
        obj, created = Subject.objects.update_or_create(
            slug=data["slug"],
            defaults=data
        )
        print(f"{'Created' if created else 'Updated'}: {data['slug']} - {data['name']}")
    
    print(f"Total subjects now: {Subject.objects.count()}")
    print("Nsibidi included! ✅")

if __name__ == "__main__":
    run()