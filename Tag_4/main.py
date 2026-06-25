import random


stein = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)l
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

schere = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

spiel_bilder = [stein, papier, schere]

spieler_auswahl = int(input("Was wählst du?" + " " + "Schreibe 0 für Stein, 1 für Papier oder 2 für Schere\n"))
if spieler_auswahl >= 0 and spieler_auswahl <= 2:
    print(spiel_bilder[spieler_auswahl])

computer_auswahl = random.randint(0,2)
print("Auswahl des Gegners:")
print(spiel_bilder[computer_auswahl])

# Unentschieden
if spieler_auswahl == computer_auswahl:
    print("Es steht unentschieden")
# Spieler gewinnt
elif spieler_auswahl == 0 and computer_auswahl == 2: # Stein schlägt Schere
    print("Du hast gewonnen!")
elif spieler_auswahl == 1 and computer_auswahl == 0: # Papier schlägt Stein
    print("Du hast gewonnen!")
elif spieler_auswahl == 2 and computer_auswahl == 1: # Schere schlägt Papier
    print("Du hast gewonnen!")
# Alles andere bedeutet, der Computer gewinnt
else:
    print("Du hast verloren!")