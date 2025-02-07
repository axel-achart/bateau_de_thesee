# Job du Jour : Le Bateau de Thésée et ses réparations

# Classe Part du bateau
class Part:
    # Constructeur Initialisation
    def __init__(self, name, material):
        self.name = name  
        self.material = material

    # Changer le matériel
    def change_material(self, new_material):
        self.material = new_material
    
    # Afficher uen description du produit
    def __str__(self):
        return f"{self.name} est fait en {self.material}"


# Instancier les 4 parties
mat = Part("Mat simple", "Bois")
voile = Part("Voile simple", "Bois")
coque = Part("Coque simple", "Bois")
ancre = Part("Ancre simple", "Bois")



# Classe Ship
class Ship:
    # Constructeur Initialisation
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mat": mat,
            "Voile": voile,
            "Coque": coque,
            "Ancre": ancre
        }

    # Lister les pièces du bâteau
    def display_state(self):
        print()
        print(f"Bâteau : {self.name}")
        for name, part in self.__parts.items():
            print(f"Pièce : {name} -> {part}")

    # Remplacer une pièce existante par une autre piece
    def replace_part(self, part_name, new_part):
        # Enregistrer dans l'historique
        with open('history.txt', 'a') as history:
            history.write(f"Modification : {part_name} --> {new_part}\n")
        self.__parts[part_name] = new_part

    # Changer le matériau d'une pièce
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            # Enregistrer dans l'historique
            with open('history.txt', 'a') as mat_hist:
                mat_hist.write(f"Modification materiel : {part_name} => {new_material}\n")
            self.__parts[part_name].change_material(new_material)
        else:
            print(f"Erreur: {part_name} n'existe pas dans le bateau.")

# Classe RacingShip
class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed
    
    def display_speed(self):
        print(f"Vitesse maximale : {self.max_speed} noeuds")

# Menu main
def menu():
    while True:
        print("\n< - - - - MENU - - - - >")
        print("Le bâteau par défaut comporte un mat, une voile, une coque, une ancre et tout en bois.")
        print("1. Nomme ton bâteau.")
        print("2. Remplace une pièce existante par une autre.")
        print("3. Change le matériel d'une partie existante.")
        print("4. Ajouter une vitesse maximale.")
        print("5. Description du bâteau")
        print("6. Afficher l'historique")
        print("7. Quitter")

        # Choix à faire
        choix = int(input("\nEntrez votre choix : "))

        if choix in (1,2,3,4,5,6,7):
            if choix == 1:
                while True:
                    try:
                        name = str(input("\nEntrez le nom à donner : "))
                        bateau = Ship(name)
                        bateau.display_state()
                        break
                    except ValueError:
                        print("Entrez un nom valide")
            elif choix == 2:
                old_piece = str(input("Entrez la pièce à changer : "))
                new_piece = str(input("Entrez le nom de la nouvelle pièce : "))
                new_mater = str(input("Entrez le matériel de la nouvelle pièce : "))
                neww_partt = Part(new_piece, new_mater)
                bateau.replace_part(old_piece, neww_partt)
                bateau.display_state()
            elif choix == 3:
                part_namme = str(input("Entrez la pièce à modifier : "))
                neww_mmater = str(input("Entrez le nouveau matériel : "))
                bateau.change_part(part_namme, neww_mmater)
                bateau.display_state()
            elif choix == 4:
                speed_max = int(input("Entrez la vitesse maximale : "))
                bateau = RacingShip(bateau.name, speed_max)
                bateau.display_state() 
                bateau.display_speed()
            elif choix == 5:
                bateau.display_state() 
            elif choix == 6:
                # Lecture du fichier
                with open('history.txt', 'r') as history:
                    historic = history.read().splitlines()
                # Affichage de l'historique si pas vide
                if historic:
                    print("\nHistorique des modifications :")
                    for h in historic:
                        print(h)
                else:
                    print("Historique vide")
            # Quitter le code
            elif choix == 7:
                print()
                exit()
        else:
            print("\nEntrez un choix valide !")

# Programme executé sécu
if __name__ == '__main__':
    menu()