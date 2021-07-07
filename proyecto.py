region=input("ingrese una region:")
print("el grafico de los pacientes uci no acumulativos de la region",region,"es: ")
import  matplotlib.pyplot as plt
x=[1,1,1,2,2,3]
plt.hist(x)
plt.show()
menu="0"
while menu != "5":
    fila=0
    flag1= False
    flag2= False
    flag3= False

