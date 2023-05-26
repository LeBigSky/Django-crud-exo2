from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Student(models.Model):
    class Genre(models.TextChoices):
        Homme = 'Masculin'
        Femme = 'Féminin'
    nom= models.CharField( max_length=50)
    age= models.IntegerField(validators=[
            MaxValueValidator(35),
            MinValueValidator(18)
        ])
    genre= models.CharField(choices=Genre.choices,max_length=15)
    email= models.EmailField()

    class Meta:
        db_table= 'students'