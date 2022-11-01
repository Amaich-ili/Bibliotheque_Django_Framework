from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Categories(models.Model):
    nom = models.CharField(max_length= 100)

    def __str__(self) -> str:
        return self.nom

class Liste_livre(models.Model):
    ref = models.ForeignKey(Categories, on_delete= models.CASCADE)
    image = models.ImageField(upload_to="images/")
    titre = models.CharField(max_length= 100)
    sujets = models.CharField(max_length= 300)
    auteur = models.CharField(max_length= 100)
    type = models.CharField(max_length= 100)
    due_back = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f"{self.titre} \n{self.sujets} "

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

class Lecteur(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    nom =  models.CharField(max_length= 100)
    prenom = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 100)
    email = models.CharField(max_length= 100)
    profil_pic = models.ImageField(upload_to="images_pic/", null=True)
    date_creation = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom


