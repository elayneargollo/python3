
""" Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles. """

numero1 = 2
numero2 = 4

if numero1 > numero2:
  print("{} é maior que {}".format(numero1, numero2))
else: print("{} é maior que {}".format(numero2, numero1))

""" Para doar sangue é necessário 1 :
• Ter entre 16 e 69 anos.
• Pesar mais de 50 kg.
• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).
Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h para uma pessoa e diga se ela
pode doar sangue ou não. """

idade = int(input("Quantos anos você tem ?"))
peso = int(input("Qual seu peso ?"))
horarioDormir = int(input("Quanto dormiu nas ultimas 24h ?"))

if idade >= 16 and idade <= 69 and peso > 50 and horarioDormir >= 6: 
    print("Você pode doar sangue")
else: print("Você não pode doar sangue")