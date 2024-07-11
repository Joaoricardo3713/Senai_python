#Escreva um programa que pergunte a velocidade de um carro e a velocidade permitida e mostre:
# - A velocidade do carro
# - A porcentagem em que o carro ultrapassou a velocidade

# - Quantos pontos serão atribuídos na carteira
# - O tipo de infração (média, grave ou gravíssima)

# - O valor da multa.

# Considere os seguintes dados
# a) superior à máxima em até 20% : infração média (4 pontos) + multa no valor de R$ 130,16;
# b) superior à máxima permitida em mais de 20% até 50% : infração grave (5 pontos) + multa no valor de R$ 195,23;
# c) superior à máxima permitida em mais de 50% : infração gravíssima (7 pontos) + multa no valor de R$ 880,41+ suspensão da CNH e curso de reciclagem.





veiculoveloci = float(input("Digite a velocidade do veiculo"))

velocidademaxima = 100
velocidadeUltrapassada = float((veiculoveloci-velocidademaxima)/100)

velocidadePorcentagem = int(f'{velocidadeUltrapassada * 100:.0f}') #andando a virgula, assim fica como no exemplo: 10

print(f'{velocidadePorcentagem}') 

if (velocidadePorcentagem <=20): 
    print(f" a velocidade do carro foi de {veiculoveloci}km/h")
    print(f"a velocidae ultaprassada foi de {velocidadePorcentagem}% infração média (4 pontos) + multa no valor de R$ 130,16")

else:
    print("nao será multado")

if ((velocidadePorcentagem >20) and (velocidadePorcentagem <= 50)): 
    print(f" a velocidade do carro foi de {veiculoveloci}km/h")
    print(f" a velocidae ultaprassada foi de {velocidadePorcentagem}% infração grave (5 pontos) + multa no valor de R$ 195,23")

else:
    print("nao será multado")
    
if (velocidadePorcentagem >=50): 
    print(f" a velocidade do carro foi de {veiculoveloci}km/h")
    print(f" a velocidae ultaprassada foi de {velocidadePorcentagem}% infração gravíssima (7 pontos) + multa no valor de R$ 880,41+ suspensão da CNH e curso de reciclagem.")

else:
    print("nao será multado")






