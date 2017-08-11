from django.conf import settings
from django.contrib.auth.models import User


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

USE_REVERSION = getattr(settings, 'ALAPAGE_USE_REVERSION',
                        "reversion" in settings.INSTALLED_APPS)

BASE_TEMPLATE_PATH = getattr(
    settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')

CODE_MODE = getattr(settings, 'ALAPAGE_CODE_MODE', True)
CODEMIRROR_KEYMAP = getattr(settings, 'ALAPAGE_CODEMIRROR_KEYMAP', 'default')
