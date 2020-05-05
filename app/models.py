from django.db import models


class UploadFile(models.Model):
    file = models.FileField('file')

    def __str__(self):
        return self.file.url