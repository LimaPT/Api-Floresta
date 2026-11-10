import random
from dataclasses import dataclass, field

@dataclass
class Attributes:
    forca: int = 0
    destreza: int = 0
    carisma: int = 0
    cartao_escola: bool = False

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
            cartao_escola=self.player_class.base_attributes.cartao_escola
        )

    # Função para alterar a classe do jogador (Necessária para o teu código funcionar)
    def change_class(self, new_class: PlayerClass) -> None:
        self.player_class = new_class
        self.attributes = Attributes(
            forca=new_class.base_attributes.forca,
            destreza=new_class.base_attributes.destreza,
            carisma=new_class.base_attributes.carisma,
            cartao_escola=new_class.base_attributes.cartao_escola
        )

    # Funções para alterar atributos do jogador
    def add_attribute(self, attribute: str, amount: int = 1) -> None:
        self._change_attribute(attribute, abs(amount))

    def subtract_attribute(self, attribute: str, amount: int = 1) -> None:
        self._change_attribute(attribute, -abs(amount))

    def _change_attribute(self, attribute: str, amount: int) -> None:
        if attribute not in {"forca", "destreza", "carisma","cartao_escola"}:
            raise ValueError(f"Unknown attribute: {attribute}")

        current_value = getattr(self.attributes, attribute)
        setattr(self.attributes, attribute, current_value + amount)

# Classes de personagem 
Gadiador = PlayerClass(name="Gladiador", 
            base_attributes=Attributes(forca=7, carisma=4, destreza=3))
Gatuno = PlayerClass(name="Gatuno", 
            base_attributes=Attributes(forca=3, carisma=5, destreza=7))
Goliardo = PlayerClass(name="Goliardo", 
            base_attributes=Attributes(forca=3, carisma=7, destreza=5))
Plebeu = PlayerClass(name="Plebeu", 
            base_attributes=Attributes(forca=1, carisma=1, destreza=1))

# Funções para alterar atributos do jogador pela tabela/simplificado
def add_attribute(attribute: str, amount: int = 1) -> None:
    player.add_attribute(attribute, amount)
def subtract_attribute(attribute: str, amount: int = 1) -> None:
    player.subtract_attribute(attribute, amount)
def change_class(player_class: PlayerClass) -> None:
    player.change_class(player_class)

#Tabelas Random
def tplebeu ():
    tabela = random.randint(1, 100)
    match tabela:
        case range(1, 4):
            add_attribute("forca", 1)
            print("Ganhas +1 Força!")
        case range(5, 8):
            add_attribute("destreza", 1)
            print("Ganhas +1 Destreza!")
        case range(9, 12):
            add_attribute("carisma", 1)
            print("Ganhas +1 Carisma!")
        case range(13, 17):
            add_attribute(random.choice(["forca", "destreza", "carisma"]), 3)
            print("Ganhas +3 Random Stat!")
        case range(18, 27):
            subtract_attribute(random.choice(["forca", "destreza", "carisma"]), 2)
            print("Perdes -2 Stat!")
        case range(28, 35):
            print("Aparecem os 4 cavaleiros do apocalipse e morres!")
            exit()
        case range(36, 45):
            # If nas ruínas, voltas para gruta / If nas gruta voltas para sombra / If nas sombras, voltas para ruína
            print("Foste para ____!")   
        case range(46, 55):
            subtract_attribute("forca", 1)
            print("Perdes -1 Força!")
        case range(56, 65):
            subtract_attribute("carisma", 1)
            print("Perdes -1 Carisma!")
        case range(66, 75):
            subtract_attribute("destreza", 1)
            print("Perdes -1 Destreza!")
        case range(76, 87):
            # voltar 2 escolhas atrás
            print("Deixaste cair o teu, porta chaves favorito. Tens de voltar 2 escolhas atrás.")
        case range(88, 93):
            change_atribute("cartao_escola", True)
            print("Ganhas o cartão da escola")
        case range(94, 96):
            change_class(random.choice([Goliardo, Gatuno, Gadiador]))
            print("Tornas-te (Goliardo/Gatuno/Gladiador)")
        case range(97, 100):
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
        case range(29, 34):
            subtract_attribute(random.choice(["forca", "destreza", "carisma"]), 2)
            print("Perdes -2 Stat!")
        case range(35, 40):
            print("Aparecem os 4 cavaleiros do apocalipse e morres!")
            exit()
        case range(41, 48):
            # If nas ruínas, voltas para gruta / If nas gruta voltas para sombra / If nas sombras, voltas para ruína
            print("Foste para ____!")   
        case range(49, 54):
            subtract_attribute("forca", 1) 
            print("Perdes -1 Força!")
        case range(55, 60):
            subtract_attribute("carisma", 1)
            print("Perdes -1 Carisma!")
        case range(61, 66):
            subtract_attribute("destreza", 1)
            print("Perdes -1 Destreza!")
        case range(67, 78):
            # voltar 2 escolhas atrás
            print("Deixaste cair o teu, porta chaves favorito. Tens de voltar 2 escolhas atrás.")
        case range(79, 90):
            change_attribute("cartao_escola", True)
            print("Ganhas o cartão da escola")
        case range(91, 92):
            change_class(random.choice([Goliardo, Gatuno, Gadiador]))
            print("Tornas-te (Goliardo/Gatuno/Gladiador)")
        case range(93, 98):
            print("Perdes-te...")
            exit()
        case range(99, 100):
            change_class(Plebeu)
            print("Tornas-te Plebeu!")

