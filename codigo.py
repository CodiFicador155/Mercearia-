#Versão: 1.0.0
#Autor: João Augusto
#Quem editar esse código, por favor, mude o Autor para Autores e adicione uma virgula depois de meu nome e coloque o seu.  
#Descrição: Simples Programa de soma de uma venda
cont  = 0 # Variável que controla a continuação da soma
valor = 0 # Variável que pega o valor do produto
quant = 0 # Variável que pega a quantidade de produtos
total = 0 # Total da Venda
print('…./””””””””|======[]')           #Logo da software
print('…./””””””””””””|')               #Logo da software
print('/”””””””””””””””””””””””””|')    #Logo da software
print('\(@) (@) (@) (@) (@) (@)/')      #Logo da software
print('     SOFWARE TANQUE  ')          #Logo da software
print('------------------------------------------------------------') # Imprime uma linha de separação do logo com o programa
while True:
    while cont != 5:#Responsável pela continuação doa soma dos produtos
        valor = float(input("Digite o preço do produto: ")) #Pega o preço dos produtos
        quant = int(input('Digite a quantidade: '))  #Pega a quantidade de Produtos
        cont = int(input('Deseja continuar 1-sim 2-não: ')) #Pega se o usuário deseja continuar com a soma dos valores
        total = total+valor*quant # Soma todos os dados pegados
        if(cont != 1): #Verifica e Faz que mostre o total da venda
            print('Total: ',total) #Mostra o total da venda
            valor = 0 # Variável que pega o valor do produto
            quant = 0 # Variável que pega a quantidade de produtos
            total = 0 # Total da Venda

