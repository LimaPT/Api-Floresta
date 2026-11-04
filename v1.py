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
    #cria uma variável que pega no dicionário que foi criado antes
    #e, com a escolha, dá "fetch" numa das classes que foram criadas e copia essa classe para esta nova variável
    print(f'Parabéns! Tornaste-te num {escolha.capitalize}!!!')
    print(f'os teus stats são: {stats_player}\n não há volta atrás...')
else:
    print('\nescolha inválida... Apenas membros da PLEBE não sabem ler!')
    stats_player = {'strength': 1, 'charisma': 1, 'dexterity': 1}
    print(f'Parabéns! Tornaste-te num PLEBEU!!!\nos teus stats são {stats_player}')

