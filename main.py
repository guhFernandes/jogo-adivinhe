from random import randint

jogar = "sim"

while jogar == "sim":

    i = numAdivinhe = 0

    numTentativas = int(input("Informe o numero de tentativas [1, 20]: "))
    while numTentativas < 1 or numTentativas > 20:
        print("Numero invalido!")
        numTentativas = int(input("Informe o numero de tentativas: [1, 20]"))

    numSecreto = randint(1, 100)

    while i < numTentativas and numAdivinhe != numSecreto:
        i += 1
        print(f"Tentativa {i}")

        numAdivinhe = int(input("Adivinhe o numero de [1, 100]: "))
        while numAdivinhe < 1 or numAdivinhe > 100:
            print("Numero invalido!")
            numAdivinhe = int(input("Adivinhe o numero de [1, 100]: "))

        if numAdivinhe == numSecreto:
            print(f"Parabens voce ganhou com apenas {i} tentativa")
        else:
            if numAdivinhe < numSecreto:
                print("Numero secreto maior")
            else:
                print("Numero secreto menor")

    if i >= numTentativas:
        print("Suas tentativas acabaram! ")

    jogar = input("fim, Deseja jogar novamente [sim, nao]: ")
