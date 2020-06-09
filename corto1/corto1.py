CARNET = "201602871"                        #Referencia CARNE
LIMITE_INFERIOR = 2                         #Limites para las secuecnia
LIMITE_SUPERIROR = 871                      #Limites para las secuencia
archivo = open('corto1/collats.txt', 'w')   #Abro el archivo

def par_impar(number):          #Funcion para determinar si el numero es impar o impar
    if(number%2):
        return False            #Si es impar retorna falso
    else:       
        return True             #Sies par retorna verdadera

for i in range(LIMITE_INFERIOR,LIMITE_SUPERIROR+1,1):   #i como iterador de numeos a los que le calculo la sucesion
    n=i                      #igualo n al numero i, siendo n mi iterador para la sucecion Collats de i
    Collatz = []             #Lista vacia para nueva secuencia Collatz
    while(n>1):              #Condicional 1 ultimo numero al cual calular COllatz
        if(par_impar(n)):       #Si es par
            Collatz.append(n)   #Agrego el numero a la secuencia
            n = n//2            #Determino el nuevo numero n
        else:
            Collatz.append(n)   #Agrego el numero a la secuencia
            n = 3*n + 1         #DEtermino el nuevo numero n
    Collatz.append(1)           #Agrego el 1, al final de la lista        
    archivo.write(str(Collatz)+"\n")  #Agrego la lista de la secuencia del numero i


archivo.close()                 #Cierro el archivo