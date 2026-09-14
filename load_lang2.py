import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from lang2.models import Tone, Dialect, GrammarRule

Tone.objects.get_or_create(name='High vs Low vs Downstep', defaults={
    'symbol': '´ vs \ vs ꜜ',
    'tone_type': 'high',
    'ipa': '/á/ vs /à/ vs /â/',
    'example1': 'ákwá',
    'meaning1': 'egg - high high',
    'example2': 'àkwà',
    'meaning2': 'cloth/bed - low low - proves tone changes meaning',
    'example3': 'ákwà',
    'meaning3': 'cry - high low - 3-way tone distinction thesis',
    'thesis_proof': 'STANDARD ORTHOGRAPHY HIDES TONE - Causes ambiguity. akwá (egg) vs àkwà (cloth) vs ákwà (cry) all written as akwa in standard. Tone is phonemic, not optional. 3 tones minimum, not 2. Proves 12 missing includes tones.',
})

Tone.objects.get_or_create(name='Tonal minimal pair - tone is phoneme', defaults={
    'symbol': '´',
    'tone_type': 'high',
    'ipa': '/ó/ vs /ò/',
    'example1': 'ó rìrì',
    'meaning1': 'he ate (past)',
    'example2': 'ò rìrì',
    'meaning2': 'you ate - tone marks person',
    'example3': 'ò riri',
    'meaning3': 'he ate (habitual) - downstep',
    'thesis_proof': 'Tone marks tense and person, not just lexical meaning. Missing tones = missing grammar.',
})

Dialect.objects.get_or_create(name='Owerri', defaults={
    'region': 'Imo - Standard base',
    'phonological_diff': 'Keeps zh? No, lost zh -> z. Uses ahia for market (should be azhịa).',
    'example_words': 'ahia (market) - wrong, should be azhịa with zh /ʒ/',
    'thesis_proof': 'Owerri dialect lost zh, gh distinctions - proves need for 43 phonemes restoration',
})

Dialect.objects.get_or_create(name='Onitsha', defaults={
    'region': 'Anambra',
    'phonological_diff': 'More conservative, keeps some affricates',
    'example_words': 'afia (market) vs azhịa - variation shows original zh',
    'thesis_proof': 'Onitsha afia vs Owerri ahia - both attempts to write zh without zh letter',
})

GrammarRule.objects.get_or_create(title='Verb Serialization - Thesis', defaults={
    'category': 'verb',
    'rule': 'Igbo verbs serialize: multiple verbs in one clause sharing subject. Reflects Odinala chain of being.',
    'examples': 'O guro akwukwo daa - He read book fall = He read until he fell',
    'igbo_example': 'Ọ gwara m okwu, m nụọ',
    'english_gloss': 'He told me word, I heard',
    'thesis_notes': 'Serialization reflects Igbo philosophy of interconnected actions - not separate like English',
    'odinala_connection': 'Actions linked like Chi and Uwa - no isolation',
})

print(f"Tones: {Tone.objects.count()} - Dialects: {Dialect.objects.count()} - Grammar: {GrammarRule.objects.count()}")
