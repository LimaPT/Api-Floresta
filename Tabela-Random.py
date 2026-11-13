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

            #Tabelas Random
def tplebeu ():
    tabela = random.randint(1, 100)
    match tabela:
        case range(1, 5):
            add_attribute("forca", 1)
            print("Ganhas +1 Força!")
        case range(6, 11):
            add_attribute("destreza", 1)
            print("Ganhas +1 Destreza!")
        case range(12, 17):
            add_attribute("carisma", 1)
            print("Ganhas +1 Carisma!")
        case range(18, 24):
            add_attribute(random.choice(["forca", "destreza", "carisma"]), 3)
            print("Ganhas +3 Random Stat!")
        case range(25, 36):
            subtract_attribute(random.choice(["forca", "destreza", "carisma"]), 2)
            print("Perdes -2 Stat!")
        case range(37, 44):
            print("Aparecem os 4 cavaleiros do apocalipse e morres!")
            exit()
        case range(45, 56):
            subtract_attribute("forca", 1)
            print("Perdes -1 Força!")
        case range(57, 68):
            subtract_attribute("carisma", 1)
            print("Perdes -1 Carisma!")
        case range(69, 80):
            subtract_attribute("destreza", 1)
            print("Perdes -1 Destreza!")
        case range(81, 88):
            change_atribute("cartao_escola", True)
            print("Ganhas o cartão da escola")
        case range(89, 91):
            change_class(random.choice([Goliardo, Gatuno, Gadiador]))
            print("Tornas-te (Goliardo/Gatuno/Gladiador)")
        case range(92, 100):
            print("Perdes-te...")
            exit()

def tnormal ():
    tabela = random.randint(1, 100)
    match tabela:
        case range(1, 7):
            add_attribute("forca", 1)
            print("Ganhas +1 Força!")
        case range(8, 14):
            add_attribute("destreza", 1)
            print("Ganhas +1 Destreza!")
        case range(15, 21):
            add_attribute("carisma", 1)
            print("Ganhas +1 Carisma!")
        case range(22, 28):
            add_attribute(random.choice(["forca", "destreza", "carisma"]), 3)
            print("Ganhas +3 Random Stat!")
        case range(29, 35):
            subtract_attribute(random.choice(["forca", "destreza", "carisma"]), 2)
            print("Perdes -2 Stat!")
        case range(36, 43):
            print("Aparecem os 4 cavaleiros do apocalipse e morres!")
            exit()
        case range(44, 53):
            subtract_attribute("forca", 1) 
            print("Perdes -1 Força!")
        case range(54, 63):
            subtract_attribute("carisma", 1)
            print("Perdes -1 Carisma!")
        case range(64, 73):
            subtract_attribute("destreza", 1)
            print("Perdes -1 Destreza!")
        case range(74, 85):
            change_attribute("cartao_escola", True)
            print("Ganhas o cartão da escola")
        case range(86, 89):
            change_class(random.choice([Goliardo, Gatuno, Gadiador]))
            print("Tornas-te (Goliardo/Gatuno/Gladiador)")
        case range(90, 97):
            print("Perdes-te...")
            exit()
        case range(98, 100):
            change_class(Plebeu)
            print("Tornas-te Plebeu!")
            

