from django.shortcuts import render
from lang1.models import PresentAlphabet, MissingPhoneme
from religion.models import Religion
from language2.models import Dialect, Tone
from esoteric.models import EsotericTradition
from history.models import HistoricalPeriod
from culture.models import CulturalPractice

def home(request):
    present_all = PresentAlphabet.objects.all()
    missing_all = MissingPhoneme.objects.all()
    
    # CUỌ vs CHUỌ emphasis - diacritics proof
    cuo_examples = PresentAlphabet.objects.filter(symbol__in=['cuo','guo','kw','nw','cuọ','guo'])
    chuo_proof = PresentAlphabet.objects.filter(symbol__in=['ch','sh','gb','kp','chuo'])
    affricates = PresentAlphabet.objects.filter(category='affricate')
    labialized = PresentAlphabet.objects.filter(category='labialized_consonant')
    
    context = {
        'present': present_all,
        'missing': missing_all,
        'religions': Religion.objects.all(),
        'dialects': Dialect.objects.all(),
        'tones': Tone.objects.all(),
        'esoteric': EsotericTradition.objects.all()[:6],
        'history': HistoricalPeriod.objects.all()[:6],
        'culture': CulturalPractice.objects.all()[:6],
        'present_count': present_all.count(),  # 43!
        'missing_count': missing_all.count(),
        # CUO vs CHUO thesis data
        'cuo_examples': cuo_examples,
        'chuo_proof': chuo_proof,
        'affricates': affricates,
        'labialized': labialized,
    }
    return render(request, 'home.html', context)