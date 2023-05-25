from os import system , name 					
def limpaTela ():			
	"""Função usada para limpar a tela"""
	if name == 'nt':
		system('cls')
	else:
		system('clear ')

def estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES):
    """função destinada ao controle de estoque e o produto escolhido pelo consumidor"""
    print("-"*80)
    if CEBOLITOS>0 or RUFFLES>0 or SENSAÇÕES>0 or CHEETOS>0 or DORITOS>0:#quando qualquer um dos produtos for maior que 0 vai printar todos os produtos disponiveis ou aqueles que nao há no estoque
        if CEBOLITOS>0:#se a quantidade de produto for maior que 0 vai printar o preco e a quantidade de produto disponivel
            print("1 - CEBOLITOS        - Quantidade disponível em estoque: {}  - R$5,00".format (CEBOLITOS))
        else:#quando a quantidade de produtos for 0 vai printar que nao há estoque
            print("1 - CEBOLITOS        - Produto Indisponível!")
        if DORITOS>0:#se a quantidade de produto for maior que 0 vai printar o preco e a quantidade de produto disponivel
            print("2 - DORITOS          - Quantidade disponível em estoque: {}  - R$5,50 ".format (DORITOS))
        else:#quando a quantidade de produtos for 0 vai printar que nao há estoque
            print("2 - DORITOS          - Produto Indisponível!")
        if CHEETOS>0:#se a quantidade de produto for maior que 0 vai printar o preco e a quantidade de produto disponivel
            print("3 - CHEETOS          - Quantidade disponível em estoque: {}  - R$4,50".format (CHEETOS))
        else:#quando a quantidade de produtos for 0 vai printar que nao há estoque
            print("3 - CHEETOS          - Produto Indisponível!")
        if RUFFLES>0:#se a quantidade de produto for maior que 0 vai printar o preco e a quantidade de produto disponivel
            print("4 - RUFFLES          - Quantidade disponível em estoque: {}  - R$3,50".format (RUFFLES))
        else:#quando a quantidade de produtos for 0 vai printar que nao há estoque
            print("4 - RUFFLES          - Produto Indisponível!")
        if SENSAÇÕES>0:#se a quantidade de produto for maior que 0 vai printar o preco e a quantidade de produto disponivel
            print("5 - SENSAÇÕES        - Quantidade disponível em estoque: {}  - R$4,00".format (SENSAÇÕES))
        else:#quando a quantidade de produtos for 0 vai printar que nao há estoque
            print("5 - SENSAÇÕES        - Produto Indisponível!")
    elif CEBOLITOS == 0 and DORITOS == 0 and RUFFLES == 0 and SENSAÇÕES == 0:#vai printar que não há estoque quando não tiver nenhum produto disponivel
        print("Desculpe, mas estamos sem estoque no momento, volte outra hora, desde já agradecemos a sua preferência.")
        print("-"*80) 
        return 0
    print("-"*80)
    produtos = int(input("\nEscolha o seu produto:"))#variável destinada a escolha do produto
    limpaTela()

    if produtos == 1:
        if CEBOLITOS>0:
            limpaTela()
            print("Você escolheu CEBOLITOS")
            print("Preço = R$ 5,00")
            CEBOLITOS -= 1#tirar 1 deste produto do estoque
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)#chama a função responsavel pelo pagamento do produto
        
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N")
            if y == "S" or y == "s":#chama se a pessoa quer comprar outro produto
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto
            elif y == "n" or y == "N":#encerra o programa
                limpaTela()
                print("Obrigado por comprar conosco, Volte sempre!")
                return 0
            else:#chama se a string inserida for diferente de s/n
                limpaTela()
                print("Operação Inválida")
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto

    elif produtos == 2:
        if DORITOS>0:
            limpaTela()
            print("Você escolheu DORITOS")
            print("Preço = R$ 5,50")
            DORITOS -= 1#tirar 1 deste produto do estoque
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)#chama a função responsavel pelo pagamento do produto
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N")
            if y == "S" or y == "s":#chama se a pessoa quer comprar outro produto
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto
            elif y == "n" or y == "N":#encerra o programa
                limpaTela()
                print("Obrigado por comprar conosco, Volte sempre!")
                return 0
            else:#chama se a string inserida for diferente de s/n
                limpaTela()
                print("Operação Inválida")
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto

    elif produtos == 3:
        if CHEETOS>0:
            limpaTela()
            print("Você escolheu CHEETOS")
            print("Preço = R$ 4,50")
            CHEETOS -= 1#tirar 1 deste produto do estoque
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)#chama a função responsavel pelo pagamento do produto
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N")
            if y == "S" or y == "s":#chama se a pessoa quer comprar outro produto
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto
            elif y == "n" or y == "N":#encerra o programa
                limpaTela()
                print("Obrigado por comprar conosco, Volte sempre!")
                return 0
            else:#chama se a string inserida for diferente de s/n
                limpaTela()
                print("Operação Inválida")
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto

    elif produtos == 4:
        if RUFFLES>0:
            limpaTela()
            print("Você escolheu RUFFLES")
            print("Preço = R$ 3,50")
            RUFFLES -= 1#tirar 1 deste produto do estoque
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)#chama a função responsavel pelo pagamento do produto
        
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N")
            if y == "S" or y == "s":#chama se a pessoa quer comprar outro produto
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto
            elif y == "n" or y == "N":#encerra o programa
                limpaTela()
                print("Obrigado por comprar conosco, Volte sempre!")
                return 0
            else:#chama se a string inserida for diferente de s/n
                limpaTela()
                print("Operação Inválida")
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)   #chama a funcao estoque denovo pra comprar outro produto                             

    elif produtos == 5:
        if SENSAÇÕES>0:
            limpaTela()
            print("Você escolheu SENSAÇÕES")
            print("Preço = R$ 4,00")
            SENSAÇÕES -= 1#tirar 1 deste produto do estoque
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,)#chama a função responsavel pelo pagamento do produto
        else:
            limpaTela()
            print("Produto indisponível")
            y = input("Deseja comprar outro produto? S/N")
            if y == "S" or y == "s":#chama se a pessoa quer comprar outro produto
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto
            elif y == "n" or y == "N":#encerra o programa
                limpaTela()
                print("Obrigado por comprar conosco, Volte sempre!")
                return 0
            else:#chama se a string inserida for diferente de s/n
                limpaTela()
                print("Operação Inválida")
                estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)#chama a funcao estoque denovo pra comprar outro produto
    else:#ocorre caso o valor inserido for diferente dos referidos dos produtos
        limpaTela()
        print("Operação não reconhecida")
        estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)


def deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,pagamento2=0):
    """Função destinada ao pagamento do produto comprado"""
    pagamento = float(input("\nInsira aqui o pagamento:"))
    pagamento2 = float(pagamento2 + pagamento)


    if produtos == 1:
        if pagamento2 < 5.00 and pagamento2 > 0:#acontece se o pagamento for maior que 0 e menor que o valor do produto
            limpaTela()
            print("Dinheiro insuficiente para o pagamento, insira o restante do pagamento.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,pagamento2)
        elif pagamento2 >= 5.00:#acontece se o dinheiro inserido for maior ou igual ao valor do produto
            limpaTela()
            troco = pagamento2 - 5.00
            print("Valor pago: R$ {:.2f}".format (pagamento2))
            print("Seu troco é: R$ {:.2f} ".format (troco))
            if troco > 0.00:#acontece se o dinheiro inserido for maior que o preço do produto
                print("\nPegue seu troco:")
            dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
        else:#acontece se o valor inserido for negativo
            limpaTela()
            print("Valor não aceito, insira um valor válido.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)
            
            
    elif produtos == 2:
        if pagamento2 < 5.50 and pagamento2 > 0:#acontece se o pagamento for maior que 0 e menor que o valor do produto
            limpaTela()
            print("Dinheiro insuficiente para o pagamento, insira o restante do pagamento.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,pagamento2)
        elif pagamento2 >= 5.50:#acontece se o dinheiro inserido for maior ou igual ao valor do produto
            limpaTela()
            troco = pagamento2 - 5.50
            print("Valor pago: R$ {:.2f}".format (pagamento2))
            print("Seu troco é: R$ {:.2f}".format (troco))
            if troco > 0.00:#acontece se o dinheiro inserido for maior que o preço do produto
                print("\nPegue seu troco:")
            dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
        else:#acontece se o valor inserido for negativo
            limpaTela()
            print("Valor não aceito, insira um valor válido.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)

    elif produtos == 3:
        if pagamento2 < 4.50 and pagamento2 > 0:#acontece se o pagamento for maior que 0 e menor que o valor do produto
            limpaTela()
            print("Dinheiro insuficiente para o pagamento, insira o restante do pagamento.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,pagamento2)

        elif pagamento2 >= 4.50:#acontece se o dinheiro inserido for maior ou igual ao valor do produto
            limpaTela()
            troco = pagamento2 - 4.50
            print("Valor pago: R${:.2f}".format (pagamento2))
            print("Seu troco é: R${:.2f}".format (troco))
            if troco > 0.00:#acontece se o dinheiro inserido for maior que o preço do produto
                print("\nPegue seu troco:")
            dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
        else:#acontece se o valor inserido for negativo
            limpaTela()
            print("Valor não aceito, insira um valor válido.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)

    elif produtos == 4:
        if pagamento2 < 3.50 and pagamento2 > 0:#acontece se o pagamento for maior que 0 e menor que o valor do produto
            limpaTela()
            print("Dinheiro insuficiente para o pagamento, insira o restante do pagamento.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,pagamento2)
        elif pagamento2 >= 3.50:#acontece se o dinheiro inserido for maior ou igual ao valor do produto
            limpaTela()
            troco = pagamento2 - 3.50
            print("Valor pago: R${:.2f}".format (pagamento2))
            print("Seu troco é: R${:.2f}".format (troco))
            if troco > 0.00:#acontece se o dinheiro inserido for maior que o preço do produto
                print("\nPegue seu troco:")
            dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
        else:#acontece se o valor inserido for negativo
            limpaTela()
            print("Valor não aceito, insira um valor válido.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)

    elif produtos == 5:
        if pagamento2 < 4.00 and pagamento2 > 0:#acontece se o pagamento for maior que 0 e menor que o valor do produto
            limpaTela()
            print("Dinheiro insuficiente para o pagamento, insira o restante do pagamento.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos,pagamento2)
        elif pagamento2 >= 4.00:#acontece se o dinheiro inserido for maior ou igual ao valor do produto
            limpaTela()
            troco = pagamento2 - 4.00
            print("Valor pago: R${:.2f}".format (pagamento2))
            print("Seu troco é: R${:.2f}".format (troco))
            if troco > 0.00:#acontece se o dinheiro inserido for maior que o preço do produto
                print("\nPegue seu troco:")
            dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
        else:#acontece se o valor inserido for negativo
            limpaTela()
            print("Valor não aceito, insira um valor válido.")
            deposito(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES,produtos)


def dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES):
    """função detinada a dar troco ao cliente"""
    troco +=0.000001
    if troco>=200:#troco para valores maiores de 200 reais
        print("R$200,00")
        troco=troco-200
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
    
    elif troco>=100:#troco para valores maiores de 100 reais
        print("R$100,00")
        troco=troco-100
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco>=50:#troco para valores maiores de 50 reais
        print("R$50,00")
        troco=troco-50
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
    
    elif troco>= 20:#troco para valores maiores de 20 reais
        print("R$20,00")
        troco=troco-20
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco>= 10:#troco para valores maiores de 10 reais
        print("R$10,00")
        troco = troco - 10
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco>=5:#troco para valores maiores de 5 reais
        print("R$5,00")
        troco = troco - 5
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco>=2:#troco para valores maiores de 2 reais
        print("R$2,00")
        troco = troco - 2
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco >=1:#troco para valores maiores de 1 real
        print("R$1,00")
        troco = troco - 1
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
    
    elif troco>= 0.50:#troco para valores maiores de 0.5 centavos
        print("R$0,50")
        troco = troco - 0.50
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco>= 0.25:#troco para valores maiores de 0.25 centavos
        print("R$0,25")
        troco = troco - 0.25
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco >= 0.10:#troco para valores maiores de 0.1 centavos
        print("R$0,10")
        troco = troco - 0.10
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco >= 0.05:#troco para valores maiores de 0.05 centavos
        print("R$0,05")
        troco = troco - 0.05
        dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

    elif troco < 0.05:# se o troco for menor que 0.05 encerra troco e pergunta se quer comprar outro produto
        x = input("\nGostaria de fazer outra compra? (S/N): ")
        if x == "s" or x == "S":#se for sim chama novamente a funcao responsavel pelo estoque para a compra de outro produto
            limpaTela()
            estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

        elif x == "n" or x == "N":#se a respota for nao encerra o programa
            limpaTela()
            print("Obrigado pela preferência, Volte sempre!")
            return 0

        else:#operação invalida chama dar troco denovopara perguntar se ele quer comprar outro produto
            limpaTela()
            print("operação inválida, Insira novamente:")
            dartroco(troco,CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)
            
def main():
    """funcao principal onde aplico valores as variaveis de quantidade de produtos e chama a função estoque"""
    CEBOLITOS = 5 #quantidade do produto em estoque
    DORITOS = 5 #quantidade do produto em estoque
    CHEETOS = 5 #quantidade do produto em estoque
    RUFFLES = 5 #quantidade do produto em estoque
    SENSAÇÕES = 5 #quantidade do produto em estoque
    estoque(CEBOLITOS,DORITOS,CHEETOS,RUFFLES,SENSAÇÕES)

main()