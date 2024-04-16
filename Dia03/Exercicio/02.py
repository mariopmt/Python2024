#faça um programa que retorne quantas letras a existem em uma palavra

palavra = input('Digite uma palavra: ').lower()

qtde = 0

for i in palavra:
    if i == 'a':
        qtde += 1

print(f'Na palavra {palavra} ocorrem {qtde} letras "a"')