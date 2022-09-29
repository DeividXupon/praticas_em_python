import random


def jogar():
    print(".", "_" * 59, ".", sep="")
    print("|", " " * 19, " Jogo de Adivinhação ", " " * 19, "|", sep="")
    print("|", "~" * 59, "|", sep="")

    numero_aleatorio = random.randrange(1, 101)
    tot_tantativas = 6

    for tentativas in range(0, tot_tantativas):

        print("|", "=" * 18, f"Jogadas restantes: (_{tot_tantativas - tentativas}¨)", "=" * 17, "|", sep="")

        # Conversão para int
        chute_str = input("| Digite um numero entre 1 a 100: ")
        try:
            chute_int = int(chute_str)
        except:
            print("|-+-> Foi pedido um NUMERO e recebi testo. ERRO: N.A.N <-+--|")
            continue
        #

        acerto = numero_aleatorio == chute_int

        # Numero é de 1 a 100?
        if (chute_int < 1 or chute_int > 100):
            print("|", "=" * 13, "NUMERO DEVE SER ENTRE 1 A 100", "=" * 13, "|")
            print("|", " " * 57, "|")
            continue
        #

        # Errou ou acertou?
        if (acerto):
            print("| ", "-~*'¨¯¨'*·~" * 5, " |")
            print("| *'¨¯¨'*·~-~*'¨¯¨'*·~-( ACERTOU!!! )-~*'¨¯¨'*·~-~*'¨¯¨'*·~ |")
            break
        else:
            print("|", "_" * 10, "Errou", "_" * 40, "|")
            if chute_int > numero_aleatorio:
                print("| O numero aleatorio é MENOR que o numero ({: 4d})".format(chute_int), " " * 12, "|", sep="")
                print("|", "=" * 59, "|", sep="")
                print("|-", " " * 57, "-|", sep="")
            elif chute_int < numero_aleatorio:
                print("| O numero aleatorio é MAIOR que o numero ({: 4d})".format(chute_int), " " * 12, "|", sep="")
                print("|", "=" * 59, "|", sep="")
                print("|-", " " * 57, "-|", sep="")
        #

    print("|", "_" * 28, "FIM!", "_" * 27, "|", sep="")
    print("O numero é:", numero_aleatorio)


if (__name__ == "__main__"):
    jogar()
