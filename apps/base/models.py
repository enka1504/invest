import uuid
from django.db import models


class BaseModel(models.Model):
    class Meta:
        ordering = ['-fecha_reg']

    identifier = ''
    uuid = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
    folio = models.CharField(max_length = 25, unique = True, null = True, editable = False)
    fecha_reg = models.DateTimeField(auto_now_add = True)
    fecha_mod = models.DateTimeField(auto_now = True)
    activo = models.BooleanField(default = True, editable = False)
    is_published = models.BooleanField(default = False)
    is_disabled = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        #self.identifier = '{}-{}'.format(self.identifier, str(self.uuid).upper()[:8])
        #self.folio = self.identifier
        self.identifier = self.identifier or self.__class__.identifier
        self.folio = '{}-{}'.format(self.identifier, str(self.uuid).upper()[:8])
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True