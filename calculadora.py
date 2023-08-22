import calcfunctions
import os

while True:

    operacao = input(
    '\n1.Soma'
    '\n2.Multiplicação'
    '\n3.Subtração'
    '\n4.Divisão'
    '\n5.Exponenciação'
    '\n6.Raiz Quadrada'
    '\n7.Cosseno de um ângulo'
    '\n8.Seno de um ângulo'
    '\n9.Logaritmo'
    '\n10.Perímetro'
    '\n11.Área do triângulo'
    '\n12.Área do retângulo/quadrado'
    '\n13.Raio do círculo'
    '\n14.Operação entre frações'
    '\nDigite qual operação deseja executar: '
    )

    if operacao == '1':
        resultado = calcfunctions.somar()
    
    elif operacao == '2':
        resultado = calcfunctions.multiplica()
    
    elif operacao == '3':
        while True:
            try:
                resultado = calcfunctions.subtrai(float(input('Digite o primeiro número: ')), float(input('Digite o segundo número: ')))
                break                                 
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')
              
    elif operacao == '4':
        while True:
            try:
                resultado = calcfunctions.divide(float(input('Digite o primeiro número: ')), float(input('Digite o segundo número: ')))
                break                                 
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')       

    elif operacao == '5':
        while True: 
            try: 
                resultado = calcfunctions.potencia(float(input('Digite o primeiro número: ')), float(input('Digite o segundo número: ')))
                break                                 
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')

    elif operacao == '6':
        while True:
            try:
                resultado = calcfunctions.raizquad(float(input('Digite o número para saber sua raiz quadrada: ')))
                break                                 
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')
            
    elif operacao == '7':
       while True:
            try:
                resultado = calcfunctions.cosseno(float(input('Digite o valor do ângulo: ')))
                break                                 
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')

    elif operacao == '8':
        while True:
            try: 
                resultado = calcfunctions.seno(float(input("Digite o valor do ângulo para saber o seno: ")))
                break                                 
            except ValueError: 
                print('Entrada digitada inválida, digite um número! ')
    
    elif operacao == '9':
         while True:  
            try:
                resultado = calcfunctions.logaritmo(float(input("Digite um numero: ")),float(input("Digite a base: ")))
                break                                
            except ValueError: 
                print('Entrada digitada inválida, digite um número! ')

    elif operacao == '10':
        while True:
            figura = None
            try:
                figura = int(input("Qual figura deseja saber o perímetro? [1] Triângulo [2] Retângulo [3] Quadrado "))
                if 1 <= figura <= 3:
                    break 
                else:
                    print("Entrada digitada inválida, digite um número entre 1 e 3.")
            except ValueError:
                print("Entrada digitada inválida, digite um número!")
                    
        if figura == 1:
            while True:
                try:
                    resultado = calcfunctions.perimetro(float(input("Digite o valor do lado 1: ")), float(input("Digite o valor do lado 2: ")), float(input("Digite o valor do lado 3: ")))
                    break                                 
                except ValueError:
                    print('Entrada digitada inválida, digite um número! ')
                    
        if figura == 2 or figura == 3:
            while True:
                try:
                    resultado = calcfunctions.perimetro(float(input("Digite o valor do lado 1: ")), float(input("Digite o valor do lado 2: ")), float(input("Digite o valor do lado 3: ")), float(input("Digite o valor do lado 4: ")))
                    break
                except ValueError:
                    print('Entrada digitada inválida, digite um número! ')
    
    elif operacao == '11':
        while True:
            try:
                resultado = calcfunctions.areatriang(float(input("Digite o valor da base : ")), float(input("Digite o valor da altura : ")))
                break
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')

    elif operacao == '12':
        while True:
            try:
                resultado = calcfunctions.areaquadret(float(input("Digite o valor da comprimento : ")), float(input("Digite o valor da largura : ")))
                break
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')

    elif operacao == '13':
        while True:
            try:
                resultado = calcfunctions.raio(float(input("Digite o comprimento da circunferência: ")))
                break
            except ValueError:
                print('Entrada digitada inválida, digite um número! ')

    elif operacao == '14':
        resultado = calcfunctions.fracoes()

    else:
        os.system('cls')
        print('Digite um número entre 1 e 14')
        continue 
    
    os.system('cls') 
    print(f'O resultado da operação realizada foi {resultado}')