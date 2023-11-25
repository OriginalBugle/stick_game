import os

#déclaration des variables
joueur=1
i=1
nombre_batonnets=21

os.system("cls")
print('''    _                               _             _               _                                    _   
   (_)   ___   _   _  __  __     __| |  _   _    | |__     __ _  | |_    ___    _ __    _ __     ___  | |_ 
   | |  / _ \ | | | | \ \/ /    / _` | | | | |   | '_ \   / _` | | __|  / _ \  | '_ \  | '_ \   / _ \ | __|
   | | |  __/ | |_| |  >  <    | (_| | | |_| |   | |_) | | (_| | | |_  | (_) | | | | | | | | | |  __/ | |_ 
  _/ |  \___|  \__,_| /_/\_\    \__,_|  \__,_|   |_.__/   \__,_|  \__|  \___/  |_| |_| |_| |_|  \___|  \__|
 |__/                                                                                                      ''')
print("21")
print("[] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []")


#boucle while
while i==1:
    
    # Joueur
    print("Joueur ",joueur)
    batonnets_input=input("combien voulez vous enlever ?(1, 2, 3):")
    

    if batonnets_input=="1" or batonnets_input=="2" or batonnets_input=="3":
        batonnets_input=int(batonnets_input)
        os.system("cls")
        nombre_batonnets=nombre_batonnets-batonnets_input
        print(nombre_batonnets)
        print(nombre_batonnets*"[] ")
        
        if nombre_batonnets==1 or nombre_batonnets<1:
            print("Joueur",joueur,"à gagné")
            break

        if joueur==1:
            joueur=2
        else:
            joueur=1           
        
    else:
        print("nombre invalide")
