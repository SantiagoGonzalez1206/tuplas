productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))

for i,val in enumerate(productos):
    print(f""" {i}. {val} ${precios[i]}""")

eleccion = int(input())

print(f"usuario usted selecciono el producto {productos[eleccion]} con un valor de ${precios[eleccion]}")
plata = int(input("Escriba su cantidad de dinero: $"))
vueltos = plata - precios[eleccion]
falta = precios[eleccion] - plata
if plata >= precios[eleccion]:
    print("Si le alcanza para la gaseosa, sus vueltas son $", vueltos)
else: 
    print("No le alcanza para la gaseosa, le faltan $", falta)