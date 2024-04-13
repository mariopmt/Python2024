#%%

#Faça um programa que vende uma garrafa de água:
#R$1,50 sem gás e R$2,50 com gás
#Pergunte a quantidade

escolha = input("Agua com gás ou sem gás: ")
qtde = int(input("Quantas você quer: "))

if escolha == "com":
    print("Preço da água com gás é R$2,50")
    total = qtde * 2.5
else:
    print("Preço da água sem gás é R$1,50")
    total = qtde * 1.5

print("O total de sua conta é R$",total)
# %%
