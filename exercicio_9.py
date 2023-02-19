"""Faça um programa que leia um número inteiro - e depois imprima os N primeiros
números naturais ímpares."""

entrada = int(input('insira um numero qualquer'))
impar = 1
contador  = 1
while contador <= entrada:
    print(f' {contador} numeros impares : {impar}')
    impar += 2
    contador += 1



    
