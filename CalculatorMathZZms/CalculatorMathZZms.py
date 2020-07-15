print("BIENVENIDO A 'CALTOMH'");
print("----------------------------------------------------");
input();
continuar = True
while continuar:
 print("Elige una de las siguientes opciones:");
 print("1" , "---->" , "Suma"); 
 print("2", "---->", "Resta");
 print("3", "---->", "Multiplicación");
 print("4", "---->", "División");
 print("5", "---->", "Potencia");
 print("6", "---->", "Radicación");
 print("Oprimir cualquier otra tecla para salir")
 onstd = input("¿Qué operación desea realizar? ") #onstd será la variable con la cual trabajaremos, el usuario colocará números del 1 al 6 y ellegirá su opción, en caso de escoger un número distinto al rango y dar clic a 'Enter', el programa se cerrará automáticamente
 if onstd=="1":
     s1=float(input("Primer número: "))
     s2=float(input("Segundo número: "))
     res = print(s1 + s2);
 elif onstd=="2":
     s1=float(input("Primer número: "))
     s2=float(input("Segundo número: "))
     res = print(s1 - s2);
 elif onstd=="3":
     s1=float(input("Primer número: "))
     s2=float(input("Segundo número: "))
     res = print(s1 * s2);
 elif onstd=="4":
     s1=float(input("Primer número: "))
     s2=float(input("Segundo número: "))
     if s2==0.0:
         print("'Ha habido un error'");
     else:
         print(s1 / s2);     
 elif onstd=="5":
     s1=float(input("Primer número: ")) #Este número será la base
     s2=float(input("Segundo número: ")) #Este número será el exponente
     res = print(s1**s2)
 elif onstd=="6":
     s1=float(input("Primer número: ")) #Este número será la base
     s2=float(input("Segundo número: ")) #Este número será el radical, el cual sera 1 dividido entre este número
     if s2==0:
         print("'Ha habido un error'")
     else:
         print(s1**(1/s2))
 else:
     print("Has apagado la máquina.")
     continuar = False


input()