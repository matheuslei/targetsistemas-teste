# Questão 2: Verificação de Número na Sequência de Fibonacci

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python questao2.py <numero>")
        sys.exit(1)
    
    try:
        numero = int(sys.argv[1])
    except ValueError:
        print("O número informado não é válido.")
        sys.exit(1)

    if is_fibonacci(numero):
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")
