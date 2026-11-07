#classes de personagem 
classes_player = {
    'Gladiador': {
        'strength': 7,
        'charisma': 4,
        'dexterity': 3,
    },
    'Gatuno': {
        'strength': 3,
        'charisma': 5,
        'dexterity': 7,
    },
    'Goliardo': {
        'strength': 3,
        'charisma': 7,
        'dexterity': 5,
    }
}

#escolha de classes

print('Escolha uma classe: Gladiador, Gatuno ou Goliardo ')
escolha = input('> ').lower()

if escolha in classes_player:
    stats_player = classes_player[escolha].copy()
    #cria uma variável que pega no dicionário que foi criado antes e,
    #com a escolha, dá "fetch" numa das classes que foram criadas e copia essa classe para esta nova variável

    print(f'Parabéns! Tornaste-te num {escolha.capitalize}!!!')
    print(f'os teus stats são: {stats_player}\n não há volta atrás...')
else:
    print('\n escolha inválida... Apenas membros da PLEBE não sabem ler!')
    stats_player = {'strength': 1, 'charisma': 1, 'dexterity': 1}
    print(f'Parabéns! Tornaste-te num PLEBEU!!!\n os teus stats são {stats_player}')

#início do Jogo

print('A floresta divide-se em três caminhos...')
print('1 - Gruta')
print('2 - Sombrasl')
print('3 - Ruínas')

path = input('Que caminho escolhes?')

#primeiro Caminho

if path == "Gruta":

    print('Chegas a uma passagem montanhosa. Uma enorme rocha bloqueia o caminho.')
    print('O terreno é instável e ouves pedras a cair ao longe...')

    if escolha == "gladiador":

        print("\nA tua força permite-te tentar mover a rocha.")
        print("1 - Tentar mover a rocha sozinho.")
        print("2 - Procurar uma forma de enfraquecer a pedra utilizando algo da floresta.")

        choice = input("Escolhe uma opção: 1, 2 ou nada..?: ")

        if choice == "1":
            print("\nCom toda a tua força, empurras a enorme rocha!")
            print("Após muito esforço, consegues movê-la, mas uma pedra cai sobre o teu braço.")

        elif choice == "2":
            print("\nEncontras um tronco resistente junto à berma do caminho.")
            print("Utilizas o tronco para atingir a rocha até esta começar a fraturar.")
            print("Com algum esforço, consegues libertar a passagem sem te magoares!")

        else:
            print("\nHesitaste demasiado e uma pedra desprende-se, atingindo-te!")
            
    elif escolha == "gatuno":

        print("\nA tua força permite-te tentar mover a rocha.")
        print("1 - Tentar mover a rocha sozinho.")
        print("2 - Procurar uma forma de enfraquecer a pedra utilizando algo da floresta.")

        choice = input("Escolhe uma opção: 1, 2 ou nada..?: ")

        if choice == "1":
            print("Tentas empurrar a pedra, mas não tens força suficiente...")
            print("Acabas por desistir e voltar atrás abandonando o local.")

        elif choice == "2":
            print("Tentas procurar")


        else:
            print("\nHesitaste demasiado e uma pedra desprende-se, atingindo-te!")

#------------------------------------------------------------------------------------------

# 1. Dicionário com as classes e os seus atributos (stats)
classes_disponiveis = {
    "gladiador": {"forca": 8, "agilidade": 3, "intel": 2},
    "gatuno": {"forca": 3, "agilidade": 8, "intel": 4}
}

def iniciar_jogo():
    print("Escolhe a tua classe: Gladiador ou Gatuno")
    escolha = input("> ").lower()
    
    if escolha in classes_disponiveis:
        player_class = escolha
        player_stats = classes_disponiveis[escolha].copy()
    else:
        print("Classe inválida. Vais ser um Gladiador por defeito.")
        player_class = "gladiador"
        player_stats = classes_disponiveis["gladiador"].copy()
        
    # Passamos a classe E os stats para as cenas
    cenario_floresta(player_class, player_stats)

def cenario_floresta(player_class, player_stats):
    print('\nA floresta divide-se em três caminhos...')
    print('1 - Gruta')
    print('2 - Sombras')
    print('3 - Ruínas')

    path = input('Que caminho escolhes? ')

    match path:
        case "1" | "gruta":
            cenario_gruta(player_class, player_stats)
        case "2" | "sombras":
            cenario_sombras(player_class, player_stats)
        case "3" | "ruínas" | "ruinas":
            cenario_ruinas(player_class, player_stats)
        case _:
            print('Opção inválida, tenta novamente.')
            cenario_floresta(player_class, player_stats)

