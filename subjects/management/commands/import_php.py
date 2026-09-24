# subjects/management/commands/import_php.py
# FIXED: No page_count field - matches DB!
from pathlib import Path
from django.core.management.base import BaseCommand

PHP_PAGES_ROOT = Path("C:/mkomigbo/mkomigbo-php-source/public/subjects/pages")

APP_MAP = {
    "history": ("history", "HistoryPage"),
    "culture": ("culture", "CulturePage"),
    "language1": ("language1_app", "Language1AppPage"),
    "language2": ("lang2_app", "Lang2Page"),
    "religion": ("religion", "ReligionPage"),
    "esoterism": ("esoterism", "EsoterismPage"),
    "tradition": ("tradition", "TraditionPage"),
    "biafra": ("biafra", "BiafraPage"),
    "slavery": ("slavery", "SlaveryPage"),
    "nigeria": ("nigeria", "NigeriaPage"),
    "africa": ("africa_app", "AfricaAppPage"),
    "pogrom": ("pogrom", "PogromPage"),
    "uk": ("uk_diaspora", "UkDiasporaPage"),
    "struggles": ("struggles", "StrugglesPage"),
    "resistance": ("resistance", "ResistancePage"),
    "europe": ("europe", "EuropePage"),
    "arabs": ("arabs", "ArabsPage"),
    "about": ("about_app", "AboutAppPage"),
    "people": ("people_app", "PeopleAppPage"),
    "persons": ("persons", "PersonsPage"),
    "spirituality": ("esoterism", "EsoterismPage"),
}

class Command(BaseCommand):
    help = "Import 122 PHP files as is"

    def handle(self, *args, **options):
        if not PHP_PAGES_ROOT.exists():
            alt = Path("C:/mkomigbo/mkomigbo-python/../mkomigbo-php-source/public/subjects/pages")
            # Try second path
            root = alt if alt.exists() else PHP_PAGES_ROOT
        else:
            root = PHP_PAGES_ROOT

        from subjects.models import Subject, Page
        
        total = 0
        for subject_folder in sorted(root.iterdir()):
            if not subject_folder.is_dir():
                continue
            subj_name = subject_folder.name
            if subj_name not in APP_MAP:
                continue
            
            app_label, model_name = APP_MAP[subj_name]
            subject_obj, _ = Subject.objects.update_or_create(
                slug=subj_name,
                defaults={"name": subj_name.title(), "description": f"{subj_name} - {len(list(subject_folder.glob('*.php')))} pages", "order": 0}
            )
            
            try:
                app_module = __import__(f"{app_label}.models", fromlist=[model_name])
                ModelClass = getattr(app_module, model_name)
            except Exception as e:
                ModelClass = None

            order = 0
            for php_file in sorted(subject_folder.glob("*.php")):
                order += 1
                try:
                    content = php_file.read_text(encoding="utf-8", errors="ignore")
                except:
                    content = php_file.read_text(encoding="latin-1", errors="ignore")
                
                slug = f"{subj_name}-{php_file.stem}"
                title = php_file.stem.replace("_", " ").replace("-", " ").title()
                
                Page.objects.update_or_create(
                    slug=slug,
                    defaults={
                        "subject": subject_obj,
                        "title": title,
                        "content": content,
                        "order": order,
                        "is_published": True,
                    }
                )
                
                if ModelClass:
                    try:
                        ModelClass.objects.update_or_create(
                            slug=slug,
                            defaults={
                                "title": title,
                                "content": content,
                                "php_file": str(php_file),
                                "order": order,
                                "is_published": True,
                            }
                        )
                    except Exception as e:
                        self.stdout.write(f"  App error {slug}: {e}")

                total += 1
                self.stdout.write(f"  {slug}")

        self.stdout.write(self.style.SUCCESS(f"DONE! Imported {total} PHP files - amuzhi untouched!"))