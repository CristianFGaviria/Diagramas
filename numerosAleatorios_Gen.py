import matplotlib.pyplot as plt

print ("GENERADOR DE NUMERO ALEATORIOS")

a = int(input("Ingresa a: ")) #(Multiplo de los primos entre m)
c = int(input("Ingresa c: ")) #(Primo relativo)
m = int(input("Ingresa m: ")) #(Modulo)
y_0 = int(input("Ingresa y_0: ")) #(Semilla)

x_i = 0 # periodo
flag = 0 # bandera de la semilla

for i in range(m):
    if (x_i == 0):
      flag = y_0
    y_0 = (a * y_0 + c) % m #operacion matematica
    x_i = x_i +1
    y_i = x_i / m
    print (f"x_i: [{y_0}]  x_i/m: [{y_i}]")
    #parte que toma las variables y grafica
    plt.scatter([y_0], [x_i])

#graficadora
plt.savefig('diagrama-dispersion.png')
plt.show()