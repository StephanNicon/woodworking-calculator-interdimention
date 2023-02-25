tailleDeLaPlanche = float(input("Taille de la grande planche ? "))
epaisseurDesAutresPlanches = int(input("Quelle est l'epaisseur des atres planches ? "))
nombreDePlanches = int(input("Nombre de planches"))

distanceEntrePlanches = (tailleDeLaPlanche - (epaisseurDesAutresPlanches*nombreDePlanches))/(nombreDePlanches-1)
print("La distance entre chaque planche est de "+str(distanceEntrePlanches))