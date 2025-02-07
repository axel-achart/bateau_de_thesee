# Job du Jour : Le Bateau de Thésée et ses réparations

# Classe Part du bateau
class Part:
    # Constructeur Initialisation
    def __init__(self, name, materiel):
        self.name = name  
        self.materiel = materiel

    # Changer le matériel
    def change_material(self, new_materiel):
        self.materiel = new_materiel
    
    # Afficher uen description du produit
    def __str__(self):
        return f"La {self.name} est fait en {self.materiel}"

# Classe Ship
class Ship:
    # Constructeur Initialisation
    def __init__(self, name, parts):
        self.name = name
        self.__parts = parts
        self.display_state()
    
    # Afficher
    def display_state(self, parts):
        return f"Ship : {self.name}"
    






# Instancier la partie du bâteau
coque = Part("Coque", "Bois")

# Afficher la description pièce
print(coque)

# Changer le matériel de la pièce
coque.change_material("Polymère")

# Re-afficher la description de la pièce
print(coque)