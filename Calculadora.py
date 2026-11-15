import math

# Historial global
historial = []


def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Debes ingresar un número válido.")


# OPERACIONES

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b


def promedio(numeros):
    if len(numeros) == 0:
        raise ValueError("La lista está vacía.")
    return sum(numeros) / len(numeros)


def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz de un número negativo.")
    return math.sqrt(numero)


# FUNCIÓN CALCULAR

def calcular(operacion, *args):
    resultado = None

    try:

        if operacion == "sumar":
            resultado = sumar(*args)

        elif operacion == "restar":
            resultado = restar(*args)

        elif operacion == "multiplicar":
            resultado = multiplicar(*args)

        elif operacion == "dividir":
            resultado = dividir(*args)

        elif operacion == "promedio":
            resultado = promedio(*args)

        elif operacion == "raiz":
            resultado = raiz_cuadrada(*args)

        else:
            raise ValueError("Operación no válida.")

    except ZeroDivisionError as e:
        print(f"❌ Error: {e}")

    except ValueError as e:
        print(f"❌ Error: {e}")

    else:
        print(f"✅ Resultado: {resultado}")

    finally:

        historial.append({
            "operacion": operacion,
            "argumentos": args,
            "resultado": resultado
        })

    return resultado


# PROPAGACIÓN DE EXCEPCIONES

def funcion_inferior():
    raise ValueError("Error generado intencionalmente.")


def funcion_intermedia():
    print("➡ Entrando a funcion_intermedia")
    funcion_inferior()


def propagar_error():
    print("➡ Entrando a propagar_error")

    try:
        funcion_intermedia()

    except ValueError as e:
        print("✅ Excepción capturada en propagar_error")
        print("Mensaje:", e)


# HISTORIAL

def mostrar_historial():

    if not historial:
        print("No hay operaciones registradas.")
        return

    print("\n===== HISTORIAL =====")

    for i, op in enumerate(historial, start=1):
        print(
            f"{i}. Operación: {op['operacion']} | "
            f"Argumentos: {op['argumentos']} | "
            f"Resultado: {op['resultado']}"
        )


# MENÚ

def menu():

    while True:

        print("\n---------------------------")
        print("     CALCULADORA SEGURA")
        print("---------------------------")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Calcular promedio")
        print("6. Raíz cuadrada")
        print("7. Probar propagación de excepciones")
        print("8. Ver historial")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":

            a = obtener_numero("Primer número: ")
            b = obtener_numero("Segundo número: ")

            calcular("sumar", a, b)

        elif opcion == "2":

            a = obtener_numero("Primer número: ")
            b = obtener_numero("Segundo número: ")

            calcular("restar", a, b)

        elif opcion == "3":

            a = obtener_numero("Primer número: ")
            b = obtener_numero("Segundo número: ")

            calcular("multiplicar", a, b)

        elif opcion == "4":

            a = obtener_numero("Primer número: ")
            b = obtener_numero("Segundo número: ")

            calcular("dividir", a, b)

        elif opcion == "5":

            cantidad = int(
                obtener_numero("¿Cuántos números deseas promediar? ")
            )

            numeros = []

            for i in range(cantidad):
                numeros.append(
                    obtener_numero(f"Número {i+1}: ")
                )

            calcular("promedio", numeros)

        elif opcion == "6":

            numero = obtener_numero(
                "Número para raíz cuadrada: "
            )

            calcular("raiz", numero)

        elif opcion == "7":

            propagar_error()

        elif opcion == "8":

            mostrar_historial()

        elif opcion == "9":

            print("👋 Programa finalizado.")
            break

        else:

            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu()