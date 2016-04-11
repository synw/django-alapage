# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User

ALAPAGE_THEMES = (
                  ('dark','Dark'),
                  ('light','Light'),
                  )

EDIT_MODES = (
              'visual',
              'mixed',
              'code',
              )

LAYOUTS = (('xs-12','Xs 12'),('smooth-md','Smooth md'))

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)
USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', False)
USE_REVERSION=getattr(settings, 'ALAPAGE_USE_REVERSION', False)
USE_PRESENTATIONS=getattr(settings, 'ALAPAGE_USE_PRESENTATIONS', False)
USE_THEMES = getattr(settings, 'ALAPAGE_USE_THEMES', False)
BASE_TEMPLATE_PATH = getattr(settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')
USE_THEMES = getattr(settings, 'ALAPAGE_USE_THEMES', False)
THEMES = getattr(settings, 'ALAPAGE_THEMES', ALAPAGE_THEMES)
MONITORING_LEVEL=getattr(settings, 'ALAPAGE_MONITORING_LEVEL', 0)
EDIT_MODE = getattr(settings, 'ALAPAGE_EDIT_MODE', EDIT_MODES[0])

