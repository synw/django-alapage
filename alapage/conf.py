# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User

ALAPAGE_LAYOUTS = (('xs-12','Xs 12'),('smooth-md','Smooth md'))
ALAPAGE_THEMES = (
                  ('dark','Dark'),
                  ('light','Light'),
                  )

LAYOUTS = getattr(settings, 'ALAPAGE_LAYOUTS', ALAPAGE_LAYOUTS)
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)
USE_JSSOR=getattr(settings, 'ALAPAGE_USE_JSSOR', False)
USE_PRESENTATIONS=getattr(settings, 'ALAPAGE_USE_PRESENTATIONS', False)
USE_THEMES = getattr(settings, 'ALAPAGE_USE_THEMES', False)
BASE_TEMPLATE_PATH = getattr(settings, 'ALAPAGE_BASE_TEMPLATE_PATH', 'base.html')
USE_THEMES = getattr(settings, 'ALAPAGE_USE_THEMES', False)
THEMES = getattr(settings, 'ALAPAGE_THEMES', ALAPAGE_THEMES)
MONITORING_LEVEL=getattr(settings, 'ALAPAGE_MONITORING_LEVEL', 0)

