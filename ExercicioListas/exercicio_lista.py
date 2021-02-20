""" Crie uma lista com o nome das 3 pessoas mais próximas. """

nomeDePessoasProximas = ["Elayne", "Natalia", "Argollo"]
print(nomeDePessoasProximas)

""" Crie três listas, uma lista de cada coisa a seguir:
• frutas
• docinhos de festa (não se esqueça de brigadeiros!!)
• ingredientes de feijoada """

frutas = ["maça", "banana", "morango"]
docinhosDeFesta = ["brigadeiro", "olho de sogra", "cajuzinho"]
ingredientesFeijoada = ["carne", "feijao", "bacon"]
print("{}\n{}\n{}".format(frutas,docinhosDeFesta,ingredientesFeijoada))

""" Agora crie uma lista com essas três listas. """ 

lista = frutas + docinhosDeFesta + ingredientesFeijoada
print("União de todas as listas {}".format(lista))

""" você consegue acessar o elemento brigadeiro? """
print(lista[lista.index('brigadeiro')])

""" Adicione mais brigadeiros à segunda lista de listona. """
docinhosDeFesta.append("brigadeiro")
print(docinhosDeFesta)

""" Adicione bebidas ao final da listona, mas sem criar uma lista! """
lista.append(["coca-cola", "fanta"])
print(lista)

lista1A200 = list(range(1,200))
print(lista1A200)

listaDe5em5 = list(range(0,30,5))
print(listaDe5em5)