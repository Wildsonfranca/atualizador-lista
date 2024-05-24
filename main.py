#lista de nomes 
nomes =['Alex','Fernanda','Carlos','Carla','joana','josé']

#usuario informa o indice que deseja alterar 
indice = int(input('Informe o indice que deseja alterar :'))
indice -= 1
#usuario informa  o novo nome
nomes[indice] = input('Informe o novo nome:')
#exibe a lista 
for nome in nomes:
    print(nome)

