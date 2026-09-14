# Thesis Expansion: Add zh, gh, tsara, azhia, cuo vs chuo proof
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from lang1.models import PresentAlphabet, MissingPhoneme

# Clear and add TRUE phonemes - Labialized proof
data_present = [
    # Your CH fallacy proof: ch = c + h, not a letter!
    {'symbol': 'cuo', 'ipa': '/kʷo/', 'example': 'cuo ala', 'meaning': 'mould soil - labialized proof', 'category': 'labialized_consonant', 'thesis_note': 'CH FALLACY: cuo vs chuo - u is labialization, not ch. Proof that ch is c+h'},
    {'symbol': 'guo', 'ipa': '/gʷo/', 'example': 'guo ofe', 'meaning': 'stir soup', 'category': 'labialized_consonant', 'thesis_note': 'Labialized - guo not g+uo'},
    {'symbol': 'zh', 'ipa': '/ʒ/', 'example': 'azhịa', 'meaning': 'market - correct not azhia', 'category': 'affricate', 'thesis_note': 'Missing in standard orthography - zh as in azhịa'},
    {'symbol': 'gh', 'ipa': '/ɣ/', 'example': 'aghara', 'meaning': 'change', 'category': 'affricate', 'thesis_note': 'Voiced velar fricative - missing'},
    {'symbol': 'ts', 'ipa': '/t͡s/', 'example': 'tsara', 'meaning': 'answer', 'category': 'affricate', 'thesis_note': 'tsara not sara - affricate proof'},
    {'symbol': 'zhia', 'ipa': '/ʒʲa/', 'example': 'azhịa', 'meaning': 'market - palatalized', 'category': 'labialized_digraph', 'thesis_note': 'Palatalized zhia'},
]

for item in data_present:
    obj, created = PresentAlphabet.objects.get_or_create(symbol=item['symbol'], defaults=item)
    print(f"{'Created' if created else 'Exists'}: {item['symbol']} - {item['ipa']}")

# Missing phonemes - 12 missing proof
data_missing = [
    {'symbol': 'zh', 'ipa': '/ʒ/', 'example': 'azhịa - market, not azhia', 'meaning_diff': 'azhia (wrong) vs azhịa (correct zh sound)', 'category': 'affricate_missing', 'reason_missing': 'Standard orthography collapsed zh to z, losing distinction. zh is voiced postalveolar fricative.'},
    {'symbol': 'gh', 'ipa': '/ɣ/', 'example': 'aghara vs ahara', 'meaning_diff': 'Different meanings lost', 'category': 'affricate_missing', 'reason_missing': 'gh is voiced velar fricative missing in 36 letter orthography'},
    {'symbol': 'tsara', 'ipa': '/t͡sara/', 'example': 'tsara iza - answer question', 'meaning_diff': 'tsara (answer) vs sara (??) - meaning lost without ts', 'category': 'affricate_missing', 'reason_missing': 'ts affricate proved by minimal pair'},
    {'symbol': 'cuo', 'ipa': '/kʷo/', 'example': 'cuo vs chuo', 'meaning_diff': 'cuo = mould, chuo = ??? CH fallacy exposed', 'category': 'labialized', 'reason_missing': 'CH FALLACY: ch is NOT a letter, it is c + h aspiration. cuo proves labialization is on consonant, not vowel. u in cuo is w, not vowel.'},
    {'symbol': 'zhia', 'ipa': '/ʒʲa/', 'example': 'zhia - to shine', 'meaning_diff': 'Palatalization distinction', 'category': 'palatalized', 'reason_missing': 'Palatalized consonants missing: zhia, ghia, nyia etc'},
    {'symbol': 'High tone', 'ipa': '/́/', 'example': 'ákwá vs àkwà', 'meaning_diff': 'egg vs cloth vs cry - tone changes meaning', 'category': 'tone', 'reason_missing': 'Tones not written - causes ambiguity'},
]

for item in data_missing:
    obj, created = MissingPhoneme.objects.get_or_create(symbol=item['symbol'], ipa=item['ipa'], defaults=item)
    print(f"{'Created' if created else 'Exists'} MISSING: {item['symbol']}")

print("\\n=== THESIS EXPANDED ===")
print(f"Present: {PresentAlphabet.objects.count()} - Missing: {MissingPhoneme.objects.count()}")
