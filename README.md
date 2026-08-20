# Calculadora Básica em Python

**Disciplina:** Garantia da Qualidade de Software
**Curso:** Gestão e Qualidade de Software
**Professor:** Daniel Henrique Matos de Paiva

---

## ▶️ Como executar?

Para executar o programa pelo terminal, siga os passos abaixo.

### 1. Abra o terminal

Abra o **Prompt de Comando (CMD)** ou o terminal do VS Code.

### 2. Acesse a pasta do projeto

Utilize o comando:

```bash
cd C:\Users\kaior\Documents\gqs-algoritmo-02-py
```

### 3. Execute o programa

Digite o seguinte comando:

```bash
python main.py
```

### 4. Utilize a calculadora

O programa solicitará dois números e apresentará as opções de operação:

```text
Digite o primeiro número: 10
Digite o segundo número: 5

Escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite o número da operação: 1
```

---

# Nível 2: Documentação e Explicação do Algoritmo

## O que o código faz?

O programa desenvolvido é uma **calculadora básica em Python**. Seu objetivo é permitir que o usuário informe dois números e escolha uma operação matemática entre adição, subtração, multiplicação ou divisão.

Após a escolha, o programa realiza o cálculo e apresenta o resultado no console.

---

## Detalhamento do código

### `print()`

A função `print()` é utilizada para exibir informações na tela, como o título da calculadora, as opções disponíveis e o resultado da operação.

Exemplo:

```python
print("CALCULADORA BÁSICA")
```

### `input()`

A função `input()` é utilizada para receber informações digitadas pelo usuário.

Exemplo:

```python
numero1 = float(input("Digite o primeiro número: "))
```

### `float()`

A função `float()` transforma o valor digitado pelo usuário em um número decimal, permitindo realizar operações matemáticas.

### `if`, `elif` e `else`

As estruturas condicionais são utilizadas para verificar qual operação foi escolhida pelo usuário.

Exemplo:

```python
if operacao == "1":
    resultado = numero1 + numero2

elif operacao == "2":
    resultado = numero1 - numero2

else:
    print("Opção inválida.")
```

O programa também possui uma verificação para impedir a divisão por zero.

---

## Exemplo de saída

Exemplo real de execução do programa:

```text
=================================
       CALCULADORA BÁSICA
=================================
Digite o primeiro número: 10
Digite o segundo número: 5

Escolha uma operação:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
Digite o número da operação: 1

Resultado: 10.0 + 5.0 = 15.0
```

---
## Autor

**Kaio Moreira - 32510906**

**Erick Mello - 326211590**

**Icaro Ferreira - 325111358**

Projeto desenvolvido como atividade acadêmica da disciplina de **Garantia da Qualidade de Software**, sob orientação do professor **Daniel Paiva**.
