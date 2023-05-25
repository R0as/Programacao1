qtd = True
#####################################
peso = float(input("Digite seu peso:"))
idade = int(input("Digite sua idade:"))
if idade < 18 and idade >= 16:
    autorizacao = input("Você possui autorização?")
boaSaude = input("Boa saúde?")
drogas = input("Usa drogas injetáveis?")
primeiraVez = input("primeira vez que doa?")
if primeiraVez == "n" or primeiraVez == "N":
    mesesDaUltima = int(input("Quantos meses desde sua última doação?"))
    qtdDoacoes = int(input("Quantas vezes você doou dentro do prazo de um ano?"))
sexo = input("Seu sexo")
if sexo == "f" or sexo == "F":
    gravidez = input("Está grávida?")
    amamentando = input("Está amamentando?")
    if amamentando == "s" or amamentando == "S":
        idadeBB = int(input("Qual a idade do bebe em meses?"))
###########################################
print("Peso:", peso)
print("Idade:", idade)
if idade < 18 and idade >= 16:
    if autorizacao == "N" or autorizacao == "n" or autorizacao == "S" or autorizacao == "s":
        print("Documento de autorizacao:", autorizacao)
print("Boa saude:", boaSaude)
print("Uso drogas injetaveis:", drogas)
print("Primeira doacao:", primeiraVez)
if primeiraVez == "n" or primeiraVez == "N":
    print("Meses desde ultima doacao:", mesesDaUltima)
    print("Doacoes nos ultimos 12 meses:", qtdDoacoes)
print("Sexo biologico:", sexo)
if sexo == "f" or sexo == "F":
    print("Gravidez:", gravidez)
    print("Amamentando:", amamentando)
    if amamentando == "s" or amamentando == "S":
        print("Meses bebe:", idadeBB)
#############################################################impedimentos
if peso < 50:
    qtd = False
    print("Impedimento: abaixo do peso minimo.")
if idade < 16:
    qtd = False
    print("Impedimento: menor de 16 anos.")
elif idade < 18:
    if autorizacao == "N" or autorizacao == "n":
        qtd = False
        print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
if idade > 60 and idade <= 69:
    if primeiraVez == "s" or primeiraVez == "S":
        qtd = False
        print("Impedimento: maior de 60 anos, primeira doacao.")
elif idade > 69:
    qtd = False
    print("Impedimento: maior de 69 anos.")
if boaSaude == "n" or boaSaude == "N":
    qtd = False
    print("Impedimento: nao esta em boa saude.")
if drogas == "S" or drogas == "s":
    qtd = False
    print("Impedimento: uso de drogas injetaveis.")
if sexo == "m" or sexo == "M":
    if primeiraVez == "n" or primeiraVez == "N": 
        if mesesDaUltima < 2:
            qtd = False
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        if qtdDoacoes >= 4:
            qtd = False
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
if sexo == "f" or sexo == "F":
    if primeiraVez == "n" or primeiraVez == "N":    
        if mesesDaUltima < 3:
            qtd = False
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        if qtdDoacoes >= 3:
            qtd = False
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    if gravidez == "s" or gravidez == "S":
        qtd = False
        print("Impedimento: gravidez.")
    if amamentando == "s" or amamentando == "S": 
        if idadeBB < 12:
            qtd = False               
            print("Impedimento: amamentacao.")
if qtd == True:
    print("Procure um hemocentro.")   
    