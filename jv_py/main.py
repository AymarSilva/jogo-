import random, os

tabuleiro = [x for x in range(10)]
tabuleiro = tabuleiro[1:len(tabuleiro)]

disponivel = [isJogada for isJogada in tabuleiro if isinstance(isJogada, int)]

parar = False

def fazLinha():
    for i in range(3):
        if not i == 2:
            print('--', end="")
        else:
            print('--', end="\n")

def fazNum():
    for x in range(9):
        if x == 2 or x == 5 or x == 8:
            print(tabuleiro[x], end="\n")
        else:
            print(tabuleiro[x], end=" ")

def fazTabuleiro():
    fazLinha()
    fazNum()
    fazLinha()

def fazJogadaP():
    global parar

    response = input("Faça sua jogada ou digite pare: ")

    # standardize the 'pare' request
    if response.lower() == "pare":
        os.system('cls')
        print("parei")
        parar = True
        return parar
    
    try:
        response = int(response)
        # Find the index through the user's response
        index = tabuleiro.index(response)

        # Write the user's move on tabuleiro
        tabuleiro[index] = 'O'

        # Drop the user's move from disponivel
        tiraDisp = disponivel.index(response)
        del disponivel[tiraDisp]

    except:
        print("Digite um valor válido")
        return fazJogadaP()

def verifica_vitoria(player, mensagem):
    global parar, disponivel

    # Win condition
    vitorias = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # it's a tie if there's nothing inside disponivel
    if not disponivel:
        os.system('cls')
        print("Empate!")
        parar = True
    
    # Verifies if it's a win
    for linha in vitorias:
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]]:
            os.system('cls')

            if tabuleiro[linha[0]] == player:
                print(mensagem)

            fazTabuleiro()
            parar = True
            return parar

def fazJogadaMaq(jogadasDisponivel):
    global tabuleiro

    if jogadasDisponivel:

        #Selects a random number from disponivel
        jogada = random.choice(jogadasDisponivel)
        print("Jogada da máquina: ", jogada)

        #Replaces the placeholder with X
        index = tabuleiro.index(jogada)
        tabuleiro[index] = 'X'

        # Drop jogada from disponivel
        tiraDisp = disponivel.index(jogada)
        del disponivel[tiraDisp]

while not parar:

    fazTabuleiro()
    fazJogadaP()

    verifica_vitoria('O',"Você ganhou!")

    if not parar:
        fazJogadaMaq(disponivel)
        verifica_vitoria('X', "Máquina ganhou!")