def cenario_gruta(player_class, player_stats):
    print('\nChegas a uma passagem montanhosa. Uma enorme rocha bloqueia o caminho.')
    print('O terreno é instável e ouves pedras a cair ao longe...')
    
    print("\nO que decides fazer?")
    print("1 - Procurar um caminho alternativo a pé. (Opção Geral)")

    # Mostra opções APENAS a classes específicas
    if player_class == "gladiador":
        print("2 - [Gladiador] Destruir a rocha com força bruta.")
    elif player_class == "gatuno":
        print("2 - [Gatuno] Escalar a rocha rapidamente usando a agilidade.")

    choice = input("Escolhe uma opção (1 ou 2): ")

    match choice:
        case "1":
            print("\nDecides contornar a montanha a pé. Encontras um atalho seguro!")

        case "2":
            # Garantimos que a opção 2 faz coisas diferentes dependendo da classe
            if player_class == "gladiador":
                if player_stats["forca"] >= 7:
                    print("\n[Sucesso Gladiador] Partes a pedra ao meio com um golpe!")
                else:
                    print("\n[Falha] Não tens força suficiente para partir a rocha.")
                    cenario_gruta(player_class, player_stats)

            elif player_class == "gatuno":
                if player_stats["agilidade"] >= 7:
                    print("\n[Sucesso Gatuno] Escalas a rocha sem fazer barulho!")
                else:
                    print("\n[Falha] Escorregas nas pedras soltas.")
                    cenario_gruta(player_class, player_stats)

        case _:
            print("\nOpção inválida.")
            cenario_gruta(player_class, player_stats)

def cenario_sombras(player_class, player_stats):
    print("\nCaminhas em direção às sombras...")

def cenario_ruinas(player_class, player_stats):
    print("\nChegas às ruínas antigas...")

# Arranque do jogo
iniciar_jogo()


#------------------------------------------------------------------------------------------

def inicioFloresta(classes_player, stats_player):
    print('\nA floresta divide-se em três caminhos...')
    print('1 - Gruta')
    print('2 - Sombras')
    print('3 - Ruínas')
    
    path = input('Que caminho escolhes?').lower()

    match path:
        case '1' | 'gruta':
            pathGruta(classes_player, stats_player)
        case '2' | 'Ruinas':
            pathRuinas(classes_player, stats_player)
        case '1' | 'sombras':
            pathSombras(classes_player, stats_player)
        case _:
            print('Opção inválida, tenta novamente.')
            inicioFloresta(classes_player, stats_player)
            
def pathGruta(classes_player, stats_player):
    print('\nChegas a uma passagem montanhosa. Uma enorme rocha bloqueia o caminho.')
    print('O terreno é instável e ouves pedras a cair ao longe...\n')
    
    print('\nO teu instinto aventureiro chama-te!. Segues o barulho e encontras um monte de rochas')
    print('1 - Procurar um caminho alternativo a pé. (Opção Geral)')

    # Mostra opções APENAS a classes específicas
    if player_class == "gladiador":
        print("2 - [Gladiador] Destruir a rocha com força bruta.")
    elif classes_player == "goliardo":
        print("2 - [Goliardo] Tocar o alaúde para os espiritos da floresta.")
    escolha1 = input('Escolha uma opção (1 ou 2)\n> ')


#------------------------------------------------------------------------------------------


def pathGruta(classes_player, stats_player):
    print('\nChegas a uma passagem montanhosa. Uma enorme rocha bloqueia o caminho.')
    print('O terreno é instável e ouves pedras a cair ao longe...\n')
    
    print('\nO teu instinto aventureiro chama-te!. Segues o barulho e encontras um monte de rochas')
    print('1 - Procurar um caminho alternativo a pé.')

    # Mostra opções APENAS a classes específicas
    if classes_player == "gladiador":
        print("2 - [Gladiador] Usar força bruta para tentar mover a rocha.")
    elif classes_player == "goliardo":
        print("2 - [Goliardo] Tocar o alaúde...?")
    escolha1 = input('Escolha uma opção (1 ou 2)\n> ')
    
    match escolha1:
        case "1":
            print("\nDecides contornar o monte de rochas a pé. Encontras um atalho seguro!")
            
        case "2":
            if classes_player == "gladiador":
                print("\n[Sucesso Gladiador] Com os teus gloriosos músculos, acidentalmente, destróis a rocha")
            elif classes_player == "goliardo":
                print("\n[Sucesso Goliardo] A tua melodia chama a atenção dos espíritos!")
                print('Eles decidem mover a rocha por ti!')