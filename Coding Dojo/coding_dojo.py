# Integrantes
# Wilgner Lopes
# Raphael Lahiry
# Bruno Domingues
# Pietro

# Declarando bibliotecas
from random import randint, choice

# Armas
armas = {
    1: {"nome": "Adaga", "min_dmg": 1, "max_dmg": 5},
    2: {"nome": "Espada", "min_dmg": 5, "max_dmg": 10},
    3: {"nome": "Machado", "min_dmg": 10, "max_dmg": 20}
}

# Armaduras
armaduras = {
    1: {"tipo": "fraca", "abs_fisico": 0.1, "abs_magica": 0.05},
    2: {"tipo": "media", "abs_fisico": 0.2, "abs_magica": 0.10},
    3: {"tipo": "forte", "abs_fisico": 0.3, "abs_magica": 0.15},
}

class Hero:
    def __init__(self, name, armas):
        self.name = name
        self.hp = 200
        self.mana = 50
        self.weapon = randint(1, 3)
        self.armor = randint(1, 3)
        self.hpotion = 5
        self.mpotion = 2
        self.hrestore = 20
        self.mrestore = 10
    def ataque(self):
        dano = armas[self.weapon]
        return dano
    def ataque_mag(self, mana, Villain):
        mana, ataque = use_magic(self.mana)
        if ataque == 1:
            self.hp -= 10
        elif ataque == 2:
            pass
        elif ataque == 3:
            Villain.hp -= 25
        elif ataque == 4:
            Villain.hp -= 50


class Villain:
    def __init__(self, name, hweapon, harmor):
        self.name = name
        self.hp = 200
        self.mana = 50
        self.weapon = randint(1, hweapon)
        self.armor = randint(1, harmor)
        self.hpotion = randint(5, 10)
        self.mpotion = randint(2, 5)
        self.hrestore = 20
        self.mrestore = 10
    def ataque_fis(self):
        dano = armas[self.weapon]
        return dano
    def ataque_mag(self, mana, Hero):
        mana, ataque = use_magic(self.mana)
        if ataque == 1:
            self.hp -= 10
        elif ataque == 2:
            pass
        elif ataque == 3:
            Hero.hp -= 25
        elif ataque == 4:
            Hero.hp -= 50
            

# Caso 1: self damage - 10%
# Caso 2: nada acontece - 20%
# Caso 3: dano normal - 50%
# Caso 4: dano critico - 20%

# Nome do personagem
hnome = input('Escolha um nome para seu personagem: ')
heroi = Hero(hnome, armas)

print(f"Olá {heroi.name}!\n")
print("Informações iniciais:")
print(f"Pontos de vida: {heroi.hp}")
print(f"Pontos de mana: {heroi.mana}")
arma_heroi = armas[heroi.weapon]
print(f"Sua arma é: {arma_heroi['nome']}. Ela dá dano entre {arma_heroi['min_dmg']} e {arma_heroi['max_dmg']} HP!")
armadura_heroi = armaduras[heroi.armor]
print(f"Sua armadura é do tipo {armadura_heroi['tipo']}. Ela absorve {armadura_heroi['abs_fisico']*100}% de dano fisico e {armadura_heroi['abs_magica']*100}% de dano magico!")
print(f"Você tem {heroi.hpotion} poções de vida que restauram {heroi.hrestore} pontos de vida cada e {heroi.mpotion} que restauram {heroi.mrestore} de mana cada!")

def print_status(h):
    print("Status: \n")
    print(f"Health points: {h}")


class Villain:
    def __init__(self, name, hweapon, harmor):
        self.name = name
        self.hp = 200
        self.mana = 50
        self.weapon = randint(1, hweapon)
        self.armor = randint(1, harmor)


#Catalogo de dano
def calc_dmg(id_weapon):
    if id_weapon == 1:  # Machado
        return randint(10, 20)  # [i for i in range(0,15,1)]
    elif id_weapon == 2:  # Espada
        return randint(5, 10)  # ([i for i in range(15,25,1)]
    elif id_weapon == 3:  # Adaga
        return randint(1, 5)  # [i for i in range(4,45,1)]

#Armas


#Armadura
armadura = {
    'Magica': 0.05,
    'Fisica': 0.1,
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

print('Escolha sua ação')

opcao = input('Ataque ou poção ? ')
if opcao == 'ataque':
    tipo = input ('Ataque fisico ou magico ? ')
    if tipo == 'fisico':
        dano = Hero.ataque()
        print(f'Vida do vilão {Villain.hp-dano}')
    else:
        dano = Hero.ataque_mag(self.mana)
        print(f'Vida do vilão {Villain.hp-dano}')
        
        