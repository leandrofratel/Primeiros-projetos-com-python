import time, random
print('{:*^40}'.format(' Vamos Jogar? '))

print('PEDRA')
time.sleep(1)
print('PAPEL')
time.sleep(1)
print('TESOURA')

escolha = input('\nFaça sua Jogada: ')

opções = ['PEDRA', 'PAPEL', 'TESOURA']
npc = random.choice(opções)

if escolha.upper() == npc:
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;43mEMPATE!\033[m')

elif escolha.upper() == 'PEDRA' and npc == 'PAPEL':
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;41mMAQUINA GANHOU\033[m')

elif escolha.upper() == 'PEDRA' and npc == 'TESOURA':
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;42mJOGADOR VENCEDOR\033[m')

elif escolha.upper() == 'PAPEL' and npc == 'PEDRA':
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;42mJOGADOR VENCEDOR\033[m')

elif escolha.upper() == 'PAPEL' and npc == 'TESOURA':
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;41mMAQUINA GANHOU\033[m')

elif escolha.upper() == 'TESOURA' and npc == 'PEDRA':
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;42mJOGADOR VENCEDOR\033[m')

elif escolha.upper() == 'TESOURA' and npc == 'PAPEL':
    print(f'\nA maquina escolheu \033[4;31m{npc}\033[m')
    print(f'Você escolheu \033[4;32m{escolha.upper()}\033[m\n')
    print('\033[1;30;41mMAQUINA GANHOU\033[m')
else:
    print('Opção \033[7;30;46mIncorreta\033[m, tente novamente!')