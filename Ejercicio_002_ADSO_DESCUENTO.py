#Ejercicio algoritmo descuento del valor de compra
valorCompra= int(input("Introduzca el valor de su compra: "))
valorReferencia= 60000
descuento1= 0.1
descuento2= 0.05
descuento3= 0.07

if valorCompra>valorReferencia:
    print("El valor con el descuento del 10% es", valorCompra-(valorCompra*descuento1))
elif valorCompra==0:
    print("No tendrá descuento ya que el valor de la compra es 0")
elif valorCompra<valorReferencia:
    print("El valor con el descuento del 5% es", valorCompra-(valorCompra*descuento2))
elif valorCompra==valorReferencia:
    print("El valor con el descuento del 7% es", valorCompra-(valorCompra*descuento3))