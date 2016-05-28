from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AlapageConfig(AppConfig):
    name = "alapage"
    verbose_name = _(u"Alapage")
    
    def ready(self):
        pass
        
        