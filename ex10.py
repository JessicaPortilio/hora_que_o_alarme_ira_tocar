hora_atual = int(input("Entre com a hora atual: "))
tempo_espera = int(input("Entre com o número de horas de espera: "))
hora_alarme = (hora_atual+tempo_espera)%12
print("O alarme irá tocar às " + str(hora_alarme) + " horas.")