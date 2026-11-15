# Calculadora# 
Calculadora Segura con Manejo de Excepciones

## Descripción

Este proyecto consiste en una calculadora desarrollada en Python cuyo objetivo es demostrar el uso correcto del manejo de excepciones. La aplicación permite realizar operaciones matemáticas comunes y responder de forma controlada ante errores de entrada o de ejecución, evitando que el programa termine inesperadamente.

Entre los conceptos utilizados se encuentran:

- Manejo de excepciones con try, except, else y finally.
- Lanzamiento de excepciones mediante raise.
- Propagación de excepciones.
- Validación de datos introducidos por el usuario.
- Registro de operaciones en un historial.

---

## Descarga del proyecto

1. Ingresa al repositorio de GitHub.
2. Haz clic en el botón **Code**.
3. Selecciona **Download ZIP**.
4. Extrae el contenido del archivo ZIP en tu computadora.
5. Abre la carpeta del proyecto en Visual Studio Code o en tu editor favorito.

---

## Estructura del proyecto

calculadora\_segura/

│

├── calculadora\_segura.py

└── README.md

- **calculadora\_segura.py**: contiene toda la lógica de la calculadora, el manejo de excepciones, el historial y el menú interactivo.
- **README.md**: documentación del proyecto.

---

## Requisitos

- Python 3.x instalado en el sistema.

Puedes verificar la instalación ejecutando:

python \-\-version

---

## Cómo ejecutar el programa

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el programa con el siguiente comando:

python calculadora\_segura.py

1. Aparecerá el menú principal.

---

## Opciones disponibles

La calculadora permite realizar las siguientes acciones:

1. Sumar dos números.
2. Restar dos números.
3. Multiplicar dos números.
4. Dividir dos números.
5. Calcular el promedio de una lista de números.
6. Calcular la raíz cuadrada de un número.
7. Probar la propagación de excepciones.
8. Consultar el historial de operaciones.
9. Salir del programa.

---

## Manejo de errores

El programa incluye validaciones para evitar errores comunes:

- Entradas no numéricas (ValueError).
- División entre cero (ZeroDivisionError).
- Promedio de listas vacías (ValueError).
- Raíz cuadrada de números negativos (ValueError).

En todos los casos se muestra un mensaje amigable al usuario sin que el programa se cierre.

---

## Historial de operaciones

Cada operación realizada se registra automáticamente en el historial, incluyendo:

- Nombre de la operación.
- Argumentos utilizados.
- Resultado obtenido o fallo de la operación.

El historial puede consultarse desde la opción correspondiente del menú principal.


