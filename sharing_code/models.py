from django.db import models
from django.shortcuts import reverse
import uuid


class Snippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    code = models.TextField()
    langs = [('Text', 'None'),
             ('Python', 'Python'),
             ('JavaScript', 'Javascript'),
             ]
    lang = models.CharField(max_length=18, choices=langs, default='Text')
    date = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = "Snippets"
        verbose_name = "Snippet"
        verbose_name_plural = "Snippets"

    def __str__(self):
        return self.id.hex
