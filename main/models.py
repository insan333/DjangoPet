from django.db import models
from django.db.models.fields import CharField,IntegerField,TimeField


class Trolleibus(models.Model):
    murshrut=CharField(max_length=200)
    murshrut_number=CharField(max_length=200)
    capacity=IntegerField()
    price=IntegerField()
    start_work=TimeField()
    stop_work=TimeField()
    def __str__(self) -> str:
        return self.murshrut_number

class Taxi(models.Model):
    company=CharField(max_length=200)
    option=CharField(max_length=200)
    average_price=IntegerField()
    start_work=TimeField()
    stop_work=TimeField()
    def __str__(self) -> str:
        return self.company

class Sprinter(models.Model):
    murshrut=CharField(max_length=200)
    murshrut_number=CharField(max_length=200)
    capacity=IntegerField()
    price=IntegerField()
    start_work=TimeField()
    stop_work=TimeField()
    def __str__(self) -> str:
        return self.murshrut_number












