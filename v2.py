import random
from dataclasses import dataclass, field

@dataclass
class Attributes:
    forca: int = 0
    destreza: int = 0
    carisma: int = 0

@dataclass(frozen=True)
class PlayerClass:
    name: str
    base_attributes: Attributes

@dataclass
class Player:
    name: str
    player_class: PlayerClass
    attributes: Attributes = field(init=False)

    def __post_init__(self) -> None:
        self.attributes = Attributes(
            forca=self.player_class.base_attributes.forca,
            destreza=self.player_class.base_attributes.destreza,
            carisma=self.player_class.base_attributes.carisma,
        )

    def add_attribute(self, attribute: str, amount: int = 1) -> None:
        self._change_attribute(attribute, abs(amount))

    def subtract_attribute(self, attribute: str, amount: int = 1) -> None:
        self._change_attribute(attribute, -abs(amount))

    def _change_attribute(self, attribute: str, amount: int) -> None:
        if attribute not in {"forca", "destreza", "carisma"}:
            raise ValueError(f"Unknown attribute: {attribute}")

        current_value = getattr(self.attributes, attribute)
        setattr(self.attributes, attribute, current_value + amount)

#classes de personagem 
Gadiador = PlayerClass(name="Gladiador", 
            base_attributes=Attributes(forca=7, carisma=4, destreza=3))
Gatuno = PlayerClass(name="Gatuno", 
            base_attributes=Attributes(forca=3, carisma=5, destreza=7))
Goliardo = PlayerClass(name="Goliardo", 
            base_attributes=Attributes(forca=3, carisma=7, destreza=5))
Plebeu = PlayerClass(name="Plebeu", 
            base_attributes=Attributes(forca=1, carisma=1, destreza=1))

#Tabela Random
def tplebeu ():
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


#escolha de classes
print('Escolha uma classe: Gladiador, Gatuno ou Goliardo ')
escolha = input('> ').lower()

if escolha in classes_player:
    stats_class = classes_player[escolha].copy()
    #cria uma variável que pega no dicionário que foi criado antes e,
    #com a escolha, dá "fetch" numa das classes que foram criadas e copia essa classe para esta nova variável

    print(f'Parabéns! Tornaste-te num {escolha.capitalize}!!!')
    print(f'os teus stats são: {stats_class}\n ')
else:
    print('\n escolha inválida... Apenas membros da PLEBE não sabem ler!')
    stats_class = {'strength': 1, 'charisma': 1, 'dexterity': 1}
    print(f'Parabéns! Tornaste-te num PLEBEU!!!\n os teus stats são {stats_class}\n não há volta atrás...')   

def stats_player:(classes_) 