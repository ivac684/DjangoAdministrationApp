from django.db import models
from django.contrib.auth.models import AbstractUser

class Korisnici(AbstractUser):
    ROLES = (('prof', 'profesor'), ('stu', 'student'), ('admin', 'admin'))
    STATUS = (('none', 'None'), ('izv', 'izvanredni student'), ('red', 'redovni student'))
    role = models.CharField(max_length=50, choices=ROLES)
    status = models.CharField(max_length=50, choices=STATUS)


class Predmeti(models.Model):
    IZBORNI = (('DA', 'da'), ('NE', 'ne'))
    STATUS = (('upis', 'upisan'), ('da', 'polozen'), ('ne', 'izgubio potpis'))
    name = models.CharField(max_length=50)
    kod = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    ects = models.IntegerField()
    sem_red = models.IntegerField()
    sem_izv = models.IntegerField()
    izborni = models.CharField(max_length=50, choices=IZBORNI)
    nositelj = models.ForeignKey(Korisnici, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Upisi(models.Model):
    student_id = models.ForeignKey(Korisnici, on_delete=models.CASCADE)
    predmet_id = models.ForeignKey(Predmeti, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=Predmeti.STATUS)