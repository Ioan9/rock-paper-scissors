# FINALMETE EU ESPEREI ANOS POR ISSO HAHAHAHAHH JOKENPO!!!!!!

import random
import time

print('JOKENPO!')
print('1 = pedra')
print('2 = papel')
print('3 = tesoura')
items = ('pedra', 'papel', 'tesoura')
player = int(input(":"))
maquina = int(random.randint(1, 3))

if player == 1 and maquina == 2:
    print('JOGADOR: PEDRA')
    time.sleep(2)
    print('MAQUINA: PAPEL')
    print('MAQUINA WINS}')

elif player == 1 and maquina == 3:
    print('JOGADOR: PEDRA')
    time.sleep(2)
    print(f'MAQUINA: TESOURA')
    print('JOGADOR WINS')

elif player == 2 and maquina == 1:
    print(f'JOGADOR: PAPEL')
    time.sleep(2)
    print(f'MAQUINA: PEDRA')
    print('JOGADOR WINS')

elif player == 2 and maquina == 3:
    print('JOGADOR: PAPEL')
    time.sleep(2)
    print('MAQUINA: TESOURA')
    print('MAQUINA WINS')

elif player == 3 and maquina == 1:
    print('JOGADOR: TESOURA')
    time.sleep(2)
    print('MAQUINA: PEDRA')
    print('MAQUINA WINS')

elif player == 3 and maquina == 2:
    print('JOGADOR: TESOURA')
    time.sleep(2)
    print('MAQUINA: PAPEL')
    print('JOGADOR WINS')

else:
    print('JOGADOR E MAQUINA JOGARAM IGUAl')

print(player, maquina)
