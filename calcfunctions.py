from fractions import Fraction
import math

def somar():
    while True: 
        try:
            qtde = int(input('Quantos números você quer somar? '))
            break 
        except ValueError:
            print('Entrada inválida, digite um número INTEIRO! ')

    soma = 0 
    for i in range(qtde): 
        while True: 
            try: 
                numero = float(input(f'Digite o número para a soma: '))
                soma += numero
                break
            except ValueError:
                print('Entrada inválida, digite um número!')

    return soma

def multiplica():
    while True:
        try:
            qtde = int(input('Quantos números quer multiplicar? '))
            break
        except ValueError:
            print('Entrada inválida, digite um número INTEIRO! ')
    multi = 1
    for i in range(qtde):
        while True:
            try:
                numero = float(input(f'Digite o número para multiplicar '))
                multi *= numero
                break
            except ValueError:
                print('Entrada inválida, digite um número!')
    return multi

def subtrai(numero1, numero2):
    return numero1-numero2
            
def divide(numero1,numero2):
    try:
        return numero1/numero2
    except ZeroDivisionError:
        print('Divisão por zero.')

def potencia(numero1,numero2):
    return numero1**numero2
    
def raizquad(numero):
    try:
        return math.sqrt(numero)
    except (ValueError, TypeError):
        print('Entrada digitada inválida, digite um número! ')
        
def cosseno(angulo):
    return math.cos(math.radians(angulo))
    
def seno(angulo):
   return math.sin(math.radians(angulo))
    
def logaritmo(numero, base):
    return math.log(numero, base)
    
def perimetro(*k):
    return sum(k)
    
def areatriang(numero1,numero2):
    return (numero1*numero2)/2
    
def areaquadret(numero1,numero2):
    return numero1*numero2
    
def raio(numero):
   return numero/(2*math.pi)

def fracoes():
    while True:
        try:
            fracao1 = Fraction(input('Digite a primeira fração no formato n/n: '))
            fracao2 = Fraction(input('Digite a segunda fração no formato n/n: '))
            operacão = int(input('Escolha a operação a ser realizada: 1-Soma 2-Subtração 3-Divisão 4-Multiplicação '))
            
            if operacão == 1:
                resultado = fracao1 + fracao2
                return resultado
            elif operacão == 2:
                resultado = fracao1 - fracao2
                return resultado
            elif operacão == 3:
                resultado = fracao1 / fracao2
                return resultado
            elif operacão == 4:
                resultado = fracao1 * fracao2
                return resultado
            else:
                print('Opção inválida')
        except ValueError:
            print('Entrada inválida, digite as frações corretamente!')

