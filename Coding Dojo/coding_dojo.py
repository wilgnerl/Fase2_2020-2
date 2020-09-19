# Integrantes
# Wilgner Lopes
# Raphael Lahiry
# Bruno Domingues
# Pietro


# Declarando biblioteca
from random import *

# Nome do personagem
nome = input('Qual o seu nome grande heroi(a)? ')

#Pontos de vida
HP = 200

#Pontos de magia
mana = 50

#Catalogo de dano
def calc_dmg(id_weapon):
    if id_weapon == 1: # Machado
        return randint(10, 20)         #[i for i in range(0,15,1)]
    elif id_weapon == 2: # Espada
        return randint(5, 10)           #([i for i in range(15,25,1)]
    elif id_weapon == 3: # Adaga
        return randint(1, 5)              #[i for i in range(4,45,1)]

#Armas
armas = {
    1:'Machado',
    2:'Espada',
    3:'Adaga'
}

#Armadura
armadura = {
    'Magica':0.05,
    'Fisica':0.1,
}


# Magia
# Caso 1: self damage - 10%
# Caso 2: nada acontece - 20%
# Caso 3: dano normal - 50%
# Caso 4: dano critico - 20%

# 5 mana pra usar
def use_magic(mana):
    if mana < 5:
        return "Sem mana para uso de magia!"
    else:
        mana -= 5
        casos_magia = [1, 2, 2, 3, 3, 3, 3, 3, 4, 4]
        out = choice(casos_magia)

        return mana, out

#escolha da arma
arma = randint(1,3)
dano_da_arma = calc_dmg(arma)

print('Olá, {}. Voce recebeu a arma {} . Sua vida atual '.format(nome, armas[arma]))
print('Sua arma causa {}'.format(dano_da_arma))
print('Sua armadura anula {} de dano magico e {} de dano físico.',format(armadura['Magica'],armadura['Fisica']))
