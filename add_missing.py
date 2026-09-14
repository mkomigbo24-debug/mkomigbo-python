import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from lang1.models import MissingPhoneme, PresentAlphabet
import inspect
print("MissingPhoneme fields:", [f.name for f in MissingPhoneme._meta.get_fields()])

# Try with only common fields
from django.db import models

# Clear old failed entries
# MissingPhoneme.objects.all().delete()

# Use correct fields - adapt to your model
# Usually model has: symbol, ipa, example, meaning, category, thesis_note or description

data = [
    ("High Tone á", "/á/", "ákwá cry vs àkwà bed", "cry", "tone", "Same letters 4 meanings by tone only - Onwu dropped tones!"),
    ("Syllabic ḿ ń", "/m̩/ /n̩/", "ḿmā knife, ńnà father", "knife", "syllabic_nasal", "M/N as vowels! English cannot write this"),
    ("C vs Cʰ", "/c/ vs /tʃ/= /cʰ/", "cuo /cʊɔ/ chase vs chuo /tʃʊɔ/ sacrifice", "chase vs sacrifice", "aspiration", "Minimal pair cuo vs chuo proves H is separate - CH not letter!"),
    ("TS Nkwerre", "/ts/ vs /tʃ/", "ọchara /ɔtʃara/ vs ọtsara /ɔtsara/ fruit ripe", "fruit ripe", "dialectal", "Nkwerre ch->ts de-palatalization proves CH compositional"),
    ("ZH azhia", "/ʒ/ = /zʰ/", "ahia vs azhia /aʒia/ market", "market", "palatalization", "Z+H=/ʒ/ Nkwerre/Mbano - H palatalizes"),
    ("SH", "/ʃ/ = /sʰ/", "sara vs shara", "exceed", "palatalization", "S+H=/ʃ/"),
    ("GH", "/ɣ/ = /gʰ/", "ghara forbid", "forbid", "fricative", "G+H=/ɣ/"),
    ("Kʷ Gʷ Nʷ", "/kʷ/ /gʷ/ /nʷ/", "kwa, gwa, nwa child /nʷa/", "child", "labialization", "W=/ʷ/ lip rounding not letter"),
    ("ã ẽ ĩ nasal", "/ã/ /ẽ/ /ĩ/", "anh nasal vowel", "nasal", "nasalization", "Nasal vowel missing"),
    ("Pʰ Tʰ Kʰ", "/pʰ/ /tʰ/ /kʰ/", "aspirated", "aspirated", "aspiration", "Every plosive +H = aspirated /ʰ/"),
    ("ɓ ɗ implosive", "/ɓ/ /ɗ/", "ɓia dialect", "come", "implosive", "Implosive B dialectal"),
    ("Nsibidi", "/nsibidi/", "Original Igbo script", "original", "original", "Latin A-Z colonial borrowed - lost Nsibidi"),
]

for symbol, ipa, ex, mean, cat, note in data:
    # Try flexible field mapping
    try:
        obj, created = MissingPhoneme.objects.get_or_create(
            symbol=symbol,
            defaults={'ipa': ipa, 'example': ex, 'meaning': mean, 'category': cat, 'thesis_note': note}
        )
    except Exception as e:
        # If thesis_note fails, try description or note
        try:
            obj, created = MissingPhoneme.objects.get_or_create(
                symbol=symbol,
                defaults={'ipa': ipa, 'example': ex, 'meaning': mean, 'category': cat, 'description': note}
            )
        except:
            # Last resort - minimal fields
            obj, created = MissingPhoneme.objects.get_or_create(
                symbol=symbol,
                defaults={'ipa': ipa, 'example': ex}
            )
    print(f"{'Added' if created else 'Exists'}: {symbol}")

print(f"Total Missing: {MissingPhoneme.objects.count()}")
print(f"Total Present: {PresentAlphabet.objects.count()}")
