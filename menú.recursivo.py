mport math

# Função para calcular a hipotenusa
def calcular_hipotenusa(cateto_oposto: float, cateto_adjacente: float) -> float:
    return math.sqrt(cateto_oposto*2 + cateto_adjacente*2)

# Função para calcular seno, cosseno e tangente
def calcular_trigonometria(cateto_oposto: float, cateto_adjacente: float) -> tuple:
    hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)
    
    seno = cateto_oposto / hipotenusa
    cosseno = cateto_adjacente / hipotenusa
    tangente = cateto_oposto / cateto_adjacente if cateto_adjacente != 0 else "Indefinido"
    
    return seno, cosseno, tangente

# Função para o menu do Teorema de Pitágoras
def menu_teorema_de_pitagoras():
    while True:
        print("\nMenu do Teorema de Pitágoras")
        print("1. Calcular Hipotenusa (Cateto Oposto e Cateto Adjacente)")
        print("2. Calcular Cateto Adjacente (Hipotenusa e Cateto Oposto)")
        print("3. Calcular Cateto Oposto (Hipotenusa e Cateto Adjacente)")
        print("4. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cateto_oposto = float(input("Digite o valor do cateto oposto: "))
            cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
            hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)
            print(f"A hipotenusa é: {hipotenusa:.4f}")
        elif escolha == '2':
            hipotenusa = float(input("Digite o valor da hipotenusa: "))
            cateto_oposto = float(input("Digite o valor do cateto oposto: "))
            cateto_adjacente = math.sqrt(hipotenusa*2 - cateto_oposto*2)
            print(f"O cateto adjacente é: {cateto_adjacente:.4f}")
        elif escolha == '3':
            hipotenusa = float(input("Digite o valor da hipotenusa: "))
            cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
            cateto_oposto = math.sqrt(hipotenusa*2 - cateto_adjacente*2)
            print(f"O cateto oposto é: {cateto_oposto:.4f}")
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")

# Função para o menu de Trigonometria
def menu_trigonometria():
    while True:
        print("\nMenu de Trigonometria")
        print("1. Calcular Seno")
        print("2. Calcular Cosseno")
        print("3. Calcular Tangente")
        print("4. Voltar ao Menu Principal")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
            cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
            seno, _, _ = calcular_trigonometria(cateto_oposto, cateto_adjacente)
            print(f"Seno: {seno:.4f}")
        elif escolha == '2':
            cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
            cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
            _, cosseno, _ = calcular_trigonometria(cateto_oposto, cateto_adjacente)
            print(f"Cosseno: {cosseno:.4f}")
        elif escolha == '3':
            cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
            cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
            _, _, tangente = calcular_trigonometria(cateto_oposto, cateto_adjacente)
            print(f"Tangente: {tangente}")
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")

# Menu principal
def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Teorema de Pitágoras")
        print("2. Funções Trigonométricas")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_teorema_de_pitagoras()
        elif escolha == '2':
            menu_trigonometria()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Inicia o programa
menu_principal()
