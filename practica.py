def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    nombre_archivo = input("Por favor, introduce el nombre del archivo que deseas leer: ")
    contenido = leer_archivo(nombre_archivo)
    if contenido:
        print("Contenido del archivo:")
        print(contenido)

if __name__ == "__main__":
    main()
