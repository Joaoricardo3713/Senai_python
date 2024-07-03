''' 
programador : Josue Rosario
Descricao : Calcular a area de um quadrado
Alteracoes :
03 07 2024 - criacao do programa
'''

# variavel ->  o nome de um pedacinho de memoria
# input() ->pega dados do usuário (retorna string str)
# type() -> o tipo da variavel
# somar -> use +
# dividir e multiplicar use / e *
# elevar ao quadrado use **  ex: 2**2 significa dois elevado ao quadrado

lado = input("digite o lado do quadrado") # pega dados do usuario
print(type(lado)) # imprime o tipo da variavel
area = int(lado)**2 

# imprimindo dados na tela
print("area do quadrado :",area)
print("area do quadrado :" + str(area)) # o mais aqui é operador de concatenacao
print(f'area do quadrado : {str(area)} metros quadrados') #como usar f string