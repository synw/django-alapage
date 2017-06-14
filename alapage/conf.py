# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User


EDIT_MODES = (
              'visual',
              'code',
              )

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

USE_REVERSION=getattr(settings, 'ALAPAGE_USE_REVERSION', "reversion" in settings.INSTALLED_APPS)

BASE_TEMPLATE_PATH = getattr(settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')

EDIT_MODE = getattr(settings, 'ALAPAGE_EDIT_MODE', EDIT_MODES[0])
CODEMIRROR_KEYMAP = getattr(settings, 'ALAPAGE_CODEMIRROR_KEYMAP', 'default')

STAFFPAGES = "staffpages" in getattr(settings, 'INSTALLED_APPS')
