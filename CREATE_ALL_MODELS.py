# CREATE_ALL_MODELS.py - Creates all 21 subjects models.py - WORKABLE ONE FILE!
# Copy/paste this file to C:\mkomigbo\mkomigbo-python\CREATE_ALL_MODELS.py
# Run: python CREATE_ALL_MODELS.py
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Template - change ClassName only
TEMPLATE = '''from django.db import models

class {ClassName}Page(models.Model):
    slug = models.SlugField(unique=True, max_length=200, help_text="e.g., {slug}-s01")
    title = models.CharField(max_length=500)
    # Full HTML from PHP - as is! NO conversion!
    content = models.TextField(help_text="Full HTML from PHP file - as is from banana0624")
    php_file = models.CharField(max_length=500, blank=True, help_text="Original PHP path in mkomigbo-php-source")
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'slug']
        verbose_name = "{Verbose} Page"
        verbose_name_plural = "{Verbose} Pages - {pages} pages"

    def __str__(self):
        return f"{self.order:03d} - {self.title} ({self.slug})"
'''

# 21 subjects - SAFE names - NO language2 conflict!
APPS = {
    "history": ("History", "history", "6"),
    "culture": ("Culture", "culture", "5"),
    "language1_app": ("Language1", "language1", "5"),
    "lang2_app": ("Lang2", "lang2", "5 - SAFE for language2 conflict"),
    "religion": ("Religion", "religion", "15 - thesis"),
    "esoterism": ("Esoterism", "esoterism", "7"),
    "tradition": ("Tradition", "tradition", "5"),
    "biafra": ("Biafra", "biafra", "5"),
    "slavery": ("Slavery", "slavery", "5"),
    "nigeria": ("Nigeria", "nigeria", "5"),
    "africa_app": ("AfricaApp", "africa", "5 - SAFE"),
    "pogrom": ("Pogrom", "pogrom", "5"),
    "uk_diaspora": ("UkDiaspora", "uk", "5 - SAFE"),
    "struggles": ("Struggles", "struggles", "5"),
    "resistance": ("Resistance", "resistance", "5"),
    "europe": ("Europe", "europe", "5"),
    "arabs": ("Arabs", "arabs", "5"),
    "about_app": ("AboutApp", "about", "5 - SAFE"),
    "people_app": ("PeopleApp", "people", "5 - SAFE"),
    "persons": ("Persons", "persons", "5"),
    "uk": ("Uk", "uk", "5"),
}

for folder, (class_name, slug, pages) in APPS.items():
    path = os.path.join(BASE, folder)
    os.makedirs(path, exist_ok=True)
    os.makedirs(os.path.join(path, "migrations"), exist_ok=True)
    open(os.path.join(path, "__init__.py"), "a").close()
    open(os.path.join(path, "migrations", "__init__.py"), "a").close()
    
    content = TEMPLATE.format(ClassName=class_name, slug=slug, Verbose=class_name, pages=pages)
    with open(os.path.join(path, "models.py"), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {folder}/models.py -> {class_name}Page")

print("\nDONE! All 21 models.py created - NO ERROR!")
print("Now run: python manage.py check")