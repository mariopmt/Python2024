#%%

idade = int(input("Informe sua idade:"))
cnh = input("Você tem CNH ")

if idade >= 18 and cnh == "sim":
    print("Não será multado")
else:
    print("Será multado")

condicao = idade >= 18 and cnh == "sim"
print(condicao)
# %%


#A tabela verdade AND
#só será True se todas condições forem True
#basta apenas 1 condição False para a tabela ser False


#A tabela verdade OR
#se ao menos uma condição for True, a tabela será True
#para ser False, todas as condições devem ser False

