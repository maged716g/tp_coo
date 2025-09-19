from django.db import models

# Create your models here.
class QuantiteMatierePremiere(models.Model):
	quantite = models.IntegerField()
	matiere_premiere = models.ForeignKey(MatierePremiere, on_delete=models.PROTECT,)
	def __init_(self, UtilisationMatierePremiere: "UtilisationMatierePremiere", ApprovisionnemoentMatierePremiere: "ApprovisionnemoentMatierePremiere"): 
		self.UtilisationMatierePremiere = UtilisationMatierePremiere 	
		self.ApprovisionnemoentMatierePremiere = ApprovisionnemoentMatierePremiere 

# class UtilisationMatierePremiere():
	# pass
	# def __init_(self, MatierePremiere): 
		# self.Metier = MatierePremiere

# class ApprovisionnemoentMatierePremiere():
	# localisation = models.CharField(max_length=100)
    # prix_unitaire = models.IntegerField()
    # delais        = models.IntegerField()
    # pass
    
# class Metier():
	# pass
	# nom = models.CharField(max_length=100)
	# remuneration = models.IntegerField()
	
# class RessourceHumaine():
	# metier = models.CharField(max_length=100)
	# quantite = models.IntegerField()
	# def __init_(self, Metier): 
		# self.Metier = Metier
	
# class MatierePremiere():
	# pass
	# nom = models.CharField(max_length=100)
	# stock = models.IntegerField()
	# emprise = models.CharField(max_length=100)
	
# #class Machine():


# #class Fabrication():





# #class Produit():


# #class Local():


# #class Energie():

# #class Localisation():

class Meta:
abstract = True

# if __name__ == "__main__":
