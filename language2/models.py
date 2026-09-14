from django.db import models

# ========================
# LANGUAGE II - Grammar, Tones, Usage - Thesis Level
# ========================
class Tone(models.Model):
    TONE_TYPES = [
        ('high', 'High - ´  ákwá egg proof'),
        ('low', 'Low - \  àkwà cloth proof'),
        ('downstep', 'Downstep - ꜜ  ákwà cry proof'),
        ('rising', 'Rising - \u030c  tone'),
        ('falling', 'Falling - ^ tone'),
    ]
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)  # ´  \  ꜜ
    tone_type = models.CharField(max_length=20, choices=TONE_TYPES)
    ipa = models.CharField(max_length=20)
    example1 = models.CharField(max_length=100)  # ákwá
    meaning1 = models.CharField(max_length=100)  # egg
    example2 = models.CharField(max_length=100)  # àkwà
    meaning2 = models.CharField(max_length=100)  # cloth
    example3 = models.CharField(max_length=100, blank=True)  # ákwà
    meaning3 = models.CharField(max_length=100, blank=True)  # cry
    thesis_proof = models.TextField()  # How tone changes meaning - 3-way distinction
    audio = models.FileField(upload_to='tones/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} {self.symbol} - {self.example1} vs {self.example2}"

class GrammarRule(models.Model):
    title = models.CharField(max_length=200)  # Noun classes, Verb serialization
    category = models.CharField(max_length=50, choices=[
        ('noun', 'Noun - Class system'),
        ('verb', 'Verb - Serialization, Extensor'),
        ('pronoun', 'Pronoun - Chi and personhood'),
        ('adjective', 'Adjective'),
        ('syntax', 'Syntax - SVO but flexible'),
        ('morphology', 'Morphology - Affixes'),
    ])
    rule = models.TextField()  # Thesis level explanation
    examples = models.TextField()
    igbo_example = models.TextField()
    english_gloss = models.TextField()
    thesis_notes = models.TextField(blank=True)
    # Connection to your philosophy
    odinala_connection = models.TextField(blank=True)  # How grammar reflects Odinala worldview
    
    def __str__(self):
        return self.title

class Dialect(models.Model):
    name = models.CharField(max_length=100)  # Owerri, Onitsha, Nsukka, Arochukwu
    region = models.CharField(max_length=100)
    phonological_diff = models.TextField()  # How it differs in zh/gh/ts
    lexical_diff = models.TextField(blank=True)  # Different words
    example_words = models.TextField()  # Example: azhịa vs ahia vs afia
    # Your thesis: dialect proves missing phonemes
    thesis_proof = models.TextField(blank=True)  # Dialect X keeps zh, standard lost it
    
    def __str__(self):
        return f"{self.name} - {self.region}"

class Sentence(models.Model):
    igbo = models.TextField()
    ipa = models.CharField(max_length=300, blank=True)
    gloss = models.TextField()  # Word-by-word
    translation = models.TextField()
    tone_marked = models.CharField(max_length=300, blank=True)  # With tones ákwá
    grammar_notes = models.TextField(blank=True)
    dialect = models.ForeignKey(Dialect, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.igbo[:80]
