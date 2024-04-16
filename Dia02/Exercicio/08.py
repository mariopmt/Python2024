#Faça um programa que receba um número que representa uma quantidade de segundos
#e converta para HH:mm:ss

#%%
segundos = int(input('Entre com a qtde de segundos: '))

horas = segundos // 3600

segundos = segundos % 3600

minutos = segundos // 60

segundos = segundos % 60

print("{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
# %%
