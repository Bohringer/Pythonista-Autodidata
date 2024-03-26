# DESAFIOS🥇
# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1

# DESAFIO 1 
contador = 1
while contador <= 120:
	print(contador)
	contador += 1
	

# DESAFIO 2
senha = ''
while senha != 'secreto':
 senha = input('Digite sua senha: ')
print('Bem-vindo!')


# DESAFIO 3
contador = 100
while contador >= 1:
 print(contador)
 contador -= 1