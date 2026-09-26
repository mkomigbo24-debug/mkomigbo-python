from django.conf import settings
def site_branding(request):
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'Nkomigbo'),
        'OLD_NAME': getattr(settings, 'OLD_NAME', 'Mkomigbo'),
        'SITE_TAGLINE': getattr(settings, 'SITE_TAGLINE', 'Nko mi Igbo - Meditation on Igbo'),
    }
