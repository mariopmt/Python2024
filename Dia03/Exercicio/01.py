#%%

#Faça um programa que verifique se a pessoa pertence à família "Tavares"


nome = input("Entre com seu nome completo: ").lower()

if "tavares" in nome or "silva" in nome:
    print("Você pertence à família Tavares e/ou à família Silva")
else:
    print('Não sei sua família!')
# %%
