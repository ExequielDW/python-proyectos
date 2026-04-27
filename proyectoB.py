import funcionesB

# en el archivo principal
from funcionesB import registro

funcionesB.carga_de_contactos()
while True:
    print(
        """1. Agregar contacto
2. Buscar contacto
3. Eliminar contacto
4. Ver todos los contactos
5. Guardar contactos
6. Salir"""
    )
    try:
        menu = int(input("ingrese una opcion: ").strip())
    except ValueError:
        print("Debe ingresar una opción númerica")
    if menu == 1:
        agregando = funcionesB.agregar()
        print(agregando)
    if menu == 2:
        buscando = funcionesB.buscar()
        print(buscando)
    if menu == 3:
        eliminado = funcionesB.eliminar()
        print(eliminado)
    if menu == 4:
        ver = funcionesB.ver_contacto()
        print(ver)
    if menu == 5:
        load = funcionesB.guardar_contactos()
        print(load)
    if menu == 6:
        print("Saliendo......")
        break
