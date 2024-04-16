#%%
import time

qtde = int(input('Até quantos segundos você quer contar?'))
count = 0
while count <= qtde:
    print(count)
    time.sleep(1)
    count += 1
# %%

while True:
    senha = input('Digite a senha:')

    if senha == "1234":
        break
    else:
        print("Senha errada. Tente novamente!")

print('Acesso garantido.')
# %%

# print todos os numeros pares entre 2 numeros

inicio = int(input('Digite primeiro numero'))
fim = int(input('Digite ultimo numero'))

print (f'Os números pares entre {inicio} e {fim} são:')
if inicio // 2 != 0:
    inicio += 1

while inicio <= fim:
    print(inicio)
    inicio += 2
# %%
