#Faça um programa que receba uma quantidade indefinida de valores correspondentes a "saldo em conta"
#mas quando o usuário aperter enter sem digitar valor algum o programa para de receber valores e exibe a soma
#de todos os valores digitados anteriormente

#%%
total = 0

while True:
    entrada = input('Entre com o valor depositado: ')
    if entrada == '':
        break

    total += float(entrada)

print(f'Saldo atual é de R${total}')
# %%
