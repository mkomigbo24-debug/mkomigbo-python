import sqlite3
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from lang1.models import PresentAlphabet

# Connect to old SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute("SELECT symbol, ipa, example, meaning, category, is_dropped, thesis_note FROM lang1_presentalphabet")
rows = cursor.fetchall()

print(f"Found {len(rows)} rows in old SQLite")

for row in rows:
    symbol, ipa, example, meaning, category, is_dropped, thesis_note = row
    PresentAlphabet.objects.get_or_create(
        symbol=symbol,
        defaults={
            'ipa': ipa,
            'example': example,
            'meaning': meaning,
            'category': category,
            'is_dropped': bool(is_dropped),
            'thesis_note': thesis_note or ''
        }
    )

print(f"PostgreSQL now has: {PresentAlphabet.objects.count()} rows")
conn.close()
