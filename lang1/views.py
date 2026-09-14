from django.shortcuts import render
from .models import PresentAlphabet, MissingPhoneme

def phonemes_view(request):
    present = PresentAlphabet.objects.all().order_by('symbol')
    missing = MissingPhoneme.objects.all().order_by('category')
    
    h_effects = [
        {'base': 'S', 'with_h': 'SH', 'ipa_base': '/s/', 'ipa_h': '/ʃ/', 'example_std': 'sara - exceed', 'example_dialect': 'shara - dialectal', 'dialect': 'General', 'process': 'Palatalization: s + h → ʃ'},
        {'base': 'Z', 'with_h': 'ZH', 'ipa_base': '/z/', 'ipa_h': '/ʒ/', 'example_std': 'ahia /a.hia/ market (Onitsha)', 'example_dialect': 'azhia /a.ʒia/ market', 'dialect': 'Nkwerre, Mbano', 'process': 'Palatalized fricative: z + h → ʒ'},
        {'base': 'C', 'with_h': 'CH', 'ipa_base': '/c/ or /k/', 'ipa_h': '/tʃ/ vs /ʃ/ vs /ts/', 'example_std': 'cuo /cʊɔ/ - chase/pursue/sack', 'example_dialect': 'chuo /tʃʊɔ/ - chuo aja = sacrifice', 'dialect': 'Standard vs Dialectal', 'process': 'Affrication: c + h → tʃ'},
        {'base': 'T', 'with_h': 'TS', 'ipa_base': '/t/', 'ipa_h': '/ts/ or /tʃ/', 'example_std': 'ochara /ɔtʃara/ - fruit ripe', 'example_dialect': 'otsara /ɔtsara/ or tsara atsa', 'dialect': 'Nkwerre/Mbano', 'process': 'De-palatalization: tʃ → ts'},
        {'base': 'K', 'with_h': 'KH', 'ipa_base': '/k/', 'ipa_h': '/kʰ/ or /x/', 'example_std': 'aka hand', 'example_dialect': 'kha - aspirated', 'dialect': 'Emphasis', 'process': 'Aspiration: k + h → kʰ'},
    ]
    
    return render(request, 'lang1/phonemes.html', {
        'present': present,
        'missing': missing,
        'h_effects': h_effects,
    })
