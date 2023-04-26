from django.db import models
from django.db.models import ImageField
from django_extensions.db.models import (
	TimeStampedModel
)

import uuid

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyModel(models.Model):
    image_url = ImageField(upload_to=upload_to, blank=True, null=True)

# class Item(TimeStampedModel, ModelId):
#     notes = TextField(blank=True)
#     samplesheet = FileField(blank=True, default='')
 
#     def __str__(self) -> str:
#         return self.name

# class ModelId(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)

#     class Meta:
#         abstract = True

