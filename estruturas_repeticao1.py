entrada_idade = ''  #deckarando variável string de valor nulo 

while str(entrada_idade) != '0': #verificação do valor digitado
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    print(f'Número digitado: {entrada_idade}')  #mostra o valor digitado se for diferente de zero
