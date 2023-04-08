from pandas import read_csv
from random import randrange


def gerar_palavras_secretas():
    """
    Retorna uma lista de palavras a serem adivinhadas, lidas de um arquivo CSV.
    """
    palavras = read_csv('palavras_adivinha.csv', header=None, names=['palavra'])
    return palavras['palavra'].apply(lambda palavra: palavra.lower().strip()).tolist()


def sorteiar_palavra(palavras_escolhidas):
    """
    Retorna uma palavra aleatória a ser adivinhada, escolhida a partir de uma lista de palavras.
    """
    return palavras_escolhidas[randrange(len(palavras_escolhidas))]


def validar_chute(chute):
    """
    Verifica se a entrada do usuário é válida (uma letra).
    """
    if len(chute) != 1:
        return False
    if not chute.isalpha():
        return False
    return True


def verificar_chute(palavra_sorteada):
    """
    Verifica se o chute do usuário está correto e imprime o resultado na tela.
    """
    posicoes = ['_' for i in range(len(palavra_sorteada))]
    chances = 5

    while chances > 0:
        print(f'Você tem {chances} chances')
        chute = input('Manda a letra pro pai: ').lower()

        if not validar_chute(chute):
            print('Chute inválido. Por favor, digite uma letra.')
            continue

        if chute in palavra_sorteada:
            indices = [i for i, letra in enumerate(palavra_sorteada) if letra == chute]
            for index in indices:
                posicoes[index] = chute
            print(f'Certo!, a letra "{chute.capitalize()}" aparece nas posições:\n {posicoes}')
        else:
            print('Mongo imbecil, errou')
            chances -= 1

        print('___*___')

        if posicoes == list(palavra_sorteada):
            print(f'Você ganhou!\nA palavra era {palavra_sorteada.title()}')
            return True

    print(f'Mongão, chances acabaram.\nA palavra era: {palavra_sorteada.title()}')
    return False


def jogar():
    """
    Executa uma partida do jogo da forca.
    """
    print('*****************************')
   

