telefones = {"elayne": 40028922, "natalia": 4124492}
print(telefones)

lista1 = ["brigadeiro","leite condesado, achocolatado"]
lista2= ["omelete","ovos, azeite, condiimentos a gosto"]
lista3 = ["ovo frito", "ovo, óleo, condimentos a gosto"]
listaReceita = [lista1, lista2, lista3]
print(listaReceita)

receitas = dict(listaReceita)
print(receitas) 

semana = {}
aula1 = ["segunda", "POO, WEB"]
aula2 = ["terca", "WEB, POO"]
aula3 = ["quarta", "WEB, POO, Padrao de Projeto"]
aula4 = ["quinta", "Redes"]
aula5 = ["sexta", "Redes,POO, WEB"]
aulas = [aula1, aula2, aula3, aula4, aula5]
semana = dict(aulas)
print(semana)