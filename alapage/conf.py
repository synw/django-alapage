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
USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', "jssor" in settings.INSTALLED_APPS)

BASE_TEMPLATE_PATH = getattr(settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')

templates_names = (
                   ("alapage/default.html", _(u'Normal')),
                   ("alapage/smooth.html", _(u'Smooth')),
                   ("alapage/blank.html", _(u'Blank')),
                   )
TEMPLATES_NAMES = getattr(settings, 'ALAPAGE_TEMPLATES_NAMES', templates_names)

EDIT_MODE = getattr(settings, 'ALAPAGE_EDIT_MODE', EDIT_MODES[0])
CODEMIRROR_KEYMAP = getattr(settings, 'ALAPAGE_CODEMIRROR_KEYMAP', 'default')

