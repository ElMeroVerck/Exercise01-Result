# Inicializar variables
baseDeDatos = []


variableContador = 0
variableDeCostos = 0
VariablePiquetera = 1
# Saludo al usiario e ingreso de parametros para el bucle
print("Bienvenido, amo todo poderoso.")
DatosAIngresar = input(
    "Su majestard, ingrese cuantas los datos de cuantas personas desea agregar a su base de datos: "
)


# Ingreso de los datos que van adentro de la lista usando un bucle
while variableContador < int(DatosAIngresar):
    print("Ingrese los datos del " + str(VariablePiquetera) + " Registro")
    cliente = input("Nombre del cliente: ")
    productos = input("Producto vendido: ")
    costo = float(input("costo ($0.00): "))
    registro = dict(cliente=cliente, producto=productos, costo=costo)
    baseDeDatos.append(registro)
    variableDeCostos = float(variableDeCostos) + costo
    variableContador = variableContador + 1
    VariablePiquetera = VariablePiquetera + 1
print(
    "El total de los costos para los datos ingresados es de: $" + str(variableDeCostos)
)
