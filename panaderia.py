eleccionPrincipal= input("Elija el tipo de producto que desea: bebidas, panaderia o postres: ")
if eleccionPrincipal == "bebidas":
    productos_bebidas = tuple((
    "Milo frio", 
    "Milo caliente", 
    "Cafe", 
    "Tinto", 
    "Jugo natural", 
    "Malteada", 
    "Naranjada", 
    "Limonada", 
    "Botella de agua",
    "Gaseosa personal",
    "Promocion botella de agua + malteada",
    "Promocion naranjada + cafe"
    ))
    precios_bebidas = tuple((
    4000, 
    4000, 
    2500, 
    2000, 
    5000, 
    8000, 
    4000, 
    4000,
    2000, 
    3000, 
    9000,    
    5500,
    ))

    for i,val in enumerate(productos_bebidas):
        print(f""" {i}. {val} ${precios_bebidas[i]}""")
    
    eleccion = int(input())
    numProductos=int(input("Cuantos quiere? "))
    print(f"usuario usted selecciono el producto {productos_bebidas[eleccion]} con un valor de ${precios_bebidas[eleccion]*numProductos}")
    plata = int(input("Escriba su cantidad de dinero: $"))
    vueltos = plata - (precios_bebidas[eleccion]*numProductos)
    falta = (precios_bebidas[eleccion]*numProductos) - plata
    if plata >= precios_bebidas[eleccion]*numProductos:
        print("Si le alcanza para la bebida, sus vueltas son $", vueltos)
    else: 
        print("No le alcanza para la bebida, le faltan $", falta)

elif eleccionPrincipal == "panaderia":
    productos_panaderia = tuple((
    "Empanadas (ranchera, pollo queso o carne)", 
    "Arepas rellenas (pollo, carne o mixta)", 
    "Pastel de pollo", 
    "Arepa de huevo", 
    "Croissant", 
    "Buñuelo unidad", 
    "Palitos de queso", 
    "Baguette", 
    "Pan por unidad",
    "Pan grande",
    "Promocion 11 panes",
    "Promocion 7 buñuelos"
    ))
    precios_panaderia = tuple((
    3000, 
    3500, 
    4000, 
    3600, 
    4200, 
    800, 
    3000, 
    3700,
    500, 
    2000, 
    5000,    
    5000,
    ))

    for i,val in enumerate(productos_panaderia):
        print(f""" {i}. {val} ${precios_panaderia[i]}""")
    
    eleccion = int(input())
    numProductos=int(input("Cuantos quiere? "))
    print(f"usuario usted selecciono el producto {productos_panaderia[eleccion]} con un valor de ${precios_panaderia[eleccion]*numProductos}")
    plata = int(input("Escriba su cantidad de dinero: $"))
    vueltos = plata - (precios_panaderia[eleccion]*numProductos)
    falta = (precios_panaderia[eleccion]*numProductos) - plata
    if plata >= precios_panaderia[eleccion]*numProductos:
        print("Si le alcanza para el producto, sus vueltas son $", vueltos)
    else: 
        print("No le alcanza para el producto, le faltan $", falta)  

elif eleccionPrincipal == "postres":
    productos_postres = tuple((
    "Tiramisú", 
    "Galleta de chocolate", 
    "Dona", 
    "Postre de maracuya", 
    "Cheesecake", 
    "Torta de chocolate", 
    "Torta de zanahoria", 
    "Gelatina", 
    "Brownie",
    "Torta tres leches",
    "Promocion dona + cheesecake ",
    "Promocion galleta de chocolate + gelatina"
    ))
    precios_postres = tuple((
    4000, 
    2500, 
    3000, 
    3800, 
    4200, 
    4000, 
    3500, 
    2800,
    5000, 
    4100, 
    7000,    
    5000,
    ))
   
    for i,val in enumerate(productos_postres):
        print(f""" {i}. {val} ${precios_postres[i]}""")
    
    eleccion = int(input())
    numProductos=int(input("Cuantos quiere? "))
    print(f"usuario usted selecciono {productos_postres[eleccion]} con un valor de {precios_postres[eleccion]*numProductos}")
    plata = int(input("Escriba su cantidad de dinero: $"))
    vueltos = plata - (precios_postres[eleccion]*numProductos)
    falta = (precios_postres[eleccion]*numProductos) - plata
    if plata >= precios_postres[eleccion]*numProductos:
        print("Si le alcanza para el producto, sus vueltas son $", vueltos)
    else: 
        print("No le alcanza para el producto, le faltan $", falta)  

