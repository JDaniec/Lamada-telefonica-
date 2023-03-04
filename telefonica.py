print("--------------------------------------------")
print("--------Coste de llamada telefonica---------")
print("---------------------------------------------")


# input

dl = int(input("ingrese la duración de la llamda"))

# processing
if dl <= 3:
    cl = 300

else: 
     m = dl - 3
     cl = 300 + (50*m)

#output
print("-----------------------------")
print("El coste de la llamda es" + str(cl) + "$")