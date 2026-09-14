from django.db import models

# ========================
# RELIGION - All Religions Deep Knowledge (Thesis Level)
# ========================
class Religion(models.Model):
    RELIGION_TYPES = [
        ('ATR', 'African Traditional - Odinala/Odinani'),
        ('Abrahamic', 'Abrahamic'),
        ('Dharmic', 'Dharmic - Eastern'),
        ('Indigenous', 'Indigenous'),
        ('New', 'New Religious Movement'),
        ('Esoteric', 'Esoteric Tradition'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, choices=RELIGION_TYPES)
    origin = models.CharField(max_length=100)
    founder = models.CharField(max_length=100, blank=True)
    founded_date = models.CharField(max_length=100, blank=True)
    followers_estimate = models.CharField(max_length=50, blank=True)
    overview = models.TextField()
    core_beliefs = models.TextField()
    cosmology = models.TextField(blank=True)
    thesis_notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class SacredText(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='texts')
    title = models.CharField(max_length=200)
    language_original = models.CharField(max_length=50)
    language_translated = models.CharField(max_length=100, blank=True)
    chapters = models.IntegerField(default=0)
    summary = models.TextField()
    download_link = models.URLField(blank=True)
    file = models.FileField(upload_to='sacred_texts/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.religion.name}"

class Doctrine(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='doctrines')
    title = models.CharField(max_length=200)
    explanation = models.TextField()
    igbo_comparison = models.TextField(blank=True)
    sources = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class Deity(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='deities', null=True, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    symbolism = models.TextField(blank=True)
    attributes = models.TextField(blank=True)
    is_alusi = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

# ========================
# ESOTERISM - Inner Teachings Across Traditions
# ========================
class EsotericTradition(models.Model):
    name = models.CharField(max_length=100)
    origin_tradition = models.CharField(max_length=100)
    parent_religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    inner_teaching = models.TextField()
    outer_teaching = models.TextField(blank=True)
    methods = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Symbol(models.Model):
    name = models.CharField(max_length=100)
    tradition = models.ForeignKey(EsotericTradition, on_delete=models.CASCADE, related_name='symbols', null=True, blank=True)
    image = models.ImageField(upload_to='symbols/', blank=True, null=True)
    meaning = models.TextField()
    esoteric_meaning = models.TextField(blank=True)
    usage = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
