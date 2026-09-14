from django.shortcuts import render
from lang1.models import PresentAlphabet, MissingPhoneme
from religion.models import Religion
from language2.models import Dialect, Tone
from esoteric.models import EsotericTradition
from history.models import HistoricalPeriod
from culture.models import CulturalPractice

def home(request):
    context = {
        'present': PresentAlphabet.objects.all()[:20],
        'missing': MissingPhoneme.objects.all(),
        'religions': Religion.objects.all(),
        'dialects': Dialect.objects.all(),
        'tones': Tone.objects.all(),
        'esoteric': EsotericTradition.objects.all()[:6],
        'history': HistoricalPeriod.objects.all()[:6],
        'culture': CulturalPractice.objects.all()[:6],
        'present_count': PresentAlphabet.objects.count(),
        'missing_count': MissingPhoneme.objects.count(),
    }
    return render(request, 'home.html', context)
