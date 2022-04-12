from django.db import models


class Bron(models.TextChoices):
    KUNLIK = 'Kunlik band qilish'
    SOATLIK = 'Soatlik band qilish'


class Room_Type(models.TextChoices):
    LYUKS = "Lyuks"
    BIZNES = "Biznes"
    KVARTERA = "Kvartera"
