import random
from dataclasses import dataclass, field

@dataclass
class Attributes:
    forca: int = 0
    destreza: int = 0
    carisma: int = 0
    cartao_escola: bool = field(default=False, repr=False)

@dataclass(frozen=True)
class Class:
    name: str
    base_attributes: Attributes

# Classes de personagem 
Gadiador = Class(name="Gladiador", 
            base_attributes=Attributes (forca=7, carisma=4, destreza=3, cartao_escola=False))
Gatuno = Class(name="Gatuno", 
            base_attributes=Attributes (forca=3, carisma=5, destreza=7, cartao_escola=True))
Goliardo = Class(name="Goliardo", 
            base_attributes=Attributes (forca=3, carisma=7, destreza=5, cartao_escola=False))
Plebeu = Class(name="Plebeu", 
            base_attributes=Attributes (forca=1, carisma=1, destreza=1, cartao_escola=False))

player_classes = {
    "gladiador": Gadiador,
    "gatuno": Gatuno,
    "goliardo": Goliardo,
}

@dataclass
class Player:
    name: str
    player_class: Class
    attributes: Attributes = field(init=False)

    def __post_init__(self) -> None:
        self.attributes = Attributes (
            forca=self.player_class.base_attributes.forca,
            destreza=self.player_class.base_attributes.destreza,
            carisma=self.player_class.base_attributes.carisma,
            cartao_escola=self.player_class.base_attributes.cartao_escola
        )

    # Função para alterar a classe do jogador (Necessária para o teu código funcionar)
    def change_class(self, new_class: Class) -> None:
        self.player_class = new_class
        self.attributes = Attributes (
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


# Funções para alterar atributos do jogador pela tabela/simplificado
def add_attribute(attribute: str, amount: int = 1) -> None:
    player.add_attribute(attribute, amount)
def subtract_attribute(attribute: str, amount: int = 1) -> None:
    player.subtract_attribute(attribute, amount)
def change_attribute(attribute: str, value: bool) -> None:
    if attribute != "cartao_escola":
        raise ValueError(f"Unknown attribute: {attribute}")
    setattr(player.attributes, attribute, value)


def change_atribute(attribute: str, value: bool) -> None:
    change_attribute(attribute, value)


def change_class(player_class: Class) -> None:
    player.change_class(player_class)

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
            
# Início do jogo

print("Escolha uma classe: Gladiador, Gatuno ou Goliardo")
escolha = input("> ").strip().lower()
player_class = player_classes.get(escolha, Plebeu)
player = Player(name="Jogador", player_class=player_class)
stats_message = (
    "Os teus stats são: "
    f"Força= {player.attributes.forca}, "
    f"Destreza= {player.attributes.destreza}, "
    f"Carisma= {player.attributes.carisma}"
)
if escolha in player_classes:
    print(f"Parabéns! Tornaste-te num {player.player_class.name}!!!")
else:
    print("\nEscolha inválida... Tornaste-te num PLEBEU!")

if player.player_class is Gatuno:
    stats_message += " e tens o cartão da escola!"
    print(stats_message)

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
            if player.player_class == Plebeu:
                tplebeu()
            else:
                tnormal()
            cenario_floresta(player)

def cenario_ruinas(player):
    print('\nEscolheste as ruínas...')
    print('1 - Explorar as ruínas')
    print('2 - Voltar para a floresta')

    choicer = input('O que queres fazer?\n ').strip().lower()

    match choicer:
        case "1" | "explorar":
            print("Explorando as ruínas...")
            choicer = input("Escolha uma ação: 1 - Sentar-se a ouvir os sons das floresta, 2 - Deixas-te levar pelo... , 3 - Decides tirar uma selfie\n").strip().lower()
            match choicer:

                case "1" | "sentar-se":
                    print("Sentaste-te a ouvir os sons da floresta...\nPassado um tempo, sentes-te uma presença agradável e relaxante. Sentes que algo te empurra para algum lugar, por isso andas.\n")
                    print("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                    exit()   

                case "2" | "deixar-se levar":
                    print("Deixaste-te levar pelo... \nSOM DA MÚSICA! \nO que ouves?")
                    print("1 - Poker Face: Lady Gaga, 2 - Beleiver: Imagine Dragons, 3 - Sweden: C418 ")
                    choicem = input("Escolha uma música: ").strip().lower()
                    match choicem:
                        case "1" | "poker face":
                            if player.attributes.destreza >= 7:
                                print("Escolheste Poker Face! \nComeças a dançar e rápidamente percebes que estás a divar!")
                                print("Os espíritos agradecem a tua performance e ajudam-te a atravessar a floresta.")
                                print("Um tempo depois observas algo um pouco estranho, um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                                exit()
                            else:
                                print("Escolheste Poker Face! \nComeças a dançar e rápidamente percebes que não sabes o que estás a fazer!")
                                print("Algo fica irritado, manda te de volta para a floresta e perdes-te!")
                                print("FIM MEH")
                                exit()
                        case "2" | "beleiver":
                            print("Escolheste Beleiver! \nComeças a ouvir e tentas dançar, mas rapidamente lembras-te das aulas de educação física.\n \nNão és o único com essa lembrança... Algo oprime-te e ouves: \nEste é o teu fim... ")
                            print("Sentes cossegas?? \n \nESTE É O TEU CASTIGO POR NOS LEMBRARES")
                            choicec = input("Tens cossegas: SIM ou NÃO? ").strip().lower()
                            match choicec:
                                case "sim":
                                    print("Sentirás cossegas por 100 anos... \n \nESTE É O TEU CASTIGO")
                                    print("FIM MAU")
                                    exit()
                                case "não":
                                    print("NÃO Sentes cossegas?? \n \nAgora terás de fazer o VAI E VEM Eternamente")
                                    print("FIM CURSED")
                                    exit()
                        case "3" | "sweden":
                            print("Escolheste Sweden! \nComeças a ouvir e lembras-te de jogar Minecraft e a sua tranquilidade. \nComeças a deanbular pela floresta e...")
                            print("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")        
                            
                case "3" | "selfie":
                    print("Decidiste tirar uma selfie...")
                    if player.attributes.carisma >= 7:
                        print("Uma presença carismática! Eles ficam honrados e guiam-te para a floresta.")
                        print("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                        exit()
                    else:
                        print("Quem és tu para tirar uma selfie com TAMANHAS entidades???? \nEles oprimem-te e ouves: \nEste é o teu fim... ")
                        print("Sentes cossegas?? \n")
                        choicec = input("Tens cossegas: SIM ou NÃO? ").strip().lower()
                        match choicec:
                            case "sim"|"s":
                                print("Sentirás cossegas por 100 anos... \n \nESTE É O TEU CASTIGO")
                                print("FIM MAU")
                                exit()
                            case "não"|"n"|"nao":
                                print("NÃO Sentes cossegas?? \n \nAgora terás de fazer o VAI E VEM Eternamente")
                                print("FIM CURSED")  
                                exit()       
                case _:
                    print('Opção inválida, tenta novamente.')
                    if player.player_class == Plebeu:
                        tplebeu()
                    else:
                        tnormal()
                    cenario_ruinas(player)

        case "2" | "voltar":
            cenario_floresta(player)
        case _:
            print('Opção inválida, tenta novamente.')
            if player.player_class == Plebeu:
                tplebeu()
            else:
                tnormal()
            cenario_ruinas(player)

def cenario_gruta(player):
    print("\n--- CAMINHO DA GRUTA ESCURA ---")
    butao=input("Tocas no butão? Sim ou Não\n").strip().lower()
    if butao == "sim":
        if player.player_class == Plebeu:
            tplebeu()
            print(stats_message)
            cenario_gruta_caminhos(player)
        else:
            tnormal()
            print(stats_message)
            cenario_gruta_caminhos(player)
    else:
        cenario_gruta_caminhos(player)

def cenario_gruta_caminhos(player):
        print("\nEntras na gruta e vês duas direções possíveis:")
        print("1 - Ouves um BOMDIA!!!, e segues o som da voz")
        print("2 - Vês a Dª Glória e aprecebes-te que precisas de algo...")
        
        option_1 = input("O que decides fazer? ")
        if option_1 == "1":
            print("BOOOOOOOOOM DIAAAAAAAAAAAAAA!")
            print("Tens que fazer uma reação ácido-redução com a professora de FQ")
            print("\nNa oxidação, o número de oxidação aumenta:1 , ou diminui:2 ?")
            option_1_1 = input("\n >") 
            if option_1_1 == "1":
                print("Erraste, foste enviado para as ruínas, para seres exorcidado...")
                print("Sentes várias sensações estranhas e ouves vozes macabras... \n \nEste é o teu fim... ")
                print("Sentes cossegas?? \n")
                choicec = input("Tens cossegas: SIM ou NÃO? ").strip().lower()
                match choicec:
                    case "sim":
                        print("Sentirás cossegas por 100 anos... \n \nESTE É O TEU CASTIGO POR FALHARES A TUA ÚNICA OBRIGAÇÃO")
                        print("FIM MAU")
                        exit()
                    case "não":
                        print("NÃO Sentes cossegas?? \n \nAgora terás de fazer o VAI E VEM Eternamente")
                        print("FIM CURSED")
                        exit()  
            else:
                print("Acertaste e escapaste da gruta com média de 15.4321/20 em Física e Quimica A!")
                print("Algo agradece o teu esforço e leva-te a pela floresta até...\n")
                print("Um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                exit()
        else:
            print("Ao chegares à Dª Glória, ela pergunta-te se tens o cartão da escola...")
            choiced = input("Tens o cartão da escola? SIM OU NÃO?").strip().lower()
            if choiced == "sim":
                player.attributes.cartao_escola==True
                print("Mostraste o cartão da escola e deixaram-te passar...!")
            else:
                player.attributes.cartao_escola==False
                print("Não tens o cartão da escola, tens que fazer uma reação ácido-redução")
                print("\nNa oxidação, o número de oxidação aumenta; 1 ou diminui; 2?")
                option_1_2 = input("\n >")
                if option_1_2 == "1":
                    print("Erraste, foste enviado para as ruínas, e és consumindo pelos espirito")
                else:
                    print("Acertaste e escapaste da gruta com média de 15.4321/20 em Física e Quimica A!")
                    print("Algo agradece o teu esforço e leva-te a pela floresta até...\n")
                    print("Um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                    exit()
            if choiced == "não":
                player.attributes.cartao_escola==False
                print("Não tens o cartão da escola.\n 1- Aceitas o teu destino e vais fazer a reação ácido-redução, 2- Tentas a tua sorte com a tua personalidade carismática, 3- Propões um braço de ferro à Dª Glória")
                if choiced == "1":
                    print("\nNa oxidação, o número de oxidação aumenta; 1 ou diminui; 2?")
                    option_1_2 = input("\n >")
                    if option_1_2 == "1":
                        print("Erraste, foste enviado para as ruínas, e és consumindo pelos espirito")
                    else:
                        print("Acertaste e escapaste da gruta com média de 15.4321/20 em Física e Quimica A")
                if choiced == "2":
                    if player.attributes.carisma >= 7:
                        print("A tua personalidade carismática convenceu a Dª Glória e ela deixa-te passar...!")
                    else:
                        print("A tua personalidade NÃO carismática, não convenceu a Dª Glória e foste enviado para o BOOOOOMMMMM DIAAAAAA!")
                        print("Tens que fazer uma reação ácido-redução com a professora de FQ")
                        print("\nNa oxidação, o número de oxidação aumenta:1 , ou diminui:2 ?")
                        option_1_1 = input("\n >")
                        if option_1_1 == "1":
                            print("Erraste, foste enviado para as ruínas, para seres exorcidado...")
                            print("Sentes várias sensações estranhas e ouves vozes macabras... \n \nEste é o teu fim... ")
                            print("Sentes cossegas?? \n \nESTE É O TEU CASTIGO POR FALHARES A TUA ÚNICA OBRIGAÇÃO")
                            choicec = input("Tens cossegas: SIM ou NÃO? ").strip().lower()
                            match choicec:
                                case "sim":
                                    print("Sentirás cossegas por 100 anos... \n \nESTE É O TEU CASTIGO POR FALHARES A TUA ÚNICA OBRIGAÇÃO")
                                    print("FIM MAU")
                                    exit()
                                case "não":
                                    print("NÃO Sentes cossegas?? \n \nAgora terás de fazer o VAI E VEM Eternamente")
                                    print("FIM CURSED")
                                    exit() 
                if choiced == "3":
                    if player.attributes.forca >= 7:
                        resultado = random.randint(1, 10)
                        if resultado <= 4:    
                            print("A tua força física convenceu a Dª Glória e ela deixa-te passar...!")
                            cenario_sombras(player)
                    else:
                        print("A tua força física NÃO convenceu a Dª Glória e foste enviado para o BOOOOOMMMMM DIAAAAAA!")
                        print("Tens que fazer uma reação ácido-redução com a professora de FQ")
                        print("\nNa oxidação, o número de oxidação aumenta:1 , ou diminui:2 ?")
                        option_1_1 = input("\n >")
                        if option_1_1 == "1":
                            print("Erraste, foste enviado para as ruínas, para seres exorcidado...")
                            print("Sentes várias sensações estranhas e ouves vozes macabras... \n \nEste é o teu fim... ")
                            print("Sentes cossegas?? \n")
                            choicec = input("Tens cossegas: SIM ou NÃO? ").strip().lower()
                            match choicec:
                                case "sim":
                                    print("Sentirás cossegas por 100 anos... \n \nESTE É O TEU CASTIGO POR FALHARES A TUA ÚNICA OBRIGAÇÃO")
                                    print("FIM MAU")
                                    exit()
                                case "não":
                                    print("NÃO Sentes cossegas?? \n \nAgora terás de fazer o VAI E VEM Eternamente")
                                    print("FIM CURSED")
                                    exit() 

def cenario_sombras(player):
    print("\nEscolheste as sombras...")
    if player.player_class == Plebeu:
        tplebeu()
    else:
        tnormal()

cenario_floresta(player)