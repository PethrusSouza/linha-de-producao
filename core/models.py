from django.db import models


class Item(models.Model):
    MEDIDAS_CHOICES = [
        ('BL', 'BL'),
        ('TL', 'TL'),
        ('M²', 'M²'),
        ('CM', 'CM'),
    ]

    nome = models.CharField(max_length=100)
    p_12 = models.IntegerField(null=True, blank=True)
    descricao_item = models.CharField(max_length=300)
    medidas = models.CharField(max_length=2, choices=MEDIDAS_CHOICES)
    acabamento = models.CharField(max_length=300)

    def __str__(self):
        return self.nome
