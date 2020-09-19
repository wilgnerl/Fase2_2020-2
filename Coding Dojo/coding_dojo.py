# Integrantes
# Wilgner Lopes
# Raphael Lahiry
# Bruno Domingues
# Pietro


# Declarando biblioteca
from time import *
from random import *

# Nome do personagem
nome = input('Qual o seu nome grande heroi(a)? ')

#Pontos de vida
HP = 200

#Pontos de magia
mana = 50

#Catalogo de dano
dano_machado = randint(10, 20)         #[i for i in range(0,15,1)]
dano_espada = randint(5, 10)           #([i for i in range(15,25,1)]
dano_adaga = randint(1, 5)              #[i for i in range(4,45,1)]

#Armas
armas = {
    'Machado': 1,
    'Espada': 2,
    'Adaga': 3
}

#Armadura
armadura = {
    'Magica':0.05,
    'Fisica':0.1,
}


#Danos

#