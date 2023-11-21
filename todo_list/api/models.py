from django.db import models
from django.utils.translation import gettext as _


class ToDo(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.title}'
    