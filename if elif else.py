'''
Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00
Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00
Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00
Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário
'''

tamanho_cabelo = 55

if tamanho_cabelo <= 20:
    print('O custo do seu corte é R$50 reais')
elif 21 <= tamanho_cabelo <= 30:
    print('O custo do seu corte é R$70 reais')
elif 31 <= tamanho_cabelo <= 50:
    print('O custo do seu corte é R$100 reais')
else:
    print('Por favor consultar na recepção')