def analizar_texto(frase: str) -> tuple[int, int]:
    """
    Calcular el número total de vocales y palabras que contiene
    :param: frase
    """

    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    
    contador_palabras = len(frase.split())

    contador_vocales = 0

    for caracter in frase:
        if caracter in vocales:
            contador_vocales += 1

    return contador_vocales, contador_palabras


def main():

    frase_entrada = input("Introduce una frase: ")
    resultado = analizar_texto(frase_entrada)
    print("La frase tiene", resultado[0], "vocales y", resultado[1], "palabras en total")

if __name__ == "__main__":
    main()