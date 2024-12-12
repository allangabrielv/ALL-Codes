import random

collection_of_words = [
    "abacaxi", "abacate", "animais", "banco", "bola", "bonito", "cachorro", "cadeira", "carro", "cidade",
    "coelho", "computador", "coragem", "coroa", "cultura", "dado", "dedo", "dinheiro", "escola", "fogo",
    "formiga", "futebol", "gato", "governo", "grande", "homem", "honesto", "janela", "jogo", "joia",
    "julho", "juventude", "lagoa", "livro", "luz", "maca", "mala", "mar", "mato", "mestre",
    "montanha", "muito", "navio", "ninho", "olho", "ordem", "orvalho", "papo", "pato", "pessoa",
    "piano", "pode", "porco", "porta", "quadro", "quente", "rato", "relogio", "rocha", "roda",
    "sabor", "saco", "sal", "semente", "sol", "sombra", "telefone", "tigre", "tio", "trabalho",
    "vaca", "verde", "vila", "vitoria", "voo", "voto", "zebra", "abismo", "alvo", "antigo",
    "arte", "bicho", "bicicleta", "brisa", "broto", "bumbum", "cabra", "calor", "caminho", "canto",
    "carne", "caverna", "cozinha", "estrela", "feliz", "galo", "gente", "giro", "gota", "grito",
    "guerra", "ilha", "inimigo", "ira", "jogo", "juiz", "lago", "leao", "livro", "lua", "matriz",
    "nuvem", "olho", "ouvido", "pague", "pao", "pedra", "pula", "riso", "roca", "sapo",
    "sombra", "sonho", "tigre", "tomate", "torneio", "urso", "vento", "tio", "pato", "ponto"
]
selected_word=collection_of_words[random.randint(0,99)]


print("\n------- JOGO DA FORCA -------\n")

secretword=str(selected_word)
secretwordbackup=str(secretword)

asteriskword=("*"*len(secretword))
asteriskwordbackup=str(("*"*len(secretword)))

chosen_letters=''
count=1


print(f"Tamanho da Palavra: {len(secretword)} letras\n")


while True:
    print ("-----------------------------")
    letter=input(f"Insira a letra (Tentativa {count}): ")

    if len(letter)>1:

        print("Você inseriu mais de um caracter, tente novamente.\n")

        continue

    if letter.isdigit():

        print("Você inseriu uma entrada incorreta, tente novamente.\n")

        continue
    
    if letter in secretword:

        for i in range(len(secretwordbackup)):

            index=secretwordbackup.find(letter)

            asteriskwordbackup=list(asteriskwordbackup)

            if index!=-1:

                asteriskwordbackup[index]=letter

            else:

                asteriskword="".join(asteriskwordbackup)
                break

            secretwordbackup=secretwordbackup.replace(letter, '*', 1)
        if not letter in chosen_letters:
            print ("\nMuito Bem, você acertou uma das letras!!!")
        else:
            print("\nEssa letra já foi inserida, e ela pertecente a palavra, tente novamente.")

    else:
        if not letter in chosen_letters:
            print("\nEssa letra não existe na palavra, tente novamente.")
        else:
            print("\nEssa letra já foi inserida, e ela não pertecente a palavra, tente novamente.")

    if not letter in chosen_letters:
        count+=1
        chosen_letters+=(f"\'{letter}\' ")

    if asteriskword.find('*') != -1:
        print ("Letras tentadas: ", chosen_letters, "\n")
        print (f"Palavra -> \" {asteriskword} \"\n")

    else:
        print(f"\nParabéns!! Você encontrou a palavra secreta.\nA palavra era \"{secretword}\".")
        
        print(f"Número de Tentativas: {count}\n")
        break
