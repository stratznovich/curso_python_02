
'''Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser
fornecida pelo usuário.
'''

entrada = int(input(f'insira a quantidade de numeros a ser digitados: '))
funcao = 1 
soma = 0
contador = []

while funcao <= entrada:
    valor = int(input(f'{funcao} insira {entrada} numeros positivos: '))
    funcao+=1
    contador.append(valor)
    maior = max(contador)
    menor = min(contador)
    soma = sum(contador)
    repeticao = contador.count(maior)
print(f'resultado: {soma} maior: {maior} manor: {menor} o numero {maior} ocorre por {repeticao} vezes: ')








