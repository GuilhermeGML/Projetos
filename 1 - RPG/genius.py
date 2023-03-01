from random import randint


class Genius:
    def __init__(self, vida, arma1, arma2, poder):
        self.vida = vida
        self.arma1 = arma1
        self.arma2 = arma2
        self.poder = poder


    def dano_a1(self):
        d = randint(1, 6)
        return d


    def dano_a2(self):
        d1 = randint(1, 4)
        d2 = randint(1, 4)
        d = d1 + d2
        return d

    def pdr(self):
        d = randint(1, 6)
        return d

# genius = Genius(15, 'Espada', 'Adaga', 'Sombra')
# print('Dados de Genius')
# print(f'Vida = {genius.vida}')
# print(f'Amra 1 = {genius.arma1}')
# print(f'Arma 2 = {genius.arma2}')
# print(f'Poder = {genius.poder}')
# print('-'*20)
# genius.dano_a1()
# genius.dano_a2()
# genius.pdr()
