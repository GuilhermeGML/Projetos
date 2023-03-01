from genius import *
from fire_leviathan import *
from ice_leviathan import *
from ghost_leviathan import *
import time
from random import randint

print('''Bem Vindo ao mundo criado por Genius que talvez será expandido porem 
isso ainda é algo incerto.
Bom o Reino de Internect estavá infectado por um Mega Virús, o The BigMente, este vírus 
infectou todo o sistema, porem ele teve um leve erro, um deslize, uma falha
um indivíduo conseguiu sobreviver e este é o protagonista, é meio que seu nome verdadeiro
não foi identificado, mas BigMente chamou de Genius por conseguir fugir de sua infecção.
E é assim que começa toda nossa história, The BigMente e seus Suditos contra Genius.''')
print('''É Genius acordou apos anos em coma, isso o salvou do BigMente, porem ele
já tinha dominado tudo e denominado 3 Suditos leais, que provaram sua força, 
mas nem eles juntos conseguiriam derrotar BigMente, pois seu poder era tão perfeito
que nada parecia que ia conseguir derrotá-lo. Porém BigMente sentiu medo pela 
primeira vez quando Genius despertou de seu sono, apos anos de estudo Genius percebeu
que ao se desligar e voltar ele aprende tudo muito mais facil, isso ele descobriu 
apos um acidente que o deixou em coma por 5 anos, e assim ele mesmo se pos a
dormir por 3005 anos o que resultou dele não ser infectado pelo virús pois ele estava
desconectado.''')
print('A partir de agora é com você')
print('-' * 20)
time.sleep(2)

genius = Genius(15, 'Espada', 'Adaga', 'Sombra')
print('Dados de Genius')
print(f'Vida = {genius.vida}')
print(f'Amra 1 = {genius.arma1}')
print(f'Arma 2 = {genius.arma2}')
print(f'Poder = {genius.poder}')
print('-' * 20)

