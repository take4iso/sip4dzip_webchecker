from django.db import models
from django.core.validators import FileExtensionValidator

class Fileupload(models.Model):
    filefield = models.FileField(
        upload_to = 'uploads/',
        verbose_name = 'attached file',
        null = True
    )
