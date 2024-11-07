plateau = [" " for _ in range(9)]
joueur_courant = "X"

# Boucle principale
for tour in range(9):
    print(f"{plateau[0]} | {plateau[1]} | {plateau[2]}")
    print("--+---+--")
    print(f"{plateau[3]} | {plateau[4]} | {plateau[5]}")
    print("--+---+--")
    print(f"{plateau[6]} | {plateau[7]} | {plateau[8]}")

    # Demande au joueur de jouer
    mouvement = int(input(f"Joueur {joueur_courant}, choisissez une case (1-9): ")) - 1

    if plateau[mouvement] == " ":
        plateau[mouvement] = joueur_courant

        # Vérifie les conditions de victoire
        if (plateau[0] == plateau[1] == plateau[2] != " " or
                plateau[3] == plateau[4] == plateau[5] != " " or
                plateau[6] == plateau[7] == plateau[8] != " " or
                plateau[0] == plateau[3] == plateau[6] != " " or
                plateau[1] == plateau[4] == plateau[7] != " " or
                plateau[2] == plateau[5] == plateau[8] != " " or
                plateau[0] == plateau[4] == plateau[8] != " " or
                plateau[2] == plateau[4] == plateau[6] != " "):
            print(f"Le joueur {joueur_courant} gagne !")
            break

        # Change de joueur
        joueur_courant = "O" if joueur_courant == "X" else "X"
    else:
        print("Case déjà occupée, essayez à nouveau.")

else:
    print("Match nul !")