def pedido_txt():
    vacias = {"el", "la", "de", "en", "y", "a", "que", "un", "una", "los", "las"}
    contador = {}
    print(
        """Bienvenid@.....
        a continuación ingresa el archivo que buscas"""
    )
    try:
        name_arch = (
            input("ingresa el nombre del archivo (example.txt): ").strip().lower()
        )
        with open(name_arch, "r") as arch:
            contenido = arch.read()
            palabras = [p.strip(".,;:!?").lower() for p in contenido.split()]
            total_palbras = len(palabras)
            palabras_unicas = set(palabras)
            palabra_mas_larga = max(palabras, key=lambda x: len(x))
            for pa in palabras:
                if pa not in vacias:
                    if pa in contador:
                        contador[pa] += 1
                    else:
                        contador[pa] = 1
            orden_de_diccionario = sorted(
                contador.items(), key=lambda x: x[1], reverse=True
            )
        with open("analizador//reporte_texto.txt", "w") as arch:
            arch.writelines(
                [
                    f"La cantidad de palabras es: {total_palbras}\n",
                    f"Las palabras unicas son: {palabras_unicas}\n",
                    f"la palabra mas larga es: {palabra_mas_larga}\n",
                    f"las palabras mas repetidas son: {orden_de_diccionario[:5]}\n",
                ]
            )
    except FileNotFoundError:
        print("El archivo no fue encontrado, chequea si el nombre es el correcto")


print(pedido_txt())
