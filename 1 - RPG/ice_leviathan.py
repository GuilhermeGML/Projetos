from random import randint


class Ice_Leviathan:
    def __init__(self, vida, arma, poder1, poder2):
        self.vida = vida
        self.arma = arma
        self.poder1 = poder1
        self.poder2 = poder2

    def dano_a_1(self):
        d = randint(1, 4)
        return d

    def pd_1(self):
        d1 = randint(0, 3)
        d2 = randint(0, 3)
        d3 = randint(0, 3)
        d4 = randint(0, 3)
        d = d1 + d2 + d3 + d4
        return d

    def pd_2(self):
        d = randint(0, 2)
        return d

# ice = Ice_Leviathan(25, 'Machado', 'Lanças Gelidas', 'Nevasca')
# print('Dados de Ice Leviathan')
# print(f'Vida = {ice.vida}')
# print(f'Amra = {ice.arma}')
# print(f'Poder 1 = {ice.poder1}')
# print(f'Poder 2 = {ice.poder2}')
# print('-'*20)
# ice.dano_a1()
# ice.pdr1()
# ice.pdr2()
