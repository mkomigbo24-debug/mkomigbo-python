from django.db import models

# ========================
# RELIGION - All Religions Deep Knowledge
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
    name = models.CharField(max_length=100)  # Odinala, Christianity, Islam, Buddhism etc
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, choices=RELIGION_TYPES)
    origin = models.CharField(max_length=100)  # Igbo, Middle East, India
    founder = models.CharField(max_length=100, blank=True)
    founded_date = models.CharField(max_length=100, blank=True)  # 9th century, 1st century CE etc
    followers_estimate = models.CharField(max_length=50, blank=True)
    overview = models.TextField()  # Thesis level argument
    core_beliefs = models.TextField()
    cosmology = models.TextField(blank=True)  # How world is viewed
    thesis_notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class SacredText(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='texts')
    title = models.CharField(max_length=200)  # Bible, Quran, Ofo Na Ogu, I Ching
    language_original = models.CharField(max_length=50)
    language_translated = models.CharField(max_length=100, blank=True)
    chapters = models.IntegerField(default=0)
    summary = models.TextField()
    download_link = models.URLField(blank=True)  # Free download like mkomigbo.com
    file = models.FileField(upload_to='sacred_texts/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.religion.name}"

class Doctrine(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='doctrines')
    title = models.CharField(max_length=200)  # Chi, Reincarnation, Trinity, Karma
    explanation = models.TextField()  # Thesis level
    igbo_comparison = models.TextField(blank=True)  # Compare to Odinala
    sources = models.TextField(blank=True)

class Deity(models.Model):
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='deities', null=True, blank=True)
    name = models.CharField(max_length=100)  # Chukwu, Ani, Amadioha, Jesus, Allah
    role = models.CharField(max_length=200)  # Creator, Earth goddess, Thunder
    symbolism = models.TextField(blank=True)
    attributes = models.TextField(blank=True)
    # For Odinala specific
    is_alusi = models.BooleanField(default=False)

# ========================
# ESOTERISM - Inner Teachings
# ========================
class EsotericTradition(models.Model):
    name = models.CharField(max_length=100)  # Afa, Hermeticism, Kabbalah, Sufism
    origin_tradition = models.CharField(max_length=100)  # Igbo Afa, Egyptian, Jewish
    parent_religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    inner_teaching = models.TextField()  # Secret/inner meaning
    outer_teaching = models.TextField(blank=True)  # Public meaning
    methods = models.TextField(blank=True)  # Divination, meditation etc

class Symbol(models.Model):
    name = models.CharField(max_length=100)  # Ofo, Nsibidi, Ankh, Yin Yang
    tradition = models.ForeignKey(EsotericTradition, on_delete=models.CASCADE, related_name='symbols', null=True, blank=True)
    image = models.ImageField(upload_to='symbols/', blank=True, null=True)
    meaning = models.TextField()
    esoteric_meaning = models.TextField(blank=True)
    usage = models.TextField(blank=True)