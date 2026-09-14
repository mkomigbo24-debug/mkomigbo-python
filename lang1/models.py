from django.db import models

class PresentAlphabet(models.Model):
    CATEGORY_CHOICES = [
        ('single', 'Single Letter'),
        ('digraph', 'Digraph - Wrongly as Letter'),
        ('diacritic', 'Diacritic Letter'),
        ('labialized_consonant', 'Labialized - cuo vs chuo proof'),
        ('affricate', 'Affricate - ts, dz, zh, gh'),
        ('labialized_digraph', 'Labialized Digraph - Real Phoneme'),
    ]
    symbol = models.CharField(max_length=10)
    ipa = models.CharField(max_length=20)
    example = models.CharField(max_length=50)
    meaning = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    is_dropped = models.BooleanField(default=False)
    thesis_note = models.TextField(blank=True)
    audio = models.FileField(upload_to='phonemes/', blank=True, null=True)
    def __str__(self):
        return self.symbol

class MissingPhoneme(models.Model):
    symbol = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=[
        ('tone', 'Tone'),
        ('syllabic_nasal', 'Syllabic Nasal'),
        ('labialized', 'Labialized - cuo, guo, kuo proof'),
        ('original', 'Original Script'),
        ('affricate_missing', 'Affricate Missing - zh, gh, tsara, azhia'),
        ('palatalized', 'Palatalized - zhia, ghia, nyia'),
    ])
    ipa = models.CharField(max_length=20)
    example = models.CharField(max_length=100)
    meaning_diff = models.CharField(max_length=200)
    reason_missing = models.TextField()
    audio = models.FileField(upload_to='missing/', blank=True, null=True)
    
    def __str__(self):
        return self.symbol
