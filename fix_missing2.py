import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from lang1.models import MissingPhoneme
MissingPhoneme.objects.all().delete()

data = [
    ("Tones áàā", "tone", "/á/ /à/ /ā/", "ákwá cry vs àkwà bed", "4 meanings by tone only! Cry vs bed vs egg vs cloth", "Onwu 1961 dropped tones - biggest missing!"),
    ("ḿ ń Syllabic", "syllabic_nasal", "/m̩/ /n̩/", "ḿmā knife, ńnà father", "M/N as vowels! ḿmā knife, ńnà father", "English cannot write consonant as vowel - borrowed script fails"),
    ("C vs Cʰ CH", "aspiration", "/c/ vs /tʃ/= /cʰ/", "cuo /cʊɔ/ vs chuo /tʃʊɔ/ sacrifice", "cuo chase vs chuo sacrifice - H changes meaning! Minimal pair!", "CH wrongly as alphabet letter No.8 - should be C + aspiration Cʰ Proposal Č"),
    ("TS Nkwerre", "dialectal", "/ts/ vs /tʃ/", "ọchara /ɔtʃara/ vs ọtsara /ɔtsara/", "ochara vs tsara atsa - CH->TS", "Proves CH compositional: /t/+/ʃ/=/tʃ/ -> /ts/"),
    ("ZH azhia", "palatalization", "/ʒ/ = /zʰ/", "ahia vs azhia /aʒia/ market", "ahia vs azhia market - Z+H=/ʒ/", "H is palatalization /ʲ/ not part of digraph"),
    ("SH", "palatalization", "/ʃ/ = /sʰ/", "sara vs shara", "sara vs shara - S+H=/ʃ/", "SH hides H as modifier /ʰ/"),
    ("GH", "fricative", "/ɣ/ = /gʰ/", "ghara forbid", "ghara - G+H=/ɣ/", "GH is G with frication"),
    ("Kʷ Gʷ Nʷ", "labialization", "/kʷ/ /gʷ/ /nʷ/ = /ʷ/", "kwa, gwa, nwa /nʷa/", "kwa, gwa, nwa child=/nʷa/ not N+W", "W=/ʷ/ lip rounding not letter"),
    ("ã ẽ ĩ nasal", "nasalization", "/ã/ /ẽ/ /ĩ/ /ɔ̃/", "anh nasal vowel", "an = nasal vowel /ã/ not a+n", "Nasal vowel missing"),
    ("Pʰ Tʰ Kʰ", "aspiration", "/pʰ/ /tʰ/ /kʰ/", "pʰa, tʰa, kʰa", "Every plosive +H = aspirated /ʰ/", "H as aspiration /ʰ/ not recognized"),
    ("ɓ ɗ implosive", "implosive", "/ɓ/ /ɗ/", "ɓia dialectal", "bia /b/ vs ɓia /ɓ/", "English B=/b/ only, Igbo has /ɓ/ missing"),
    ("Nsibidi", "original_script", "/nsibidi/", "Original Igbo script", "Latin A-Z colonial borrowed", "Britain gave 26 letters, Q+X dropped, added 12 to make 36 - lost Nsibidi"),
]

for symbol, cat, ipa, ex, diff, reason in data:
    obj, created = MissingPhoneme.objects.get_or_create(
        symbol=symbol,
        defaults={'category': cat, 'ipa': ipa, 'example': ex, 'meaning_diff': diff, 'reason_missing': reason}
    )
    print(f"{'Added' if created else 'Exists'}: {symbol}")

print(f"Total Missing: {MissingPhoneme.objects.count()}")
