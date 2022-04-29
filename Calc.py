
import random as rd
import os
import time
import ast






cls = os.system("cls")


gscore={}



def operation(op,num1,gscore):
    reg=[]
    i=0
    sc=[]
    cont = 0
    hits=0
    fails=0
    _porc = 0
    if op == 1:

        for j in num1:
            os.system("cls")
            for i in range(1,11):
                sol=num1[cont] * i
                
                try:
                    inicio=time.time()
                    resp = input(f"{num1[cont]} x {i} = ")
                    if int(resp) == sol:
                        fin = time.time()

                        print(f"{num1[cont]} x {i} = {resp}  OK")
                        hits = hits + 1
                        reg.append(f"{num1[cont]} x {i} = {resp}  OK {round(fin-inicio)} Seg")


                    else:
                        fin = time.time()

                        print(f'{num1[cont]} x {i} = {resp} (es {sol})')
                        fails= fails +1
                        reg.append(f'{num1[cont]} x {i} = {resp} (es {sol}) {round(fin-inicio)} Seg')
                        
                except:
                    fin = time.time()

                    resp=0
                    print(f'{num1[cont]} x {i} = {resp} ( es {sol})')
                    fails= fails +1
                    reg.append(f'{num1[cont]} x {i} = {resp} (es {sol}) {round(fin-inicio)} Seg')
                os.system('cls')
                i=0
                for j in reg:
                    print(reg[i])
                    i=i+1
            total = 10
            _porc = (hits/total)*100
            sc.append(_porc)
            gscore=Score(gscore,num1[cont],sc[cont])
            cont=cont+1
            _hits = hits
            hits = 0
            os.system('cls')
            reg=[]
    else:
        
        for j in num1:

            os.system("cls")
            for i in range(1,11):
                mul = rd.randint(1,10)
                sol = num1[cont-1] * mul
                
                try:
                    inicio=time.time()
                    
                    resp = input(f"{num1[cont-1]} x {mul} = ")
                    if int(resp) == sol:
                        fin = time.time()

                        print("OK\n")
                        hits = hits +1
                        reg.append(f'{num1[cont]} x {mul} = {sol} OK {round(fin-inicio)} Seg')
                        
                    else:
                        fin = time.time()

                        print(f"No, es{sol}\n")
                        fails= fails +1
                        reg.append(f'{num1[cont-1]} x {mul} = {resp} (es {sol}) {round(fin-inicio)} Seg')
                        
                        
                except:
                        fin = time.time()
                        resp=0
                        reg.append(f'{num1[cont-1]} x {mul} = {resp} (es {sol}) {round(fin-inicio)} Seg')

                        print(f"No, es{sol}\n")
                        fails= fails +1
                i=0
                os.system('cls')
                for j in reg:
                    print(reg[i])
                    i=i+1
                
            reg=[]
            _hits=hits
            hits=0
            total = 10
            _porc = (hits/total)*100
            sc.append(_porc)
            gscore=Score(gscore,num1[cont],sc[cont])
            cont = cont + 1
            os.system('cls')


    i=0

    # for j in range(len(num1)):
    #     i=i+1
    #     print(j)

    print(f"\nHas tenido {_hits} aciertos y {fails} fallos.\n")






def ChooseNumber():
    os.system('cls')
    num=0
    
    while True:
        try:
            os.system('cls')
            num=[]
            cont=0
            cadena=input("Tablas a practicar ")
            cadena = cadena.split(" ")


            for i in cadena:
                cont
                hola = cadena[cont]
                num.append(int(hola))
                
                cont=cont + 1
                
            return num
        except:
            os.system('cls')











def menu():

    ch=0
    while ch != 1 and ch != 2:
        os.system('cls')
        print("********************************************")
        print("*   Seleccione el modo que desee repasar   *")
        print("********************************************")
        print("*     1. Tabla/s de multiplicar            *")
        print("*     2. Multiplicacion aleatoria          *")
        print("*     3. Evaluacion                        *")
        print("*     4. Resetear puntuacion               *")
        print("*     5. Salir                             *")
        print("********************************************")
        try:
            ch = int(input("Seleccione una opcion "))
            if  ch != 1 and ch != 2 and ch !=3 and ch !=4 and ch != 5:
                cls
                print("Introduce un numero valido ")
                input("Pulse una tecla para continuar")
            else:
                return ch
        except:
            return 0