# Primeiro Chefe
while True:
    print('Agora inicie a sua jornada')
    print('Seu primeiro boss para enfrentar é o Fire Leviathan')

    fire = Fire_Leviathan(30, 'Lança', 'Bola de Fogo', 'Erupção')

    print('Você começa atacando ele distraido. Escolha sua habilidade')
    damage = int(input('Arma1 [1], Arma[2], Poder[3]'))
    if damage == 1:
        dano = genius.dano_a1()
        print(f'Genius causou {dano} de dano')
        fire.vida -= dano
    elif damage == 2:
        dano = genius.dano_a2()
        print(f'Genius causou {dano} de dano')
        fire.vida -= dano
    elif damage == 3:
        dano = genius.pdr()
        print(f'Genius causou {dano} de dano')
        fire.vida -= dano

    print('Agora q Fire Leviatha percebeu sua presença após seu ataque, ele revida usando')
    test = randint(1, 3)
    if test == 1:
        dano = fire.dano_a1()
        print(f'Fire causou {dano} de dano')
        genius.vida -= dano
    elif test == 2:
        dano = fire.pdr1()
        print(f'Fire causou {dano} de dano')
        genius.vida -= dano
    elif test == 3:
        dano = fire.pdr2()
        print(f'Fire causou {dano} de dano')
        genius.vida -= dano

    print('Que começe o Duelo')
    while True:
        damage = int(input('Esolha seu ataque Arma1 [1], Arma[2], Poder[3]'))
        if damage == 1:
            dano = genius.dano_a1()
            print(f'Genius causou {dano} de dano')
            fire.vida -= dano
        elif damage == 2:
            dano = genius.dano_a2()
            print(f'Genius causou {dano} de dano')
            fire.vida -= dano
        elif damage == 3:
            dano = genius.pdr()
            print(f'Genius causou {dano} de dano')
            fire.vida -= dano
        test = randint(1, 3)
        if test == 1:
            dano = fire.dano_a1()
            print(f'Fire causou {dano} de dano')
            genius.vida -= dano
        elif test == 2:
            dano = fire.pdr1()
            print(f'Fire causou {dano} de dano')
            genius.vida -= dano
        elif test == 3:
            dano = fire.pdr2()
            print(f'Fire causou {dano} de dano')
            genius.vida -= dano
        if genius.vida <= 0:
            print('Fire Leviathan Ganhou')
            break
        if fire.vida <= 0:
            print('Genius Ganhou')
            break
        print(f'Vida de Genius ={genius.vida}')
        print(f'Vida de Fire ={fire.vida}')
    if genius.vida <= 0:
        break

    print('Como recompensa por derrotar o Fire você recebe 12 pontos de vida')
    genius.vida += 12
    print(f'Sua vida atual é de {genius.vida}')

    # Segundo Chefe
    time.sleep(2)
    print('-' * 20)
    print('Sua jornada ainda não acabou')
    print('Proseguindo o caminho você enconra o Ghost Leviathan')
    ghost = Ghost_Leviathan(10, 'Invocação', 'Ivulnerabilidade')
    print('Ele percebe sua presença e o ataca ')
    test = randint(1, 2)
    if test == 1:
        dano = ghost.pdr_1()
        print(f'Ghost causou {dano} de dano')
        genius.vida -= dano
    elif test == 2:
        dano = ghost.pdr_2()
        print(f'Ghost se cura {dano} de vida')
        ghost.vida += dano

    print('Sua vez de contra atacar')
    while True:
        damage = int(input('Arma1 [1], Arma[2], Poder[3]'))
        if damage == 1:
            dano = genius.dano_a1()
            print(f'Genius causou {dano} de dano')
            ghost.vida -= dano
        elif damage == 2:
            dano = genius.dano_a2()
            print(f'Genius causou {dano} de dano')
            ghost.vida -= dano
        elif damage == 3:
            dano = genius.pdr()
            print(f'Genius causou {dano} de dano')
            ghost.vida -= dano

        test = randint(1, 2)
        if test == 1:
            dano = ghost.pdr_1()
            print(f'Ghost causou {dano} de dano')
            genius.vida -= dano
        elif test == 2:
            dano = ghost.pdr_2()
            print(f'Ghost se cura {dano} de vida')
            ghost.vida += dano

        if genius.vida <= 0:
            print('Ghost Leviathan Ganhou')
            break
        if ghost.vida <= 0:
            print('Genius Ganhou')
            break
        print(f'Vida de Genius = {genius.vida}')
        print(f'Vida de Ghost = {ghost.vida}')
    if genius.vida <= 0:
        break

    print('Como recompensa por derrotar o Ghost você recebe 20 pontos de vida')
    genius.vida += 20
    print(f'Sua vida atual é de {genius.vida}')

    # Terceiro Boss Último
    time.sleep(2)
    print('-' * 20)
    print('Bom soldado você sobreviveu até aqui, foi forte e superou os inimigos')
    print('Agora siga ao próximo inimigo')
    ice = Ice_Leviathan(25, 'Machado', 'Lanças Gelidas', 'Nevasca')
    test = randint(1, 3)
    if test == 1:
        dano = ice.dano_a_1()
        print(f'Ice causou {dano} de dano')
        genius.vida -= dano
    elif test == 2:
        dano = ice.pd_1()
        print(f'Ice causou {dano} de dano')
        genius.vida -= dano
    elif test == 3:
        dano = ice.pd_2()
        print(f'Ice causou {dano} de dano')
        genius.vida -= dano

    print('Ice o ataca desprevinido ganhando vantagem no duelo')
    print('Ao ser atingido rapidamente você revida')
    while True:
        damage = int(input('Esolha seu ataque Arma1 [1], Arma[2], Poder[3]'))
        if damage == 1:
            dano = genius.dano_a1()
            print(f'Genius causou {dano} de dano')
            ice.vida -= dano
        elif damage == 2:
            dano = genius.dano_a2()
            print(f'Genius causou {dano} de dano')
            ice.vida -= dano
        elif damage == 3:
            dano = genius.pdr()
            print(f'Genius causou {dano} de dano')
            ice.vida -= dano
        test = randint(1, 3)
        if test == 1:
            dano = ice.dano_a_1()
            print(f'Ice causou {dano} de dano')
            genius.vida -= dano
        elif test == 2:
            dano = ice.pd_1()
            print(f'Ice causou {dano} de dano')
            genius.vida -= dano
        elif test == 3:
            dano = ice.pd_2()
            print(f'Ice causou {dano} de dano')
            genius.vida -= dano

        if genius.vida <= 0:
            print('Ice Leviathan Ganhou')
            break
        if ice.vida <= 0:
            print('Genius Ganhou')
            break
        print(f'Vida de Genius = {genius.vida}')
        print(f'Vida de Ice ={ice.vida}')
    if genius.vida <= 0:
        break
    elif ice.vida <= 0:
        break

if genius.vida <= 0:
    print('Infelizmente você foi derrotado')
else:
    print('Parabéns todos os lideres foram derrotados')
    time.sleep(5)
    print('''E aleatóriamente todos foram salvos, pois The BigMente era apenas uma entidade
criado pelos Leviathans para desviar a atenção que eram eles q estavam atrás de toda a 
infecção''')
    print('Assim se encerra a jornada de Genius')
    print('Quem sabe apereça novas aventuras para ele')