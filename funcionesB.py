registro = {}


def carga_de_contactos():
    try:
        with open("analizador//contactos.txt", "r") as arch:
            lineas = arch.readlines()
            for linea in lineas:
                nombre, email, telefono = linea.strip().split(",")
                registro[nombre] = {"email": email, "telefono": telefono}
    except FileNotFoundError:
        print("archivo vacio")


def agregar():
    name_contacto = input("ingrese nombre del contacto").lower().strip()
    correo_contacto = input("ingrese un correo (example@gmail.com)").lower().strip()
    if "@" in correo_contacto:
        correo = correo_contacto
    else:
        print("Formato de mail invalido")
    try:
        tel_contacto = int(input("ingrese el número a almacenar: ").strip())
    except ValueError:
        print("Debe ingresar un valor númerico...")
    if not name_contacto in registro:
        registro[name_contacto] = {"telefono": tel_contacto, "email": correo}
        print(
            f"Registro exitoso, se ha guardado a {name_contacto},tel:{tel_contacto},email:{correo}"
        )
    else:
        print("El contacto ya se encuentra registrado")


def buscar():
    busqueda = input("ingrese el nombre del contacto que busca: ").strip().lower()
    busqeda_co = input("ingrese su correo para verificar: ").strip().lower()
    encontrado = False
    for clave, valor in registro.items():
        if busqueda == clave and busqeda_co == valor["email"]:
            encontrado = True
            break
    if encontrado:
        print(f"Se encuentra en el registro {registro[busqueda]['telefono']}")
    else:
        print("Contacto no registrado")


def eliminar():
    eliminar = (
        input("ingrese el nombre del contacto que desea eliminar: ").strip().lower()
    )
    eliminar_co = (
        input("ingrese el correo para verificar el contacto a eliminar").strip().lower()
    )
    encontrado = False
    for clave, valor in registro.items():
        if eliminar in clave and eliminar_co == valor["email"]:
            encontrado = True
            clave_eliminar = clave
            break
    if encontrado:
        registro.pop(clave_eliminar)
        print("Contacto eliminado correctamente...")
    else:
        print("El contacto no se encuentra en el registro")


def ver_contacto():
    for clave, valor in registro.items():
        print(f"{clave}, {valor['telefono']}, {valor['email']}")


def guardar_contactos():
    if registro:
        with open("analizador//contactos.txt", "w") as arch:
            for clave, valor in registro.items():
                arch.write(f"{clave},{valor['email']},{valor.get('telefono')}\n")
    else:
        print("El registro esta vacio")
