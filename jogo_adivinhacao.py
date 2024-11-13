import random
#lista para armazenar as pontuações
pontuacoes = []
# Criando o Loop principal do jogo
print("Bem-vindo ao jogo de Adivinhação!")

while True:
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = 7
    tentativas = 0

    print("\nEu pensei em um número entre 1 e 100.")
    print("Você tem 7 tentativas para adivinhar")

    #Loop de tentativas
    while tentativas_restantes > 0:
        palpite = input("\nDigite o seu palpite: ")

        #Verificando se o input é um número válido
        if not palpite.isdigit():
            print("Por favor, digite um número válido entre 1 e 100.")
            continue

        palpite = int(palpite)
        if palpite < 1 or palpite > 100:
            print("O número de estar entre 10 e 100.")
            continue

        tentativas += 1
        tentativas_restantes -= 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas(s).")
            pontuacao = tentativas_restantes * 10
            pontuacoes.append(pontuacao)
            print(f"Sua pontuação nesta partida: {pontuacao} pontos.")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse.")
        else:
            print("O número é menor que esse.")

        print(f"Tentaivas restantes: {tentativas_restantes}")

    else:
        print(f"\nQue pena! Você não conseguiu adivinhar. O número era {numero_secreto}.")
        pontuacoes.append(0)

    # Exibindo o Placar
    print("\nPlacar:")
    for idx, pontos in enumerate(pontuacoes, start=1):
        print(f"Partida {idx}: {pontos} pontos")

    # Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar! Até a próxima.")
        break