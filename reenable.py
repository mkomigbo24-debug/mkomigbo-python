import pathlib
p = pathlib.Path('core/settings.py')
t = p.read_text(encoding='utf-8')
t = t.replace(\"# 'django.middleware.csrf.CsrfViewMiddleware', # DISABLED FOR LOGIN\", \"'django.middleware.csrf.CsrfViewMiddleware',\")
p.write_text(t, encoding='utf-8')
print('CSRF RE-ENABLED')
