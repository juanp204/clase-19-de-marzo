#ejercicio 1
def uno():
    for x in range(10):
        print(x)
#ejercicio 2
def dos():
    for x in range(100,200,):
       print(x)
#ejercicio 3
def tres():
    for x in range(5,20,3):
        print(x)
#ejercico 4
def cuatro():
    n = int(input())
    for x in range((n-1),(n*2)):
        if (n+1)>=x:
            print(x)
        if (x == ((n*2)-1)):
            print(x)
#ejercicio 5
def cinco():
    frase = input("ingrese frase ")
    for v in "aeiou":
        if v in frase:
            print(v)
#ejercicio 7
def siete():
    sumar = 0
    for x in range(1,101):
        sumar += x
        print(sumar)
#ejercicio 8
def ocho():
    año1 = int(input("ingrese primer año "))
    año2 = int(input("ingrese segundo año "))
    for x in range(año1,(año2+1)):
        if (x%4 == 0 & x%400 == 0) or x%10 == 0:
            print(x)
#ejercicio 9
def nueve():
    num = int(input("numero = "))
    facto = 1
    for x in range(1,num+1):
        facto = facto*x
    print(num,"factorial es",facto)
#ejeccio 10
def diez():
    anterior = 1
    num = 0
    for x in range(10):
        print(num)
        num = anterior + num
        anterior = num
print("0 para cerrar programa")
while True:
    try:
        ejercicio = int(input("numero del ejercicio "))
        if ejercicio == 0:
            break
    except ValueError:
        print("solo numeros de los ejercicios")
        continue
    if ejercicio>10 or ejercicio<0 or ejercicio == 6:
        print("solo hay ejercicos del 1 al 5 y del 7 al 10")
        continue
    if ejercicio == 1:
        uno()
    if ejercicio == 2:
        dos()
    if ejercicio == 3:
        tres()
    if ejercicio == 4:
        cuatro()
    if ejercicio == 5:
        cinco()
    if ejercicio == 7:
        siete()
    if ejercicio == 8:
        ocho()
    if ejercicio == 9:
        nueve()
    if ejercicio == 10:
        diez()
