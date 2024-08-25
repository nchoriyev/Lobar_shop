import uuid
from django.db import models

class SaveMedia(object):
    def save_book_image_path(instance, filename):
        image_path = filename.split('.')[-1]
        return f"{uuid.uuid4()}.{image_path}"

class StatusChoicesPb(models.TextChoices):
    DRAFT = 'DRAFT', 'DRAFT'
    PUBLIC = 'PUBLIC', 'PUBLIC'

