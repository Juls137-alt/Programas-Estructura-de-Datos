
# ============================================
# CONVERSION DE EXPRESIONES MATEMATICAS
# INORDEN, PREORDEN Y POSTORDEN
# UTILIZANDO PILAS
# ============================================

def es_operador(caracter):
    return caracter in "+-*/^"


def prioridad(operador):
    prioridades = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }
    return prioridades.get(operador, 0)


# Separar numeros, operadores y parentesis
def separar_expresion(expresion):
    tokens = []
    numero = ""

    for caracter in expresion:

        if caracter.isdigit() or caracter == ".":
            numero += caracter

        else:
            if numero:
                tokens.append(numero)
                numero = ""

            if caracter in "+-*/^()":
                tokens.append(caracter)

    if numero:
        tokens.append(numero)

    return tokens


# Convertir INORDEN a POSTORDEN usando una pila
def convertir_postorden(tokens):

    pila = []
    salida = []

    for token in tokens:

        if token.replace(".", "", 1).isdigit():
            salida.append(token)

        elif token == "(":
            pila.append(token)

        elif token == ")":

            while pila and pila[-1] != "(":
                salida.append(pila.pop())

            if pila:
                pila.pop()

        elif es_operador(token):

            while (pila and pila[-1] != "(" and
                   (prioridad(pila[-1]) > prioridad(token) or
                    (prioridad(pila[-1]) == prioridad(token)
                     and token != "^"))):

                salida.append(pila.pop())

            pila.append(token)

    while pila:
        salida.append(pila.pop())

    return salida


# Convertir POSTORDEN a PREORDEN utilizando pilas
def convertir_preorden(tokens_postorden):

    pila = []

    for token in tokens_postorden:

        if not es_operador(token):
            pila.append(token)

        else:
            operando_derecho = pila.pop()
            operando_izquierdo = pila.pop()

            nueva_expresion = [
                token,
                operando_izquierdo,
                operando_derecho
            ]

            pila.append(nueva_expresion)

    return pila[0]


# Convertir una lista de expresion a texto
def mostrar_expresion(expresion):

    if isinstance(expresion, list):
        return "(" + " ".join(
            mostrar_expresion(x) for x in expresion
        ) + ")"

    return expresion


# Evaluar POSTORDEN utilizando una pila
def evaluar_postorden(tokens):

    pila = []

    for token in tokens:

        if not es_operador(token):
            pila.append(float(token))

        else:
            derecho = pila.pop()
            izquierdo = pila.pop()

            if token == "+":
                resultado = izquierdo + derecho

            elif token == "-":
                resultado = izquierdo - derecho

            elif token == "*":
                resultado = izquierdo * derecho

            elif token == "/":
                resultado = izquierdo / derecho

            elif token == "^":
                resultado = izquierdo ** derecho

            pila.append(resultado)

    return pila[0]


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

print("====================================")
print(" CONVERSION DE EXPRESIONES MATEMATICAS")
print("====================================")

expresion = input("\nIngresa una operacion matematica: ")

try:

    # Obtener los elementos de la expresion
    tokens = separar_expresion(expresion)

    # Convertir a POSTORDEN
    postorden = convertir_postorden(tokens)

    # Convertir a PREORDEN
    preorden = convertir_preorden(postorden)

    # Evaluar la operacion
    resultado = evaluar_postorden(postorden)

    # Mostrar resultados
    print("\n====================================")
    print("          RESULTADOS")
    print("====================================")

    print("INORDEN: ", expresion)

    print("PREORDEN:", mostrar_expresion(preorden))

    print("POSTORDEN:", " ".join(postorden))

    print("RESULTADO:", resultado)

    print("\n====================================")
    print("       PROCESO TERMINADO")
    print("====================================")

except (ValueError, IndexError, ZeroDivisionError):
    print("\nError: expresion matematica invalida.")
