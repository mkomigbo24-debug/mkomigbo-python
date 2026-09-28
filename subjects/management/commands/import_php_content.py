import os
from pathlib import Path
from django.core.management.base import BaseCommand
from subjects.models import Subject, Page
import re

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
CONTENT_RAW = BASE_DIR / 'content_raw'

FOLDER_TO_SUBJECT = {
    'ISUAMA': ('history', 'History - Isuama & Igbo Origin'),
    'ODINALA': ('religion', 'Religion - Ọdịnàla EKE ORIE AFO NKWO'),
    'IGBO_FRATANITY': ('culture', 'Culture - Igbo Fraternity'),
    'mkomigbo': ('language1', 'Language1 - Ndebe & Phonemes'),
}
FOLDER_ORDER = ['ISUAMA', 'ODINALA', 'IGBO_FRATANITY', 'mkomigbo']

def read_docx_text(path):
    try:
        import zipfile, xml.etree.ElementTree as ET
        with zipfile.ZipFile(path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            texts = []
            for elem in tree.iter():
                if elem.tag.endswith('}t'):
                    if elem.text:
                        texts.append(elem.text)
            return '\n\n'.join(texts)[:10000]
    except Exception as e:
        return f"[Could not read {path.name}: {e}]"

def read_html_file(path):
    try:
        return path.read_text(encoding='utf-8', errors='ignore')[:15000]
    except:
        return f"[HTML error {path.name}]"

class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f"Scanning {CONTENT_RAW}")
        for folder, (slug, name) in FOLDER_TO_SUBJECT.items():
            Subject.objects.get_or_create(
                slug=slug,
                defaults={'name': name, 'description': f'From PHP {folder}', 'page_count':0, 'order': FOLDER_ORDER.index(folder), 'is_public':True}
            )
        total=0
        for folder_name in FOLDER_ORDER:
            folder_path = CONTENT_RAW / folder_name
            if not folder_path.exists(): continue
            subject_slug,_ = FOLDER_TO_SUBJECT[folder_name]
            subject = Subject.objects.get(slug=subject_slug)
            files = sorted(folder_path.glob('*.*'))
            print(f"\n{folder_name} -> {subject_slug} : {len(files)} files")
            for idx, file_path in enumerate(files,1):
                slug = re.sub(r'[^a-z0-9]+', '-', file_path.stem.lower()).strip('-')
                slug = f"{subject_slug}-{slug[:40]}-{idx}"
                if Page.objects.filter(slug=slug).exists(): continue
                if file_path.suffix=='.docx':
                    content=read_docx_text(file_path)
                elif file_path.suffix=='.html':
                    content=read_html_file(file_path)
                else:
                    content=f"[{file_path.name}]"
                Page.objects.create(
                    subject=subject, slug=slug,
                    title=file_path.stem.replace('_',' ').title(),
                    subtitle=f"From PHP {folder_name} - {file_path.name}",
                    content=f"<div><h2>{file_path.stem}</h2><pre>{content[:8000]}</pre></div>",
                    order=idx, is_published=True
                )
                total+=1
                print(f"  + {slug}")
        for subject in Subject.objects.all():
            subject.page_count=subject.pages.count()
            subject.save()
            print(f"Subject {subject.slug}: {subject.page_count} pages")
        print(f"\nDone! Imported {total} pages")