def jogar():

    from pandas import read_csv
    from random import randrange

    print('*****************************')
    print('*******Jogo da forca*********')
    print('*****************************')

    # Ler arquivo
    palavras = read_csv('palavras_adivinha.csv')
    palavras.dropna(inplace=True)
    coluna = randrange(len(palavras.columns))

    # Escolhendo dificuldade
    def escolha_dificuldade():
        dificuldade = input('Olá escolha uma dificuldade:\n0-Facil(15 chances) / 1-Medio(10 chances) / 2-Dificil(5 chances)\n:')
        chances = 0
        if dificuldade == '0':
            chances = 15
        elif dificuldade == '1':
            chances = 10
        elif dificuldade == '2':
            chances = 5
        else:
            print('Error, opção invalida')
            escolha_dificuldade()

        return chances
    
    chances = escolha_dificuldade()

    # Coleta palavras e as normaliza
    def gerar_palavras_secretas_e_categoria(palavras,coluna):
        palavras_escolhidas = []

        # Gerar categoria
        
        categoria = palavras.iloc[:,coluna]

        # Gerar palavra
        for palavra in categoria:
            palavras_escolhidas.append(palavra)
        return palavras_escolhidas
    

    # Gera uma palavra aleatoria para ser adivinhada
    def sorteiar_palavra(palavras_escolhidas):
        i = randrange(len(palavras_escolhidas))
        palavras_sorteada = palavras_escolhidas[i]
        return palavras_sorteada.lower()

    # Verifica se o chute esta certo
    def verificar_chute(palavra_sorteada,chances,palavras,coluna):
        posicoes = ['_' for i in range(len(palavra_sorteada))]
        print(posicoes, len(posicoes))
        
        # Enquanto chances maior que 0
        while(chances>0):
            print(f'Você tem {chances} chances')
            print(f'A categoria é {palavras.columns[coluna]}')
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
            
    verificar_chute(sorteiar_palavra(gerar_palavras_secretas_e_categoria(palavras,coluna)),chances,palavras,coluna)

if __name__ == '__main__':
    jogar()