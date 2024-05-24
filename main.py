#lista de 15 nomes
nomes = ['Lucas','isabela','Eladio','Marcia','Luiza','Pedro','Joao','Maria','Ciclano','Beltrano','Zeze','Jose','didi','dedé','chaves']

#usuario informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ')

#retorna o indice do nome pesquisado
indice = nomes.index(nome)
# verifica se o nome está na lista ou não
if nome in nomes:
    print(f'Nome encontrado: {nome} no indice {indice}.')
else:
    print(f'{nome} não encontrado na lista.')
