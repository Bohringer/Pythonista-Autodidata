# DESAFIO 🥇
# Calcule quantos dias faltam até o seu aniversário
from datetime import datetime

aniversario = datetime(2025, 2, 4)
dias_restante = aniversario - datetime.now()
print(dias_restante)

# Com input

inserir_aniversario = datetime.strptime(input('Quando é seu proximo aniversario? '),'%d/%m/%Y')
data_aniversario = inserir_aniversario - datetime.now()

print('Faltam {} dias para seu aniversario!'.format(data_aniversario.days))
print(f'Faltam {data_aniversario.days} dias para seu aniversario!')

