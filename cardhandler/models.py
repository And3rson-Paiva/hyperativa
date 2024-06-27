
from django.db import models

class Card(models.Model):
    card_number = models.CharField(max_length=19, unique=True)  # Assumindo 19 dígitos como o máximo para números de cartão

    def __str__(self):
        return self.card_number
