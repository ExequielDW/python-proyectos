import pandas as pd


def leer_archivo():
    while True:
        print(
            """1-Buscar y leer archivo.
                2-Salir."""
        )
        try:
            menu = int(input("ingrese una opcion").strip())
        except ValueError:
            print("Debes ingresar una opción númerica, gracias")
        if menu == 1:
            try:
                name_arch = (
                    input(
                        "ingrese el nombre del archivo que busca y formato (example.csv): "
                    )
                    .lower()
                    .strip()
                )
                if name_arch:
                    df = pd.read_csv(name_arch)
                    total_categoria = df.groupby("categoria")["monto"].sum()
                    print(
                        f"""Total gastado por categoria:
                    {total_categoria}"""
                    )
                    total_gastado = total_categoria.idxmax()
                    print(
                        f"La categoria que mas gastó es: {total_gastado} : {total_categoria[total_gastado]}"
                    )
                    monto_indv = df.loc[df["monto"].idxmax()]
                    print(f"gasto individual mas alto: {monto_indv}")
                    promedio = df["monto"].mean()
                    print(f"Gasto general promedio: {promedio}$")
                    total_categoria.to_csv("analizador//reporte_gastos.csv")
            except FileNotFoundError:
                print("archivo no encontrado")
        if menu == 2:
            print("Saliendo........")
            break


print(leer_archivo())
