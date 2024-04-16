# %%

# print todos os numeros pares entre 2 numeros

inicio = int(input('Digite primeiro numero'))
fim = int(input('Digite ultimo numero'))

print (f'Os números pares entre {inicio} e {fim} são:')

for i in range(inicio,(fim+1)):
    if i % 2 == 0:
        print(i)

# %%
