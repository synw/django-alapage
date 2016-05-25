# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User


EDIT_MODES = (
              'visual',
              'mixed',
              'code',
              )

LAYOUTS = (('xs-12','Xs 12'),('smooth-md','Smooth md'))

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', False)
USE_REVERSION=getattr(settings, 'ALAPAGE_USE_REVERSION', False)

BASE_TEMPLATE_PATH = getattr(settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')

EDIT_MODE = getattr(settings, 'ALAPAGE_EDIT_MODE', EDIT_MODES[0])
CODEMIRROR_KEYMAP = getattr(settings, 'ALAPAGE_CODEMIRROR_KEYMAP', 'default')

ENABLE_PRIVATE_PAGES = getattr(settings, 'ALAPAGE_ENABLE_PRIVATE_PAGES', False)

