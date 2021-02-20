import math

print('Python é legal ! Mas não o "legal" como dizem para outras coisas')
print("Python é legal ! Mas não o 'legal como dizem para outras coisas")
print('Olha esse textão sobre aspas simples e dúplas.\nIsso aqui é aspas duplas:"\nIsso aqui é aspas simples: \'')

#Exercicio Operadores matemáticos

#Calcule o resto da divisão de 10 por 3.
print("Resto da divisao de 10 por 3 é" ,10%3)

#Calcule a área de um círculo de raio r = 2.
print("Área do círculo de r = 2 é", (2**2)*math.pi)

# Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber
# quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!
quantidadeMeses = 4
quantidadeAulasPorSemana = 2
totalDeAulasPorMes = quantidadeAulasPorSemana * 4
quantidadeTotalDeAulas = totalDeAulasPorMes * quantidadeMeses
quantidadeDeAulasQuePodeFaltar = quantidadeTotalDeAulas*(25/100)
print("Davinir pode faltar no máximo ",quantidadeDeAulasQuePodeFaltar, "aulas")

#Quantos segundos há em 3 horas, 23 minutos e 17 segundos?
hora = 3
minuto = 23
segundos = 17
quantidadeDeSegundos = segundos + (3*3600) + (minuto*60)
print("3h23min17seg tem ", quantidadeDeSegundos, "segundos")

#Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?
quilomentro = 65
print("Velocidade media é ",(quilomentro*1000)/quantidadeDeSegundos, "m/s")

#Resolva essa expressão: 100 − 413 · (20 − 5 × 4) / 5
print("Resolução da expressão é ", (100 - (413*(20 - (5*4))))/5)

# Se ele ligar os três em paralelo, a capacitância resultante é a soma: Cp = C1 + C2 + C3
#Qual é o valor resultante em cada um desses casos?

capacitor1 = 10
capacitor2 = 22
capacitor3 = 6.8
capacitanciaEmParalelo = capacitor1 + capacitor2 + capacitor3
capacitanciaEmSerie = (1/capacitor1) + (1/capacitor2) + (1/capacitor3)
capacitanciaEmSerie = 1 /capacitanciaEmSerie
print("Capacitância em paralelo é ", capacitanciaEmParalelo, "\nCapacitância em série é ", capacitanciaEmSerie)

#Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e
#compraram alguns itens:
#• 75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
#• 2 pacotes de macarrão: R$ 8,73 cada
#• 1 pacote de Molho de tomate: R$ 3,45
#• 420g Cebola: R$ 5,40/kg
#• 250g de Alho: R$ 30/kg
#• 450g de pães franceses: R$ 25/kg

quantidadeDeIntegrantes = 5
cerveja = 2.20*75
macarrao = 8.73*2
molho = 3.45
cebola = (0.001*420) * 5.40 
alho = (0.001*250) * 30
pao = (0.001*450) * 25
somaDasCompras = cerveja + macarrao + molho + cebola + alho + pao
print("Cada um tem que pagar R$",somaDasCompras/quantidadeDeIntegrantes)


