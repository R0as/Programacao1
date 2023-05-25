import random
from os import system, name

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    
    return "2020102389"
def getNome():
    """
    Retorna o nome completo do aluno
    """
    
    return "HENRIQUE ROAS MARTINS MARQUITO"
def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear')
def escolheLetra():
    """
    Função destinada a escolher com qual letra você quer jogar.
    """
    jogador1 = input("\nVocê deseja ser X ou O ? (letra maiuscula) ")
    limpaTela()
    if jogador1 == "X":
        print("Você escolheu X")
        return "X", "O"
    elif jogador1 == "O":
        print("Você escolheu O")
        return "O", "X"
    else:
        limpaTela()
        print("Operação Inválida")
        return escolheLetra()
def primeiraJogada():
    """
    Função para ver quem irá começar jogando.
    """
    return random.choice([0, 1])
def tab(tabuleiro):
    """
    Função que apenas imprime o tabuleiro
    """
    print(f" {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}")   
    print("---+---+---")
    print(f" {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}")
    print("---+---+---")
    print(f" {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}")
def PosicaoDaJogada(tabuleiro):
    """
    Função destinada a escolher em qual posição você irá jogar
    """
    jogada = int(input("\nEscolha a posição onde deseja jogar (entre 1 e 9): "))
    

    if jogada <= 9 and jogada>=1:
        if jogada == 1 and tabuleiro[1] == " ":
            return jogada
        elif jogada == 2 and tabuleiro[2] == " ":
            return jogada
        elif jogada == 3 and tabuleiro[3] == " ":
            return jogada
        elif jogada == 4 and tabuleiro[4] == " ":
            return jogada
        elif jogada == 5 and tabuleiro[5] == " ":
            return jogada
        elif jogada == 6 and tabuleiro[6] == " ":
            return jogada
        elif jogada == 7 and tabuleiro[7] == " ":
            return jogada
        elif jogada == 8 and tabuleiro[8] == " ":
            return jogada
        elif jogada == 9 and tabuleiro[9] == " ":
            return jogada
        else:
            limpaTela()
            tab(tabuleiro)
            print("\nJogada inválida")
            return PosicaoDaJogada(tabuleiro)
           
    else:
        limpaTela()
        tab(tabuleiro)
        print("\nJogada inválida")
        return PosicaoDaJogada(tabuleiro)
def Vitoria_Jogador(tabuleiro,jogador):
    """
    verifica se a pessoa ganhou
    """
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == jogador:
        return True
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == jogador:
        return True
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == jogador:
        return True
    elif tabuleiro[7] == tabuleiro[4] == tabuleiro[1] == jogador:
        return True
    elif tabuleiro[8] == tabuleiro[5] == tabuleiro[2] == jogador:
        return True
    elif tabuleiro[9] == tabuleiro[6] == tabuleiro[3] == jogador:
        return True
    elif tabuleiro[7] == tabuleiro[5] == tabuleiro[3] == jogador:
        return True
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == jogador:
        return True
    else:
        return False
def Vitoria_Computador(tabuleiro,computador):
    """
    verifica se o computador ganhou
    """
    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3] == computador:
        return True
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6] == computador:
        return True
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9] == computador:
        return True
    elif tabuleiro[7] == tabuleiro[4] == tabuleiro[1] == computador:
        return True
    elif tabuleiro[8] == tabuleiro[5] == tabuleiro[2] == computador:
        return True
    elif tabuleiro[9] == tabuleiro[6] == tabuleiro[3] == computador:
        return True
    elif tabuleiro[7] == tabuleiro[5] == tabuleiro[3] == computador:
        return True
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9] == computador: 
        return True
    else:
        return False
def empate(tabuleiro,jogador,computador,primeiroAJogar):
    """
    Função que verifica se houve empate ou não
    """
    if tabuleiro[1] != " " and tabuleiro[2] != " " and tabuleiro[3] != " " and tabuleiro[4] != " " and tabuleiro[5] != " " and tabuleiro[6] != " " and tabuleiro[7] != " " and tabuleiro[8] != " " and tabuleiro[9] != " ":
        return True
    else:
       return False
