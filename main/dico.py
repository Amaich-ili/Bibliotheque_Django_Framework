import random
class Auteur:
    def __init__(self, nom, naissance, nationnalite):
        self.nom = nom
        self.date_naissance = naissance
        self.nationnalite = nationnalite
   
    def __str__(self):
        return f"nom de l'auteur{self.auteur} dete de naissance:{self.date_naissance} {self.nationnalite}"   

class Livre:
    def __init__(self,titre, image, auteur, categorie):
        self.categorie = categorie
        self.titre = titre
        self.img = image
        self.auteur = auteur
    
    def __str__(self):
        return f"{self.titre} \n {self.nom} \n categorie {self.categorie}"
    
    
    def __eq__(self, livre) -> bool:
        if self.categorie == livre.categorie:
            return True
        else:
            return False
    
    def livre_dico(self):
        livre = {
            "livre": {
            "categorie": self.categorie,
            "titre": self.titre ,
            "image":self.img
             },
          "auteur": {
              "nom": self.auteur.nom,
              "date de naissance": self.auteur.date_naissance,
              "natoinnalité" : self.auteur.nationnalite}
               }
        return livre

class Roman_policier(Livre):
    def __init__(self, titre, image, auteur):
        super().__init__( titre, image, auteur, "policier")
       

class Science(Livre):
    def __init__(self, titre, image, auteur):
        super().__init__( titre, image, auteur, "science")
       
        
    
class Cuisine(Livre):
    def __init__(self, titre, image, auteur):
        super().__init__(titre, image, auteur, "cuisine")  
       
class Conte_enfant(Livre):
    def __init__(self, titre, image, auteur):
        super().__init__(titre, image, auteur, "conte enfants")
      
def dico():
    dico ={}
    i = 1
    with open("C:/Users/amaic/Documents/GitHub/Notre_Projet/main/livre.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
                elet = line.split(",")
                if elet[0] == "1":
                    auteur = Auteur(elet[3], elet[4], elet[5])
                    livre = Livre(elet[1], elet[2], auteur, "policier")
                    livre_dico = livre.livre_dico()
                    dico[i] = livre_dico
                    i  += 1
                elif elet[0] == "2":
                    auteur = Auteur(elet[3], elet[4], elet[5])
                    livre = Livre(elet[1], elet[2], auteur, "science")
                    livre_dico = livre.livre_dico()
                    dico[i] = livre_dico 
                    i  += 1
                elif elet[0] == "3":
                    auteur = Auteur(elet[3], elet[4], elet[5])
                    livre = Livre(elet[1], elet[2], auteur, "cuisine")
                    livre_dico = livre.livre_dico()
                    dico[i] = livre_dico 
                    i  += 1
                elif elet[0] == "4":
                    auteur = Auteur(elet[3], elet[4], elet[5])
                    livre = Livre(elet[1], elet[2], auteur, "conte enfants")
                    livre_dico = livre.livre_dico()
                    dico[i] = livre_dico 
                    i += 1
    return dico                            

dicto = dico()

for i in dicto:
    print(dicto[i]["livre"])

                        
