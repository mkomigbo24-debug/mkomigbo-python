from lang1.models import PresentAlphabet, MissingPhoneme

# Clear old
PresentAlphabet.objects.all().delete()
MissingPhoneme.objects.all().delete()

# 1. Dropped Q,X - Thesis core
PresentAlphabet.objects.create(symbol='Q', ipa='N/A', example='-', meaning='DROPPED - English Q is /kw/', category='single', is_dropped=True, thesis_note='English Q = KW, Igbo uses KW digraph, so Q dropped from 26 to 24')
PresentAlphabet.objects.create(symbol='X', ipa='N/A', example='-', meaning='DROPPED - English X is /ks/', category='single', is_dropped=True, thesis_note='English X = KS, Igbo has no KS cluster, so X dropped')

# 2. Single letters
singles = [('A','/a/','aka','hand'),('B','/b/','bia','come'),('D','/d/','de','write'),('E','/e/','ere','sell'),('F','/f/','fe','fly'),('G','/g/','ga','go'),('H','/h/','ha','they'),('I','/i/','ife','thing'),('J','/dʒ/','ji','yam'),('K','/k/','kwa','also'),('L','/l/','li','eat'),('M','/m/','mmiri','water'),('N','/n/','nne','mother'),('O','/o/','obi','heart'),('P','/p/','pia','press'),('R','/r/','ri','eat'),('S','/s/','si','from'),('T','/t/','ta','chew'),('V','/v/','vo','dialectal'),('W','/w/','wa','they'),('Y','/j/','ya','his'),('Z','/z/','zu','buy')]
for s,ipa,ex,mean in singles:
    PresentAlphabet.objects.create(symbol=s, ipa=ipa, example=ex, meaning=mean, category='single')

# 3. Diacritics - Dot below
PresentAlphabet.objects.create(symbol='Ị', ipa='/ɪ/', example='inyinya', meaning='horse', category='diacritic', thesis_note='Dot below - English has no this')
PresentAlphabet.objects.create(symbol='Ọ', ipa='/ɔ/', example='oku', meaning='fire', category='diacritic')
PresentAlphabet.objects.create(symbol='Ụ', ipa='/ʊ/', example='ulo', meaning='house', category='diacritic')
PresentAlphabet.objects.create(symbol='Ṅ', ipa='/ŋ/', example='nga', meaning='singa', category='diacritic')

# 4. Digraphs - CH wrongly as letter
PresentAlphabet.objects.create(symbol='CH', ipa='/tʃ/', example='chere', meaning='wait', category='digraph', thesis_note='WRONGLY ADOPTED - C+H two letters forced as one alphabet. English CH same but should be single symbol like Č')
PresentAlphabet.objects.create(symbol='GB', ipa='/ɡ͡b/', example='gba', meaning='shoot', category='digraph', thesis_note='Labial-velar - Good addition, not in English')
PresentAlphabet.objects.create(symbol='KP', ipa='/k͡p/', example='kpaa', meaning='pluck', category='digraph')
PresentAlphabet.objects.create(symbol='GW', ipa='/ɡʷ/', example='gwa', meaning='tell', category='digraph')
PresentAlphabet.objects.create(symbol='KW', ipa='/kʷ/', example='kwa', meaning='also', category='digraph')
PresentAlphabet.objects.create(symbol='NW', ipa='/nʷ/', example='nwa', meaning='child', category='digraph', thesis_note='Very Igbo!')
PresentAlphabet.objects.create(symbol='NY', ipa='/ɲ/', example='nyere', meaning='give', category='digraph', thesis_note='Like Spanish ñ')
PresentAlphabet.objects.create(symbol='GH', ipa='/ɣ/', example='ghara', meaning='forbid', category='digraph')
PresentAlphabet.objects.create(symbol='SH', ipa='/ʃ/', example='shi', meaning='dialectal', category='digraph')

# 5. Missing - Tones - Biggest missing!
MissingPhoneme.objects.create(symbol='á', category='tone', ipa='/á/', example='ákwá', meaning_diff='cry (high tone)', reason_missing='English has no tones, so Onwu omitted tone marks - child confuses akwa cloth/egg/cry/bed')
MissingPhoneme.objects.create(symbol='à', category='tone', ipa='/à/', example='àkwá', meaning_diff='egg (low tone)', reason_missing='No low tone mark in borrowed script')
MissingPhoneme.objects.create(symbol='ā (a)', category='tone', ipa='/a/', example='akwa', meaning_diff='cloth/bed (mid tone)', reason_missing='Mid tone not written')
MissingPhoneme.objects.create(symbol='ń / ḿ', category='syllabic_nasal', ipa='/n̩/ /m̩/', example='ńnà / ḿmā', meaning_diff='father / knife - nasal as vowel', reason_missing='English M,N cannot be vowel alone, but Igbo ḿ, ń are vowels!')

print("Thesis data loaded: Present 36 + Dropped Q,X + Missing tones")
