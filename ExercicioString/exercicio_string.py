# Strings (sequência de caracteres)!

""" Dada a frase Python é muito legal., use fatiamento para dar nome às variáveis contendo cada palavra. """

frase = "Python é muito legal."

primeiraPalavraFrase = frase[:6]
segundaPalavraFrase = frase[7:9]
terceiraPalavraFrase = frase[9:14]
quartaPalavraFrase = frase[14:20]
print(primeiraPalavraFrase + " " + segundaPalavraFrase + " " + terceiraPalavraFrase + " " + quartaPalavraFrase)

""" Agora que conhecemos atribuição múltipla e o método str.split() refaça os dois exercícios anteriores
usando essas técnicas. """

separacao = frase.split()

primeiraPalavra = separacao.pop(0)
segundaPalavraFrase = separacao.pop(0)
terceiraPalavraFrase = separacao.pop(0)
quartaPalavraFrase = separacao.pop(0)
print(primeiraPalavra + " " + segundaPalavraFrase + " " + terceiraPalavraFrase + " " + quartaPalavraFrase)

""" Qual o tamanho dessa frase? E qual o tamanho de cada palavra? """

print("Tamanho da frase é",len(frase))
print("Tamanho da primeira palavra é",len(primeiraPalavraFrase))
print("Tamanho da segunda palavra é",len(segundaPalavraFrase))
print("Tamanho da terceira palavra é",len(terceiraPalavraFrase))
print("Tamanho da quarta palavra é",len(quartaPalavraFrase))

""" Use slicing (mais especificamente o passo do fatiamento) para inverter a string «Python». """
palavra = "Python"
ultimaLetra = palavra[::-1]
print(ultimaLetra)

""" Leia um nome pelo teclado e imprima "Olá, <nome lido>!" """
nomeInformado = input("Digite seu nome: ")
frase = "Olá, {} !".format(nomeInformado)
print(frase)

""" Leia outro nome pelo teclado e imprima:
<nome lido> roubou pão na cassa do <nome2 lido>!
<nome2 lido> ficou triste e com fome,
porque o bandejão estava fechado. """

outroNomeInformado = input("Digite outro nome: ")
frase = "{} roubou pão na casa do {}".format(nomeInformado, outroNomeInformado)
print(frase)

frase = "{} ficou triste e com fome,\nporque o bandejão estava fechado.".format(outroNomeInformado)
print(frase)

""" Leia uma frase pelo teclado e a imprima ao contrário. """
frase = input("Escreva um frase qualquer: ")
fraseInversa = frase[::-1]
print(fraseInversa)

