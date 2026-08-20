print("=================================")
print("       CALCULADORA BÁSICA")
print("=================================")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação: ")

if operacao == "1":
    resultado = numero1 + numero2
    print(f"\nResultado: {numero1} + {numero2} = {resultado}")

elif operacao == "2":
    resultado = numero1 - numero2
    print(f"\nResultado: {numero1} - {numero2} = {resultado}")

elif operacao == "3":
    resultado = numero1 * numero2
    print(f"\nResultado: {numero1} × {numero2} = {resultado}")

elif operacao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\nResultado: {numero1} ÷ {numero2} = {resultado}")
    else:
        print("\nErro: não é possível dividir por zero.")

else:
    print("\nOpção inválida.")