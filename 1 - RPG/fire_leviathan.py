from random import randint


class Fire_Leviathan:
    def __init__(self, vida, arma, poder1, poder2):
        self.vida = vida
        self.arma = arma
        self.poder1 = poder1
        self.poder2 = poder2

    def dano_a1(self):
        d = randint(1, 4)
        return d

    def pdr1(self):
        d1 = randint(0, 3)
        d2 = randint(0, 3)
        d = d1 + d2
        return d

    def pdr2(self):
        d = randint(0, 2)
        return d

#fire = Fire_Leviathan(30, 'Lança', 'Bola de Fogo', 'Erupção')
# print('Dados de Ice Leviathan')
# print(f'Vida = {fire.vida}')
# print(f'Amra = {fire.arma}')
# print(f'Poder 1 = {fire.poder1}')
# print(f'Poder 2 = {fire.poder2}')
# print('-'*20)
# fire.dano_a1()
# fire.pdr1()
# fire.pdr2()

