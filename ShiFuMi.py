
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:23:24 2020

@author: achille
"""
import random
import time

rock = 1
paper = 2
scissors = 3
names = { rock: "Pierre", paper: "Feuille", scissors: "Ciseaux"}
rules = { rock: scissors, paper : rock, scissors: paper}

player_score = 0
computer_score = 0
print("test")
def start():
    print ("On va jouer à un jeu ! ... (Rire machiavellique)... Shifumi, aussi appelé Pierre-Feuille-Ciseaux")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        player = input('Pierre = 1\nPapier = 2\nCiseaux = 3\n Choisissez un mouvement :')
        print (player)
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print ("Oups, j'ai pas compris ce que tu voulais Jean Louis, recommence et soi pas con cette fois !")

def result(player, computer):
    print ("Shi")
    time.sleep(1)
    print('Fu')
    time.sleep(1)
    print("Mi!")
    time.sleep(0.5)
    print ("L'ordinateur a joué : {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print ("Egalité")
    else:
        if rules[player] == computer:
            print("Ta victoire était assurée Jean Louis")
            player_score+=1
        else:
            print("L'ordinateur a été plus fort que toi Jean Louis ! Tes Mauvais ! Tu sais pas jouer !")
            computer_score+=1
        
def play_again():
    answer = input("Tu veux retenter ta chance ? Oui/Non/evidemment fdp")
    if answer in ("O", "o", "Y", "y", "Oui", "oui", "Yes", "yes", "evidemment fdp"):
        return answer
    else:
        print ("Merci d'avoir joué, on se refait une partie quand tu veux !")

def scores():
    global player_score, computer_score
    print ("HIGH SCORES")
    print ("Joueur Humain : ", player_score)
    print ("Joueur Ordinateur : ", computer_score)
    
    if __name__ == '__main__':
        start()