def jogadaComputador(tabuleiro, computador,jogador,primeiroAJogar):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    caso o computador comece ele escolherá uma casa aleatória para fazer a jogada, depois dará prioridade para a defesa, em segunda ordem tem ataques diretos(ataque na 3 jogada),depois ataque com 3 jogadas, a primeira jogada(nao tem ordem de prioridade pois as condicções para ela ocorrer permitem isso), e as jogadas caso só houver 1 casa disponivel.
    """
    ##########COMPUTADOR COMECA COM JOGADA ALEATORIA########
    if tabuleiro == ([" "," "," "," "," "," "," "," "," "," "]):
        aleatorio = random.choice([1,3,7,9])
        if aleatorio == 1:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif aleatorio == 3:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif aleatorio == 7:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif aleatorio == 9:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9


    else:
        ###################ATAQUE COM 3 JOGADAS#########################
        if tabuleiro[1] == tabuleiro[3] == tabuleiro[9]:
            if tabuleiro[6] == " ":
                tabuleiro[6] = computador
                return 6
            elif tabuleiro[2] == " ":
                tabuleiro[2] = computador
                return 2
        if tabuleiro[7] == tabuleiro[1] == tabuleiro[3]:
            if tabuleiro[2] == " ":
                tabuleiro[2] = computador
                return 2
            if tabuleiro[4] == " ":
                tabuleiro[2] = computador
                return 2
        ##############DEFESA######################
        if tabuleiro[1] == tabuleiro[5] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[1] == tabuleiro[9] == jogador:
            if tabuleiro[5] == " ":
                tabuleiro[5] = computador
                return 5
        elif tabuleiro[9] == tabuleiro[5] == jogador:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[4] == tabuleiro[5] == jogador:
            if tabuleiro[6] == " ":
                tabuleiro[6] = computador
                return 6
        elif tabuleiro[7] == tabuleiro[5] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[7] == tabuleiro[3] == jogador:
            if tabuleiro[5] == " ":
                tabuleiro[5] = computador
                return 5
        elif tabuleiro[5] == tabuleiro[3] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[8] == tabuleiro[5] == jogador:
            if tabuleiro[2] == " ":
                tabuleiro[2] = computador
                return 2
        elif tabuleiro[8] == tabuleiro[2] == jogador:
            if tabuleiro[5] == " ":
                tabuleiro[5] = computador
                return 5
        elif tabuleiro[5] == tabuleiro[2] == jogador:
            if tabuleiro[8] == " ":
                tabuleiro[8] = computador
                return 8
        elif tabuleiro[1] == tabuleiro[7] == jogador:
            if tabuleiro[4] == " ":
                tabuleiro[4] = computador
                return 4
        elif tabuleiro[1] == tabuleiro[2] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[1] == tabuleiro[3] == jogador:
            if tabuleiro[2] == " ":
                tabuleiro[2] = computador
                return 2
        elif tabuleiro[2] == tabuleiro[3] == jogador:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[7] == tabuleiro[4] == jogador:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[7] == tabuleiro[1] == jogador:
            if tabuleiro[4] == " ":
                tabuleiro[4] = computador
                return 4
        elif tabuleiro[1] == tabuleiro[4] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[7] == tabuleiro[8] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[7] == tabuleiro[9] == jogador:
            if tabuleiro[8] == " ":
                tabuleiro[8] = computador
                return 8
        elif tabuleiro[8] == tabuleiro[9] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[9] == tabuleiro[6] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[5] == tabuleiro[6] == jogador:
            if tabuleiro[4] == " ":
                tabuleiro[4] = computador
                return 4
        elif tabuleiro[3] == tabuleiro[9] == jogador:
            if tabuleiro[6] == " ":
                tabuleiro[6] = computador
                return 6
        elif tabuleiro[6] == tabuleiro[3] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        ################ATAQUE COM DIRETO################        
        if tabuleiro[1] == tabuleiro[5]:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[1] == tabuleiro[9]:
            if tabuleiro[5] == " ":
                tabuleiro[5] = computador
                return 5
        elif tabuleiro[9] == tabuleiro[5]:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[4] == tabuleiro[5]:
            if tabuleiro[6] == " ":
                tabuleiro[6] = computador
                return 6
        elif tabuleiro[7] == tabuleiro[5]:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[7] == tabuleiro[3]:
            if tabuleiro[5] == " ":
                tabuleiro[5] = computador
                return 5
        elif tabuleiro[5] == tabuleiro[3]:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[8] == tabuleiro[5]:
            if tabuleiro[2] == " ":
                tabuleiro[2] = computador
                return 2
        elif tabuleiro[8] == tabuleiro[2]:
            if tabuleiro[5] == " ":
                tabuleiro[5] = computador
                return 5
        elif tabuleiro[5] == tabuleiro[2]:
            if tabuleiro[8] == " ":
                tabuleiro[8] = computador
                return 8
        elif tabuleiro[1] == tabuleiro[7]:
            if tabuleiro[4] == " ":
                tabuleiro[4] = computador
                return 4
        elif tabuleiro[1] == tabuleiro[2]:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[1] == tabuleiro[3]:
            if tabuleiro[2] == " ":
                tabuleiro[2] = computador
                return 2
        elif tabuleiro[2] == tabuleiro[3]:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[7] == tabuleiro[4]:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[7] == tabuleiro[1]:
            if tabuleiro[4] == " ":
                tabuleiro[4] = computador
                return 4
        elif tabuleiro[1] == tabuleiro[4]:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[7] == tabuleiro[8]:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[7] == tabuleiro[9]:
            if tabuleiro[8] == " ":
                tabuleiro[8] = computador
                return 8
        elif tabuleiro[8] == tabuleiro[9]:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[9] == tabuleiro[6]:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[5] == tabuleiro[6]:
            if tabuleiro[4] == " ":
                tabuleiro[4] = computador
                return 4
        elif tabuleiro[3] == tabuleiro[9]:
            if tabuleiro[6] == " ":
                tabuleiro[6] = computador
                return 6
        elif tabuleiro[6] == tabuleiro[3]:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        ##########JOGADAS ALEATORIAS################
        if tabuleiro[1] == computador and tabuleiro[2] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[1] == computador and tabuleiro[4] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[1] == computador and tabuleiro[5] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[1] == computador and tabuleiro[7] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[1] == computador and tabuleiro[9] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[1] == computador and tabuleiro[3] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[1] == computador and tabuleiro[8] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[1] == computador and tabuleiro[6] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        ##############PRIMEIRA JOGADA DO COMPUTADOR##############
        if tabuleiro[1] == jogador:
            if tabuleiro[7] == " ":
                tabuleiro[7] = computador
                return 7
        elif tabuleiro[2] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[3] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[4] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[5] == jogador:
            if tabuleiro[3] == " ":
                tabuleiro[3] = computador
                return 3
        elif tabuleiro[6] == jogador:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[7] == jogador:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        elif tabuleiro[8] == jogador:
            if tabuleiro[9] == " ":
                tabuleiro[9] = computador
                return 9
        elif tabuleiro[9] == jogador:
            if tabuleiro[1] == " ":
                tabuleiro[1] = computador
                return 1
        #########JOGADAS ALEATORIAS OU QUANDO SO TIVER UMA JOGADA LIVRE###############
        if tabuleiro[1] == " ":
            tabuleiro[1] = computador
            return 1
        elif tabuleiro[2] == " ":
            tabuleiro[2] = computador
            return 2
        elif tabuleiro[3] == " ":
            tabuleiro[3] = computador
            return 3
        elif tabuleiro[4] == " ":
            tabuleiro[4] = computador
            return 4
        elif tabuleiro[5] == " ":
            tabuleiro[5] = computador
            return 5
        elif tabuleiro[6] == " ":
            tabuleiro[6] = computador
            return 6
        elif tabuleiro[7] == " ":
            tabuleiro[7] = computador
            return 7
        elif tabuleiro[8] == " ":
            tabuleiro[8] = computador
            return 8
        elif tabuleiro[9] == " ":
            tabuleiro[9] = computador
            return 9

def Movimentos(tabuleiro,jogador,computador,primeiroAJogar):
    """
    função que chama a função tabuleiro, a posicao onde quer jogar,preenche o tabuleiro,verifica quem ganhou,printa quem ganhou, pergunta se quer jogar novamente, com a finalidade de coordenar as jogadas e chamar a funcao jogada computador
    """
    if primeiroAJogar == 1:
        tab(tabuleiro)
        jogadaPlayer = PosicaoDaJogada(tabuleiro)
        tabuleiro[jogadaPlayer] = jogador
        limpaTela()
        tab(tabuleiro)
        Vitoria_Jogador(tabuleiro,jogador)
        if Vitoria_Jogador(tabuleiro,jogador) == True:
            print("\nVocê ganhou!!!!")
            jogar_DNV = input("Deseja jogar novamente (S/N)? ")
            if jogar_DNV == "S" or jogar_DNV == "s":
                main()
            elif jogar_DNV == "n" or jogar_DNV == "N":
                limpaTela()
                print("Obrigado por jogar o jogo da velha!!!")
                exit()
            else:
                limpaTela()
                print("Comando inválido!")
                return Vitoria_Jogador(tabuleiro,jogador)
        else:
            empate(tabuleiro,jogador,computador,primeiroAJogar)
            if empate(tabuleiro,jogador,computador,primeiroAJogar)== True:
                print("\nO jogo terminou empatado!!!")
                jogar_DNV = input("Deseja jogar novamente (S/N)? ")
                if jogar_DNV == "S" or jogar_DNV == "s":
                    main()
                elif jogar_DNV == "N" or jogar_DNV == "n":
                    limpaTela()
                    print("Obrigado por jogar o jogo da velha!!!")
                    exit()
                else:
                    limpaTela()
                    print("Comando inválido!")
                    return empate(tabuleiro,jogador,computador,primeiroAJogar)
            else:
                primeiroAJogar -= 1
                limpaTela()
                Movimentos(tabuleiro,jogador,computador,primeiroAJogar)
    elif primeiroAJogar == 0:
        jogadaComputador(tabuleiro,computador,jogador,primeiroAJogar)
        limpaTela()
        tab(tabuleiro)
        Vitoria_Computador(tabuleiro,computador)
        if Vitoria_Computador(tabuleiro,computador) == True:
            print("\nO computador ganhou!!!")
            jogar_DNV = input("Deseja jogar novamente (S/N)? ")
            if jogar_DNV == "S" or jogar_DNV == "s":
                main()
            elif jogar_DNV == "N" or jogar_DNV == "n":
                limpaTela()
                print("Obrigado por jogar o jogo da velha!!!")
                exit()
            else:
                limpaTela()
                print("Comando inválido!")
                return Vitoria_Computador(tabuleiro,computador)
        else:
            empate(tabuleiro,jogador,computador,primeiroAJogar)
            if empate(tabuleiro,jogador,computador,primeiroAJogar)== True:
                print("\nO jogo terminou empatado!!!")
                jogar_DNV = input("Deseja jogar novamente (S/N)? ")
                if jogar_DNV == "S" or jogar_DNV == "s":
                    main()
                elif jogar_DNV == "N" or jogar_DNV == "n":
                    limpaTela()
                    print("Obrigado por jogar o jogo da velha!!!")
                    exit()
                else:
                    limpaTela()
                    print("Comando inválido!")
                    return empate(tabuleiro,jogador,computador,primeiroAJogar)
            else:
                primeiroAJogar += 1
                limpaTela()
                Movimentos(tabuleiro,jogador,computador,primeiroAJogar)####chama a funcao movimento####
def main():
    """
    funcao main onde há o tabuleiro,msg de boas vindas,chama a funcao de quem comeca, a funcao com qual letra a pessoa quer jogar, e a funcao das jogadas
    """
    limpaTela()    
    print("Seja bem vindo ao jogo da velha!")
    input("\nAperte enter para entrar")
    limpaTela()
    tabuleiro = [" "," "," "," "," "," "," "," "," "," "]    ###lista###
    jogador,computador = escolheLetra()    #chama a funcao de escolher a letra###
    primeiroAJogar = primeiraJogada()      #chama a funcao de primeira jogada####
    if primeiroAJogar == 0:
        print("\nO computador será o primeiro a jogar.\n")
    elif primeiroAJogar == 1:
        print("\nVocê começa.\n")
    Movimentos(tabuleiro,jogador,computador,primeiroAJogar)###chama a funcao movimento###
if __name__ == "__main__":
    main()