def PlayAgain():
    playAgain = True
    playAgain=input("¿Quieres volver a jugar? y/n  \n")
    if playAgain.upper()=='Y' or playAgain.upper() == 'YES' or playAgain.upper() == 'SI' or playAgain.upper()=='S' or playAgain.upper()=='SÍ' or playAgain.upper() == 'YE':
        return playAgain
    else:
        playAgain = False
        return playAgain

def Score(_score,_tabla, _porc):
        os.system('cls')
        _porc = "{0:.0f}%".format(_porc)

        _score[f"Tabla {_tabla}"] = _porc
        os.system('cls')
        print(f"Puntuacion registrada con exito")
        input()
        return _score


def ResetScore(_score):
    for i in range(1,11):
        _score[f"Tabla {i}"] = ''
        
    return _score

def SaveScore(_score):
    tf = open("Score.txt","w")
    tf.write(str(_score))
    tf.close()


def ReadScore(_score):
    tf = open("Score.txt","r")
    _score=tf.read()
    tf.close()
    return _score



def Eval(_score,_tabla):
    os.system('cls')
    for i in range(len(_tabla)):

        value = _score.get(f'Tabla {_tabla[i]}')
        
        try:
            value=value.replace("%","")
            value = int(value)
            if value<= 20:
                print(" ******************************")

                print(f"Tabla {_tabla[i]}")
                print(_score.get(f'Tabla {_tabla[i]}'))
                print("Muy mal")
                print(" ******************************")

            elif value <=40:
                print(" ******************************")

                print(f"Tabla {_tabla[i]}")
                print(_score.get(f'Tabla {_tabla[i]}'))
                print("Hay que mejorar")
                print(" ******************************")

            elif value >= 50 and value <=80:
                print(" ******************************")

                print(f"Tabla {_tabla[i]}")
                print(f"Puntuacion Tabla {_tabla[i]} = {_score.get(f'Tabla {_tabla}')}")
                print("Esta bien pero podrias mejorar")
                print(" ******************************")

            elif value ==100:
                print(" ******************************")

                print(f"Tabla {_tabla[i]}")
                print(_score.get(f'Tabla {_tabla[i]}'))
                print("Te la sabes perfecta")
                print(" ******************************")

            elif value== 90:
                print(" ******************************")

                print(f"Tabla {_tabla[i]}")
                print(_score.get(f'Tabla {_tabla[i]}'))
                print("Solo has fallado 1")
                print(" ******************************")

        except:
            print(" ******************************")
            print(f"*      Tabla {_tabla[i]}      *")
            print("*                              *")
            print("Todavia no has hecho esta tabla*")
            print("*                              *")
            print("********************************")
        
        input()
        





#Comienzo Programa
playAgain = False
cont=True
try:
    gscore=ReadScore(gscore)
    gscore=ast.literal_eval(gscore)
except:
    ResetScore(gscore)






while cont:

    if playAgain==False:
        op = menu()
    if op==3:
        num=[]
        tabla=input("¿Que puntuacion quieres ver? ")
        tabla = tabla.split(" ")
        for i in range(len(tabla)):
            
            hola = tabla[i]
            num.append(int(hola))
            
            
        Eval(gscore,num)

    elif op==1 or op==2:
        
        nm = ChooseNumber()
        operation(op,nm,gscore)
        playAgain=PlayAgain()
    elif op==4:
        ResetScore(gscore)
    elif op == 5:
        cont=False
        SaveScore(gscore)
        os.system('cls')





#Puntuacion, mostrar todas las tablas
#No borrar la pantalla een las multiplicaciones

#En los randoms preguntar por los que falla




