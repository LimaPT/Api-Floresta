# Floresta Alentejana
# Feito por Sofia Lima 27, Rafael Matos 25 e Marcelo Antero 20
# Turma 12º 2

import random
import time
import os

from dataclasses import dataclass, field

def printBonito(text="", delay=0.04):
    for char in str(text):
        print(char, end="", flush=True)
        if char in ".!?":
            time.sleep(delay * 3)   # Pausa maior no fim de frase
        elif char == ",":
            time.sleep(delay * 2)   # Pausa breve nas vírgulas
        else:
            time.sleep(delay)
    print()

def inputBonito(prompt="", delay=0.04):
    for char in str(prompt):
        print(char, end="", flush=True)
        if char in ".!?":
            time.sleep(delay * 5)
        elif char == ",":
            time.sleep(delay * 3)
        else:
            time.sleep(delay)
    return input()

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
            base_attributes=Attributes (forca =7, carisma =4, destreza =3, cartao_escola=False))
Gatuno = Class(name="Gatuno", 
            base_attributes=Attributes (forca =3, carisma =5, destreza =7, cartao_escola=True))
Goliardo = Class(name="Goliardo", 
            base_attributes=Attributes (forca =3, carisma =7, destreza =5, cartao_escola=False))
Plebeu = Class(name="Plebeu", 
            base_attributes=Attributes (forca =1, carisma =1, destreza =1, cartao_escola=False))

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
               
# Início do jogo

printBonito("Escolha uma classe: Gladiador, Gatuno ou Goliardo")
escolha = inputBonito("> ").strip().lower()
player_class = player_classes.get(escolha, Plebeu)
player = Player(name="Jogador", player_class=player_class)
stats_message = (
    "Os teus stats são: \n"
    f" Força ==== {player.attributes.forca},\n "
    f"Destreza ==== {player.attributes.destreza},\n "
    f"Carisma ==== {player.attributes.carisma}\n"
)

if escolha in player_classes:
    printBonito(f"Parabéns! Tornaste-te num {player.player_class.name}!!!")
else:
    printBonito("\nEscolha inválida... Tornaste-te num PLEBEU!")

if player.player_class is Gatuno:
    stats_message += " E tens o cartão da escola!"
    printBonito(stats_message)
input('Aperte ENTER para continuar... ')
os.system("cls" if os.name == "nt" else "clear")
printBonito('Acordas num descampado no meio da floresta...')

# Primeira Opção
def cenario_floresta(player):
    time.sleep(3)
    printBonito('\nEncontras uma placa que aparentemente diz que a floresta divide-se em três caminhos...')
    printBonito('1 - Gruta (da escuridão e soturnidade)')
    printBonito('2 - Sombras (assustadoras e macabras)')
    printBonito('3 - Ruínas (da perdição e do tormento)')

    path = inputBonito('Que caminho escolhes?\n> ').strip().lower()

    match path:
        case "1" | "gruta":
            cenario_gruta(player)
        case "2" | "sombras":
            cenario_sombras(player)
        case "3" | "ruínas" | "ruinas":
            cenario_ruinas(player)
        case _:
            printBonito('Opção inválida, tenta novamente.')
            cenario_floresta(player)

