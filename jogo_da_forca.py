def jogar():

    from pandas import read_csv
    from random import randrange

    print('*****************************')
    print('*******Jogo da forca*********')
    print('*****************************')

    # Coleta palavras e as normaliza
    def gerar_palavras_secretas():
        palavras = read_csv('palavras_adivinha.csv')
        palavras_escolhidas = []
        for palavra in palavras.palavras_adivinha:
            palavras_escolhidas.append(palavra)
        return palavras_escolhidas

    # Gera uma palavra aleatoria para ser adivinhada
    def sorteiar_palavra(palavras_escolhidas):
        i = randrange(len(palavras_escolhidas))
        palavras_sorteada = palavras_escolhidas[i]
        return palavras_sorteada.lower()

    # Verifica se o chute esta certo
    def verificar_chute(palavra_sorteada):
        posicoes = ['_' for i in range(len(palavra_sorteada))]
        print(posicoes, len(posicoes))
        chances = 5
        
        # Enquanto chances maior que 0
        while(chances>0):
            print(f'Você tem {chances} chances')
            chute = input('Manda a letra pro pai: ').lower()
            chutes = list(chute)

            # Se a letra chutada estiver dentro da palavra secreta
            for chute in chutes:
                if chute in palavra_sorteada:
                    indices = [i for i in range(len(palavra_sorteada)) if palavra_sorteada.startswith(chute, i)]
                    for index in indices:
                        posicoes[index] = palavra_sorteada[index]
                    print(f'Certo!, a letra "{chute.capitalize()}" aparece nas posições:\n {posicoes}')
                else:
                    print('Mongo imbecil, errou')
                    chances -= 1

            print('___*___') # Separador para legibilidade

            # Se as todas as letras chutadas estiverem nas posições certas
            if posicoes == list(palavra_sorteada):
                print(f'Você ganho \n A palavra era {palavra_sorteada.title()}')
                break
                
            # Se as chances acabarem
            elif chances == 0:
                print(f'Mongão, chances acabaram\n A palavra era: {palavra_sorteada.title()}')

    verificar_chute(sorteiar_palavra(gerar_palavras_secretas()))

if __name__ == '__main__':
    jogar()