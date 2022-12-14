#Simulação da lei dos grandes numeros para uniforme(0,1) convergindo para ln(2)

from cmath import e
import numpy as np
import math as mt

while True:
    N = input("Digite o numero de interações, ou digite uma string para sair: ")
    try:
        N = int(N)
    except:#quebra de loop quando houve erro na transformação para inteiro
        print("String inserida")
        break

    sum = 0
    unif = np.random.uniform(size=N)#por padrão a uniforme já é gerada no intervalo (0,1)    
    for i in unif:
        sum += 1/(1+i)
    
    print("ln(2)=",mt.log(2,e))
    print("Soma = ",(1/len(unif)*sum))        
