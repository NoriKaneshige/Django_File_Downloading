# Django_File_Downloading

![download_as_it_is](download_as_it_is.gif)



![download_as_zip](download_as_zip.gif)

> ## models.py
``` python
from django.db import models


class UploadFile(models.Model):
    file = models.FileField('file')

    def __str__(self):
        return self.file.url
```

> ## admin.py
``` python
from django.contrib import admin
from .models import UploadFile

admin.site.register(UploadFile)
```

> ## views.py
``` python


```
