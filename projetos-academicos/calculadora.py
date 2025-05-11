op = input("Operação: ")

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

if op == '+':
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")