#RUINAS
def cenario_ruinas(player):

    printBonito('\nEscolheste as ruínas...')
    printBonito('1 - Explorar as ruínas')
    printBonito('2 - Voltar para a floresta')

    choicer = inputBonito('O que queres fazer?\n> ').strip().lower()

    match choicer:
        case "1" | "explorar":
            printBonito("Explorando as ruínas...")
            choicer = inputBonito("Escolha uma ação: 1 - Sentar-se a ouvir os sons das floresta, 2 - Deixas-te levar pelo... , 3 - Decides tirar uma selfie\n> ").strip().lower()
            match choicer:
                case "1" | "sentar-se":
                    printBonito("Sentaste-te a ouvir os sons da floresta...\nPassado um tempo, sentes uma presença agradável e relaxante. Sentes que algo te empurra para algum lugar, por isso andas.\n")
                    printBonito("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                    exit()   

                case "2" | "deixar-se levar":
                    printBonito("Deixaste-te levar pelo... \nSOM DA MÚSICA! \nO que ouves?")
                    printBonito("1 - Poker Face: Lady Gaga, 2 - Believer: Imagine Dragons, 3 - Sweden: C418 ")
                    choicem = inputBonito("Escolha uma música\n>  ").strip().lower()
                    match choicem:

                        case "1" | "poker face":
                            if player.attributes.destreza >= 7:
                                printBonito("Escolheste Poker Face! \nComeças a dançar e rápidamente percebes que estás a divar!")
                                printBonito("Os espíritos agradecem a tua performance e ajudam-te a atravessar a floresta.")
                                printBonito("Um tempo depois observas algo um pouco estranho, um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                                exit()
                            else:
                                printBonito("Escolheste Poker Face! \nComeças a dançar e rápidamente percebes que não sabes o que estás a fazer!")
                                printBonito("Algo fica irritado, manda te de volta para a floresta e perdes-te!")
                                printBonito("FIM MEH")
                                exit()

                        case "2" | "believer":
                            printBonito("Escolheste Believer! \nComeças a ouvir e tentas dançar, mas rapidamente lembras-te das aulas de educação física.\n \nNão és o único com essa lembrança... Algo oprime-te e ouves: \nEste é o teu fim... ")
                            printBonito("Sentes cossegas?? \n \nESTE É O TEU CASTIGO POR NOS LEMBRARES")
                            choicec = inputBonito("Tens cossegas: SIM ou NÃO? ").strip().lower()
                            if choicec in {"sim", "s"}:
                                printBonito("Sentirás cócegas por 100 anos...")
                                printBonito("FIM MAU")
                                exit()
                            elif choicec in {"não", "nao", "n"}:
                                printBonito("Agora terás de fazer o VAI E VEM eternamente")
                                printBonito("FIM CURSED")
                                exit()
                            else:
                                printBonito("Resposta inválida.")
                                cenario_ruinas(player)

                        case "3" | "sweden":
                            printBonito("Escolheste Sweden! \nComeças a ouvir e lembras-te de jogar Minecraft e a sua tranquilidade. \nComeças a deambular pela floresta e...")
                            printBonito("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")        
                            exit()
                        case _:
                            printBonito('Opção inválida, tenta novamente.')
                            cenario_ruinas(player)
                case "3" | "selfie":
                    printBonito("Decidiste tirar uma selfie...")
                    if player.attributes.carisma >= 7:
                        printBonito("Uma presença carismática! Eles ficam honrados e guiam-te para a floresta.")
                        printBonito("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                        exit()
                    else:
                        printBonito("Quem és tu para tirar uma selfie com TAMANHAS entidades???? \nEles oprimem-te e ouves: \nEste é o teu fim... ")
                        printBonito("Sentes cócegas??\n> ")
                        choicec = inputBonito("Tens cossegas: SIM ou NÃO? ").strip().lower()
                        if choicec in {"sim", "s"}:
                            printBonito("Sentirás cócegas por 100 anos...")
                            printBonito("FIM MAU")
                            exit()
                        elif choicec in {"não", "nao", "n"}:
                            printBonito("Agora terás de fazer o VAI E VEM eternamente")
                            printBonito("FIM CURSED")
                            exit()
                        else:
                            printBonito("Resposta inválida.")
                            cenario_ruinas(player) 

                case _:
                    printBonito('Opção inválida, tenta novamente.')
                    cenario_ruinas(player)

        case "2" | "voltar":
            cenario_floresta(player)
        case _:
            printBonito('Opção inválida, tenta novamente.')
            cenario_ruinas(player)

#GRUTA
def cenario_gruta(player):
    printBonito("\n--- CAMINHO DA GRUTA ESCURA ---")
    printBonito("\nEntras na gruta e vês duas direções possíveis:")
    printBonito("1 - Ouves um BOMDIA!!!, e segues o som da voz")
    printBonito("2 - Vês a Dª Glória e aprecebes-te que precisas de algo...")

    option_1 = inputBonito("O que decides fazer? ").strip().lower()

    if option_1 == "1":
        printBonito("BOOOOOOOOOM DIAAAAAAAAAAAAAA!")
        printBonito("Tens que fazer uma reação ácido-redução com a professora de FQ")
        printBonito("\nNa oxidação, o número de oxidação Aumenta - 1 ou Diminui - 2 ?")

        resposta = inputBonito("\n> ")

        if resposta == "1":
            printBonito("Acertaste e escapaste da gruta com média de 15.4321/20 em Física e Quimica A!")
            printBonito("Algo agradece o teu esforço e leva-te a pela floresta até...\n")
            printBonito("Um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
            exit()
        else:
            printBonito("Erraste, foste enviado para as ruínas, para seres exorcidado...")
            printBonito("Sentes várias sensações estranhas e ouves vozes macabras... \n \nEste é o teu fim... ")
            printBonito("Sentes cossegas?? \n")

            choicec = inputBonito("Tens cossegas: SIM ou NÃO? ").strip().lower()

            if choicec in {"sim", "s"}:
                printBonito("Sentirás cócegas por 100 anos...")
                printBonito("FIM MAU")
                exit()
            elif choicec in {"não", "nao", "n"}:
                printBonito("Agora terás de fazer o VAI E VEM eternamente")
                printBonito("FIM CURSED")
                exit()
            else:
                printBonito("Resposta inválida. Responde SIM ou NÃO.")
                cenario_gruta(player)

    elif option_1 == "2":
        printBonito("Ao chegares à Dª Glória, ela pergunta-te se tens o cartão da escola...")
        choiced = inputBonito("Tens o cartão da escola? SIM OU NÃO? ").strip().lower()

        if choiced in {"sim", "s"} and player.attributes.cartao_escola:
            printBonito("Mostraste o cartão da escola e deixaram-te passar...!")
            cenario_sombras(player)

        elif choiced in {"sim", "s"} and not player.attributes.cartao_escola:
            player.attributes.cartao_escola = False
            printBonito("Não tens o cartão da escola.")

            acao = inputBonito(
                "1 - Fazer a reação de oxidação-redução, "
                "2 - Usar carisma, "
                "3 - Propor um braço de ferro\n> "
            ).strip()

            if acao == "1":
                printBonito("\nNa oxidação, o número de oxidação Aumenta - 1 ou Diminui - 2 ?")
                resposta = inputBonito("\n> ")

                if resposta == "1":
                    printBonito("Acertaste e escapaste da gruta com média de 15.4321/20 em Física e Quimica A!")
                    printBonito("Algo agradece o teu esforço e leva-te a pela floresta até...\n")
                    printBonito("Um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                    exit()
                else:
                    printBonito("Erraste, foste enviado para as ruínas, para seres exorcidado...")
                    printBonito("Sentes várias sensações estranhas e ouves vozes macabras... \n \nEste é o teu fim... ")
                    printBonito("Sentes cossegas?? \n \nESTE É O TEU CASTIGO POR FALHARES A TUA ÚNICA OBRIGAÇÃO")

                    choicec = inputBonito("Tens cócegas: SIM ou NÃO? ").strip().lower()

                    if choicec in {"sim", "s"}:
                        printBonito("Sentirás cócegas por 100 anos...")
                        printBonito("FIM MAU")
                        exit()
                    elif choicec in {"não", "nao", "n"}:
                        printBonito("Agora terás de fazer o VAI E VEM eternamente")
                        printBonito("FIM CURSED")
                        exit()
                    else:
                        printBonito("Resposta inválida. Responde SIM ou NÃO.")
                        cenario_gruta(player)

            elif acao == "2":
                if player.attributes.carisma >= 7:
                    printBonito("A tua personalidade carismática convenceu a Dª Glória e ela deixa-te passar...!")
                    cenario_sombras(player)
                else:
                    printBonito("A tua personalidade NÃO carismática, não convenceu a Dª Glória e foste enviado para o BOOOOOMMMMM DIAAAAAA!")
                    cenario_gruta(player)

            elif acao == "3":
                if player.attributes.forca >= 7:
                    resultado = random.randint(1, 10)

                    if resultado <= 4:
                        printBonito("A tua força física convenceu a Dª Glória e ela deixa-te passar...!")
                        cenario_sombras(player)
                    else:
                        printBonito("A tua força física NÃO convenceu a Dª Glória e foste enviado para o BOOOOOMMMMM DIAAAAAA!")
                        cenario_gruta(player)
                else:
                    printBonito("A tua força física NÃO convenceu a Dª Glória e foste enviado para o BOOOOOMMMMM DIAAAAAA!")
                    cenario_gruta(player)

            else:
                printBonito("Opção inválida, tenta novamente.")
                cenario_gruta(player)

        elif choiced in {"não", "nao", "n"}:
            printBonito("BOOOOOOOOOM DIAAAAAAAAAAAAAA!")
            printBonito("Tens que fazer uma reação ácido-redução com a professora de FQ")
            printBonito("\nNa oxidação, o número de oxidação Aumenta - 1 ou Diminui - 2 ?")

            resposta = inputBonito("\n> ")

            if resposta == "1":
                printBonito("Acertaste e escapaste da gruta com média de 15.4321/20 em Física e Quimica A!")
                printBonito("Algo agradece o teu esforço e leva-te a pela floresta até...\n")
                printBonito("Um BURGERKING! \nParece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
                exit()
            else:
                printBonito("Erraste, foste enviado para as ruínas, para seres exorcidado...")
                cenario_gruta(player)

        else:
            printBonito("Resposta inválida.")
            cenario_gruta(player)

    else:
        printBonito("Opção inválida, tenta novamente.")
        cenario_gruta(player)

# SOMBRAS DO MAL
def cenario_sombras(player):
    printBonito("\n--- CAMINHO DO VALE DAS SOMBRAS ---")
    printBonito(stats_message)

    printBonito("\nEntras no vale coberto de névoa e encontras uma encruzilhada:")
    printBonito("1 - Seguir pelo trilho principal onde a névoa parece mais baixa")
    printBonito("2 - Cortar caminho por entre os arbustos densos e negros")

    opt_1s = inputBonito("O que decides fazer?\n> ")

    if opt_1s == "1":
        printBonito("Segues caminho pela frente...")

        if player.attributes.destreza >= 7:
            printBonito("Sentes uma presença estranha e fazes o teu melhor para não ser notado.\n")
            printBonito("Mesmo com os teus dotes de destreza, a presença parece saber onde te encontras e continua a aproximar-se!")
        else:
            printBonito("Sentes que qualquer coisa não está bem mas continuas a andar...\n")
            printBonito("Sentes uma pressão cada vez maior e começas a correr!")
    else:
        printBonito("Depois de andar por algum tempo por entre os arbustos, acabas por voltar ao mesmo sítio...")
        return cenario_sombras(player)

    printBonito("Um grupo de luzes coloridas aparece à tua frente e fazem-te parar a corrida\n")
    printBonito("As luzes começam a comunicar-se telepaticamente contigo e, em poucas palavras, fazem-te um enigma:\n")

    enigmasTotilBacano(player)

# ENIGMAS
def enigmasTotilBacano(player):
    printBonito("O que é que uma impressora disse para a outra?\n")
    printBonito("1 - Impressoras falam...?")
    printBonito("2 - Impressiona-me...?")
    printBonito("3 - Essa folha é tua ou é impressão minha...?")

    opt_2s = inputBonito("A resposta é...\n> ")

    if opt_2s == "3":
        printBonito("[CERTO] Os espíritos começam a piscar de felicidade!")
    elif opt_2s == "2":
        if player.attributes.carisma >= 7:
            printBonito("[CARISMA] A tua resposta não é a esperada... Mas os espíritos sentem-se impressionados pela tua confiança e consideram-te um génio!")
        else:
            printBonito("[ERRADO] Os espíritos pensam por um bocado... e chegam à conclusão que mereces uma outra oportunidade!\n")
            return enigmasTotilBacano(player)
    else:
        printBonito("[DEAD END] Os espíritos calam-se por completo e decidem abandonar-te na escuridão da névoa...")
        exit()

    printBonito("Acertaste 1 enigma! Mas os espíritos ainda parecem insatisfeitos...")
    printBonito("Ainda agitados, os espíritos partilham outro enigma:")
    printBonito("Num muro, ainda metade construído, dois tijolos têm uma conversa...")
    printBonito("O que um tijolo falou para o outro?")

    printBonito("1 - Há um ciumento entre nós...")
    printBonito("2 - Nada, uh.. tijolos não costumam falar...")
    printBonito("3 - Sinto que... a nossa relação precisa de uma definição em concreto...")

    opt_3s = inputBonito("A resposta é...\n> ")

    if opt_3s == "1":
        printBonito("[CERTO] Os espíritos começam a piscar de felicidade!")
    elif opt_3s == "3":
        if player.attributes.carisma >= 7:
            printBonito("[CARISMA] Os espíritos ficam em silêncio por um bocado... Mas acabaram por gostar da tua resposta!")
        else:
            printBonito("[ERRADO] Os espíritos pensam por um bocado... e chegam à conclusão que mereces uma outra oportunidade! Mas vais ter de começar denovo. \n")
            return enigmasTotilBacano(player)
    else:
        printBonito("[DEAD END] Os espíritos calam-se por completo e decidem abandonar-te na escuridão da névoa...")
        exit()

    printBonito("Woah! 2 enigmas corretos! Mas os espíritos continuam insatisfeitos.")
    printBonito("Assim, como se fosse o último (talvez porque seja), eles fazem mais um enigma:")
    printBonito("Se um avião cair na fronteira entre Alemanha e França, onde se enterram os sobreviventes?")

    printBonito("1 - No seu respetivo país de origem ou no país que os seus relativos decidirem!")
    printBonito("2 - Acho que depende. Seria necessário discutir com os governos sobre onde deveriam ser enterrados.")
    printBonito("3 - huh?")

    opt_3s = inputBonito("A resposta é...\n> ")

    if opt_3s == "1":
        printBonito('Os espíritos param. "como assim? Não ouviste?" perguntam')
        printBonito("Se um avião cair na fronteira entre Alemanha e França, onde se enterram os sobreviventes?")

        printBonito("1 - Como assim enterrar sobreviventes?")
        printBonito("2 - ...?")

        opt_sub3s = inputBonito("A resposta é...\n> ")

        if opt_sub3s == "1":
            printBonito("[CORRETO] Os espíritos aplaudem a tua atenção e finalmente sentem-se satisfeitos!")
        else:
            printBonito("[DEAD END] O puro facto de teres de continuar a pensar sobre isto fala muito sobre ti.")
            exit()
    else:
        if player.attributes.carisma >= 7:
            printBonito("[CARISMA] Os espíritos riem-se de ti. Aparentemente achavam que estavas a fazer uma piada por isso deixam-te refazer os enigmas...")
            return enigmasTotilBacano(player)
        else:
            printBonito("[DEAD END] Os espíritos param de se mexer e decidem abandonar-te na névoa. Talvez desse jeito ler melhor a pergunta huh.")
            exit()

    printBonito("Conseguiste! 3 enigmas totalmente corretos! Sem enganos nenhuns!")
    printBonito("Agora, com a total confiança e admiração pela tua sabedoria, os espíritos decidem guiar-te pelo caminho nebuloso...")
    printBonito("Um tempo depois observas algo um pouco estranho, um BURGERKING! Parece que a floresta chegou ao fim e agora o Rei dos hamburgers oferece-te um whopper.\n \nFIM BOM")
    exit()

cenario_floresta(player)
