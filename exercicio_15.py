"""Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números ímpares de 1 até N em ordem crescente."""

entrada = int(input('insira um valor acima de 1: '))
contador = 1
while contador <= entrada:
    print(contador)
    contador += 2