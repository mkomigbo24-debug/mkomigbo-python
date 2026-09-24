# CREATE_ALL_MODELS_FIXED.py - FIXED KeyError self - double braces!
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# FIXED: Double braces for self.order
TEMPLATE = '''from django.db import models

class {ClassName}Page(models.Model):
    slug = models.SlugField(unique=True, max_length=200)
    title = models.CharField(max_length=500)
    content = models.TextField()
    php_file = models.CharField(max_length=500, blank=True)
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'slug']
        verbose_name = "{Verbose} Page"
        verbose_name_plural = "{Verbose} Pages"

    def __str__(self):
        return f"{{self.order:03d}} - {{self.title}} ({{self.slug}})"
'''

APPS = {
    "lang2_app": "Lang2",
    "africa_app": "AfricaApp",
    "uk_diaspora": "UkDiaspora",
    "about_app": "AboutApp",
    "people_app": "PeopleApp",
    "language1_app": "Language1App",
}

for folder, class_name in APPS.items():
    path = os.path.join(BASE, folder)
    os.makedirs(path, exist_ok=True)
    os.makedirs(os.path.join(path, "migrations"), exist_ok=True)
    open(os.path.join(path, "__init__.py"), "a").close()
    open(os.path.join(path, "migrations", "__init__.py"), "a").close()
    content = TEMPLATE.format(ClassName=class_name, Verbose=class_name)
    with open(os.path.join(path, "models.py"), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {folder}/models.py")

print("DONE! Now python manage.py check will work!")