classes = {
    "gladiador": Gadiador,
    "gatuno": Gatuno,
    "goliardo": Goliardo,
}

# Início do jogo
print("Escolha uma classe: Gladiador, Gatuno ou Goliardo")
escolha = input("> ").strip().lower()
player_class = classes.get(escolha, Plebeu)
player = Player(name="Jogador", player_class=player_class)

if escolha in classes:
    print(f"Parabéns! Tornaste-te num {player.player_class.name}!!!")
else:
    print("\nEscolha inválida... Tornaste-te num PLEBEU!")
print(f"Os teus stats são: {player.attributes}")

# Primeira Opção
def cenario_floresta(player):
    print('\nA floresta divide-se em três caminhos...')
    print('1 - Gruta')
    print('2 - Sombras')
    print('3 - Ruínas')

    path = input('Que caminho escolhes? ').strip().lower()

    match path:
        case "1" | "gruta":
            cenario_gruta(player)
        case "2" | "sombras":
            cenario_sombras(player)
        case "3" | "ruínas" | "ruinas":
            cenario_ruinas(player)
        case _:
            print('Opção inválida, tenta novamente.')
            cenario_floresta(player)

# --- CENÁRIOS BASEADOS PURAMENTE EM TESTES DE ATRIBUTOS ---

def cenario_gruta(player):
    print("\n--- CAMINHO DA GRUTA ESCURA ---")
    tplebeu() if player.player_class == Plebeu else tnormal()
    print(f"Stats atuais: {player.attributes}")

    print("\nEntras na gruta e vês duas direções possíveis:")
    print("1 - Seguir pelo túnel iluminado por cogumelos brilhantes")
    print("2 - Avançar pela fresta escura na parede de pedra")
    
    input("O que decides fazer? ")

    print("\n[DESAFIO] Uma rocha gigante desaba na saída da gruta!")
    if player.attributes.forca >= 5:
        print("Os teus pontos de Força chegaram para empurrar a rocha e abrir caminho. Escapaste!")
    else:
        print("Não tens força suficiente para mover a rocha... Ficas preso para sempre.")
    exit()

def cenario_sombras(player):
    print("\n--- CAMINHO DO VALE DAS SOMBRAS ---")
    tplebeu() if player.player_class == Plebeu else tnormal()
    print(f"Stats atuais: {player.attributes}")

    print("\nEntras no vale coberto de névoa e encontras uma encruzilhada:")
    print("1 - Seguir pelo trilho principal onde a névoa parece mais baixa")
    print("2 - Cortar caminho por entre os arbustos densos e negros")
    
    input("O que decides fazer? ")

    print("\n[DESAFIO] Criaturas disparam flechas contra ti a partir das árvores!")
    if player.attributes.destreza >= 5:
        print("Os teus pontos de Destreza foram suficientes para te desviares das flechas rápido! Escapaste!")
    else:
        print("És demasiado lento para te desviares das flechas... Fim da linha.")
    exit()

def cenario_ruinas(player):
    print("\n--- CAMINHO DAS RUÍNAS ANTIGAS ---")
    tplebeu() if player.player_class == Plebeu else tnormal()
    print(f"Stats atuais: {player.attributes}")

    print("\nChegas às ruínas do templo e vês duas entradas para o salão:")
    print("1 - Subir as escadarias principais de mármore partido")
    print("2 - Descer pelas catacumbas subterrâneas que passam por baixo")
    
    input("O que decides fazer? ")

    print("\n[DESAFIO] Uma grande estátua de pedra mágica ganha vida e bloqueia o caminho!")
    if player.attributes.carisma >= 5:
        print("Pedes educadamente para a estátua mexer-se. O teu Carisma convence-a e ela abre o caminho! Escapaste!")
    else:
        print("Não tens lábia ou carisma suficiente. A estátua ignora-te e esmaga-te... Fim do jogo.")
    exit()

# Executa o início do jogo após a criação do player
cenario_floresta(player)
