import os, re, pathlib
from django.core.management.base import BaseCommand
from subjects.models import Subject, Page

OLD_PAGES = r"C:\mkomigbo\old-php\public\subjects\pages"

def extract_body(content):
    # Try new format: 'body_html' => <<<HTML ... HTML,
    m = re.search(r"'body_html'\s*=>\s*<<<HTML(.*?)HTML,", content, re.S)
    if m:
        return m.group(1).strip()
    
    # Old format: echo '<html>' or echo "<html>" or plain HTML after PHP
    # Remove PHP tags
    content_no_php = re.sub(r'<\?php.*?\?>', '', content, flags=re.S)
    # Extract all echo '...' ; 
    echoes = re.findall(r"echo\s+['\"](.*?)['\"]\s*;", content_no_php, re.S)
    if echoes:
        # Join echoes, replace \n, \'
        body = "\n".join(echoes)
        body = body.replace("\\'", "'").replace('\\"', '"').replace("\\n", "\n")
        return body.strip()
    
    # Fallback: if file contains HTML directly
    if '<p>' in content or '<div' in content:
        # Strip php opening
        body = re.sub(r'<\?php.*', '', content, flags=re.S).strip()
        if len(body) > 50:
            return body
    
    return content[:5000]  # last resort

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        imported = 0
        for subject_slug in os.listdir(OLD_PAGES):
            s_path = os.path.join(OLD_PAGES, subject_slug)
            if not os.path.isdir(s_path):
                continue
            try:
                subject_obj = Subject.objects.get(slug=subject_slug)
            except:
                continue
            
            for page_file in os.listdir(s_path):
                if not page_file.endswith('.php'):
                    continue
                slug = page_file.replace('.php','')
                full = os.path.join(s_path, page_file)
                raw = pathlib.Path(full).read_text(encoding='utf-8', errors='ignore')
                
                # Extract title - try array format first
                m_title = re.search(r"'title'\s*=>\s*'([^']+)'", raw)
                if m_title:
                    title = m_title.group(1)
                else:
                    # Old format - try to guess from filename
                    title = slug.replace('_',' ').capitalize()
                
                body = extract_body(raw)
                # Clean leftover PHP artifacts: '; echo '
                body = re.sub(r"';\s*echo\s+'", "\n", body)
                body = re.sub(r"';\s*echo\s+\"", "\n", body)
                body = body.replace("'; echo '", "")
                
                Page.objects.update_or_create(
                    subject=subject_obj,
                    slug=slug,
                    defaults={'title': title, 'body_html': body, 'nav_order': 1}
                )
                imported += 1
                print(f"Fixed {subject_slug}/{slug} -> {len(body)} chars - {title}")
        
        print(f"Done! Fixed {imported} pages - echo codes removed!")