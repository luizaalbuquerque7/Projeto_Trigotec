import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

# Solicitar entrada do usuário
cateto_a = float(input("Digite o comprimento do cateto A: "))
cateto_b = float(input("Digite o comprimento do cateto B: "))

# Calcular a hipotenusa
hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

# Exibir o resultado
print(f"A hipotenusa é: {hipotenusa:.2f}")