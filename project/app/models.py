from django.db import models

my_model_choices = [
    ('normal', 'Normal'),
    ('extra', 'Extra'),
    ('additional', 'Additional'),
    ('cosmic', 'Cosmic'),
]
class MyModel(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    type = models.CharField(null=True, choices=my_model_choices, max_length=255)
