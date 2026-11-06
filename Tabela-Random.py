# Tabela-Random.py
def tplebeu ():
    import random
    tabela = random.randint(1, 100)
    match tabela:
        case range(1, 4):
            # +1 Stretgth
            print("Ganhas +1 Strength!")
        case range(5, 8):
            # +1 Dexterity
            print("Ganhas +1 Dexterity!")
        case range(9, 12):
            # +1 Carisma
            print("Ganhas +1 Charisma!")
        case range(13, 17):
            # +3 Random Stat
            print("Ganhas +3 Stat!")
        case range(18, 27):
            # -2 Random Stat
            print("Perdes -2 Stat!")
        case range(28, 35):
            # End
            print("Aparecem os 4 cavaleiros do apocalipse e morres!")
        case range(36, 45):
            # If nas ruínas, voltas para gruta / If nas gruta voltas para sombra / If nas sombras, voltas para ruína
            print("Foste para ____!")   
        case range(46, 55):
            # -1 Stretgth 
            print("Perdes -1 Strength!")
        case range(56, 65):
            # -1 Charisma
            print("Perdes -1 Charisma!")
        case range(66, 75):
            # -1 Dexterity
            print("Perdes -1 Dexterity!")
        case range(76, 87):
            # voltar 2 escolhas atrás
            print("Deixaste cair o teu, porta chaves favorito. Tens de voltar 2 escolhas atrás.")
        case range(88, 93):
            # + Cartão da Escola
            print("Ganhas o cartão da escola")
        case range(94, 96):
            # Mudas de classe
            print("Tornas-te (Goliardo/Gatuno/Gladiador)")
        case range(97, 100):
            # Fim Meh
            print("Perdes-te...")

def tnormal ():
    import random
    tabela = random.randint(1, 100)
    match tabela:
        case range(1, 7):
            # +1 Stretgth
            print("Ganhas +1 Strength!")
        case range(8, 14):
            # +1 Dexterity
            print("Ganhas +1 Dexterity!")
        case range(15, 21):
            # +1 Carisma
            print("Ganhas +1 Charisma!")
        case range(22, 28):
            # +3 Random Stat
            print("Ganhas +3 Stat!")
        case range(29, 34):
            # -2 Random Stat
            print("Perdes -2 Stat!")
        case range(35, 40):
            # End
            print("Aparecem os 4 cavaleiros do apocalipse e morres!")
        case range(41, 48):
            # If nas ruínas, voltas para gruta / If nas gruta voltas para sombra / If nas sombras, voltas para ruína
            print("Foste para ____!")   
        case range(49, 54):
            # -1 Stretgth 
            print("Perdes -1 Strength!")
        case range(55, 60):
            # -1 Charisma
            print("Perdes -1 Charisma!")
        case range(61, 66):
            # -1 Dexterity
            print("Perdes -1 Dexterity!")
        case range(67, 78):
            # voltar 2 escolhas atrás
            print("Deixaste cair o teu, porta chaves favorito. Tens de voltar 2 escolhas atrás.")
        case range(79, 90):
            # + Cartão da Escola
            print("Ganhas o cartão da escola")
        case range(91, 92):
            # Mudas de classe
            print("Tornas-te (Goliardo/Gatuno/Gladiador)")
        case range(93, 98):
            # Fim Meh
            print("Perdes-te...")
        case range(99, 100):
            #Tornas-te Plebeu
            print("Tornas-te Plebeu!")

