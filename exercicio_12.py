"""Faça um programa que leia um rúmero inteiro positivo par N e imprima todos os números
pares de O até N em ordem decrescente."""

entrada = int(input('insira um valor qualquer: '))
contador = 0
resultado = entrada
while resultado >= 0:
    print(f'{contador} resultado: {resultado}')
    contador += 1
    resultado -= 1
