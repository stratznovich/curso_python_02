"""Faça um programa que leia um número inteiro positivo N e imprima todos os números
de O até N em crescente"""

entrada = int(input('insira um valor qualquer: '))
contador = 0
resultado = 0
while contador <= entrada:
    print(f'{contador} resultado: {resultado}')
    contador += 1
    resultado += 1
