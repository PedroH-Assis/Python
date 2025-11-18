secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo             |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("Digite um numero: "))

while number != secret_number:

    print("HA HA HA VOCÊ ESTÁ PRESO NO MEU LOOP!!")

    number = int(input("Digite um numero: "))

print(secret_number)

print("Parabéns, você saiu do loop")

