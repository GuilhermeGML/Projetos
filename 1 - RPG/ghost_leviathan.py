from random import randint


class Ghost_Leviathan:
    def __init__(self, vida, poder1, poder2):
        self.vida = vida
        self.pdr1 = poder1
        self.pdr2 = poder2

    def pdr_1(self):
        d1 = randint(0, 2)
        d2 = randint(0, 2)
        d3 = randint(0, 2)
        d = d1 + d2 + d3
        return d

    def pdr_2(self):
        d = randint(1, 4)
        return d
ghost = Ghost_Leviathan(10, 'Invocação', 'Ivulnerabilidade')
# print('Dados de Genius')
# print(f'Vida = {ghost.vida}')
# print(f'Poder 1 = {ghost.poder1}')
# print(f'Poder 2 = {ghost.poder2}')
# print('-'*20)

ghost.pdr_1()
ghost.pdr_2()
