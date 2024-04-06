#Ejercicio imprimir valor con descuento
valorCompra= int(input("Introduzca el valor de la compra: "))
descuento=0.05
valorTotal= valorCompra-(valorCompra*descuento)
print("El valor de la compra es:", valorCompra)
print(f"El valor del descuento es: {valorCompra*descuento}")
print("El valor total es:", valorTotal)