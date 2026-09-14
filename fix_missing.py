import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from lang1.models import MissingPhoneme

# Clear and re-add with correct field names
MissingPhoneme.objects.all().delete()

data = [
    ("á à ā - Tones", "tone", "/á/ /à/ /ā/", "ákwá cry vs àkwà bed vs ákwà egg vs àkwá cloth", "Same letters 4 meanings by tone only! Cry vs bed vs egg vs cloth", "Onwu 1961 dropped tone marks - English has no tone, Igbo needs tone mandatory - biggest missing!"),
    ("ḿ ń Syllabic", "syllabic_nasal", "/m̩/ /n̩/ high tone", "ḿmā knife, ńnà father, ḿ - I", "M/N as vowels! ḿmā knife, ńnà father", "English cannot write consonant as vowel - borrowed Latin script fails"),
    ("C vs Cʰ - CH Fallacy", "aspiration", "/c/ vs /tʃ/ = /cʰ/", "cuo /cʊɔ́/ chase vs chuo /tʃʊɔ́/ sacrifice = chuo aja", "cuo chase/pursue/sack vs chuo sacrifice - H alone changes meaning! Minimal pair!", "CH wrongly as alphabet letter No.8 - should be C + aspiration diacritic Cʰ. Proposal: Č"),
    ("TS - Nkwerre de-palatal", "dialectal", "/ts/ vs /tʃ/", "ọchara acha /ɔtʃara/ vs ọtsara atsa /ɔtsara/ fruit ripe", "ochara vs tsara atsa - CH → TS in Nkwerre/Mbano", "Proves CH compositional: /t/+/ʃ/=/tʃ/ → /ts/ if CH were one letter cannot become ts"),
    ("ZH azhia market", "palatalization", "/ʒ/ = /zʰ/ = /zʲ/", "ahia /ahia/ Onitsha vs azhia /aʒia/ Nkwerre/Mbano market", "ahia vs azhia market - Z+H=/ʒ/ like French je", "H is palatalization feature /ʲ/ not part of digraph - proves H modifier"),
    ("SH", "palatalization", "/ʃ/ = /sʰ/", "sara exceed vs shara dialectal", "sara vs shara - S+H=/ʃ/", "SH digraph hides H as modifier /ʰ/"),
    ("GH", "fricative", "/ɣ/ = /gʰ/", "ghara forbid", "ghara forbid - G+H=/ɣ/ voiced velar fricative", "GH is G with frication, not digraph letter"),
    ("Kʷ Gʷ Nʷ Labial", "labialization", "/kʷ/ /gʷ/ /nʷ/ = /ʷ/", "kwa also, gwa tell, nwa child /nʷa/", "kwa, gwa, nwa child = /nʷa/ not N+W", "W=/ʷ/ lip rounding feature not letter - Onwu writes KW but is /kʷ/"),
    ("ã ẽ ĩ Nasal vowel", "nasalization", "/ã/ /ẽ/ /ĩ/ /ɔ̃/", "anh nasal vowel - an = ã", "an = nasal vowel /ã/ not a+n", "English writes an but Igbo has nasal vowel phoneme missing"),
    ("Pʰ Tʰ Kʰ Aspirated", "aspiration", "/pʰ/ /tʰ/ /kʰ/", "pʰa, tʰa, kʰa aspirated", "Every plosive +H = aspirated /ʰ/ - aka vs kha", "H as aspiration diacritic /ʰ/ not recognized"),
    ("ɓ ɗ Implosive", "implosive", "/ɓ/ /ɗ/", "ɓia dialectal come", "bia /b/ vs ɓia implosive /ɓ/", "Borrowed English B=/b/ only, Igbo dialect has /ɓ/ implosive missing"),
    ("Nsibidi Original", "original_script", "/nsibidi/", "Original Igbo script before 1840s", "Latin A-Z colonial borrowed - lost Nsibidi", "Britain gave 26 letters, Q+X dropped to 24, added 12 to make 36 - lost original writing system"),
]

for symbol, cat, ipa, ex, diff, reason in data:
    obj, created = MissingPhoneme.objects.get_or_create(
        symbol=symbol,
        defaults={'category': cat, 'ipa': ipa, 'example': ex, 'meaning_diff': diff, 'reason_missing': reason}
    )
    print(f"{'Added' if created else 'Exists'}: {symbol}")

print(f"Total Missing: {MissingPhoneme.objects.count()}")
