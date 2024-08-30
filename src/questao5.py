# Questão 5: Inversão de String

def inverter_string(s):
    return s[::-1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python questao5.py <string>")
        sys.exit(1)
    
    string = sys.argv[1]
    string_invertida = inverter_string(string)
    print(f"String invertida: {string_invertida}")
