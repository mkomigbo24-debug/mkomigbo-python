import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from language2.models import Tone, Dialect, GrammarRule

Tone.objects.get_or_create(name='High vs Low vs Downstep', defaults={
    'symbol': '´ vs \ vs ꜜ',
    'tone_type': 'high',
    'ipa': '/á/ vs /à/ vs /â/',
    'example1': 'ákwá',
    'meaning1': 'egg - high high',
    'example2': 'àkwà',
    'meaning2': 'cloth/bed - low low',
    'example3': 'ákwà',
    'meaning3': 'cry - high low - 3-way proof',
    'thesis_proof': 'STANDARD ORTHOGRAPHY HIDES TONE - akwa written same for egg/cloth/cry. Tone is phonemic.',
})

Tone.objects.get_or_create(name='Tonal minimal pair', defaults={
    'symbol': '´',
    'tone_type': 'high',
    'ipa': '/ó/ vs /ò/',
    'example1': 'ó rìrì',
    'meaning1': 'he ate (past)',
    'example2': 'ò rìrì',
    'meaning2': 'you ate',
    'example3': 'ò riri',
    'meaning3': 'he ate habitual',
    'thesis_proof': 'Tone marks tense and person',
})

Dialect.objects.get_or_create(name='Owerri', defaults={
    'region': 'Imo - Standard base',
    'phonological_diff': 'Lost zh -> z. ahia for market should be azhịa',
    'example_words': 'ahia - wrong, should be azhịa with zh /ʒ/',
    'thesis_proof': 'Lost zh, gh - proves 43 phonemes',
})

Dialect.objects.get_or_create(name='Onitsha', defaults={
    'region': 'Anambra',
    'phonological_diff': 'More conservative',
    'example_words': 'afia vs azhịa - variation shows original zh',
    'thesis_proof': 'afia vs ahia both attempts to write zh',
})

GrammarRule.objects.get_or_create(title='Verb Serialization - Thesis', defaults={
    'category': 'verb',
    'rule': 'Igbo verbs serialize: multiple verbs sharing subject. Reflects Odinala chain of being.',
    'examples': 'O guro akwukwo daa - He read book fall = He read until he fell',
    'igbo_example': 'Ọ gwara m okwu, m nụọ',
    'english_gloss': 'He told me word, I heard',
    'thesis_notes': 'Serialization reflects Igbo philosophy',
    'odinala_connection': 'Actions linked like Chi and Uwa',
})

print(f"Tones: {Tone.objects.count()} - Dialects: {Dialect.objects.count()} - Grammar: {GrammarRule.objects.count()}")
