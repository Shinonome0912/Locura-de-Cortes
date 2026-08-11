# 🐍 PYTHON WEIRDNESS 001 — "¿QUÉ ACABO DE EJECUTAR?"
#
# Este archivo contiene comportamientos de Python que, a primera
# vista, parecen absurdos, pero tienen una explicación.
# La idea del repositorio es experimentar con estas situaciones
# y entender QUÉ está pasando realmente.


# 🤨 1. ¿PUEDO GUARDAR EL RESULTADO DE print()?

hola = print("Hola!")

# Sí, podemos guardar el resultado de una función en una variable.

# PERO...

# print() no devuelve el texto que imprimió.
# Su valor de retorno es None.

# Por lo tanto:
#     hola → None

# La función hizo algo (imprimir "Hola!"), pero no produjo un
# valor para que nosotros lo guardáramos.

print(hola)

# Resultado:

# Hola!
# None

# La primera línea pertenece al print() original.
# La segunda pertenece al print(hola).

# En otras palabras:
#     hola = print("Hola!")
#     print(hola)

# es conceptualmente:
#     hola = None
#     print(hola)


# 🤯 2. ¿Y SI GUARDO LA FUNCIÓN EN VEZ DE EJECUTARLA?

x = print

# Aquí NO ejecutamos print().
# No hay paréntesis.
#     print

# Por lo tanto, x ahora apunta al objeto función print.
# Podemos usar x como si fuera print:
x("Esto salió usando la variable x")
# Ahora sí estamos ejecutando la función.
# Pero si ponemos paréntesis...

x = print()

# ¡BOOM! 💀

# Ahora sí ejecutamos print().
# Como no le pasamos ningún argumento, simplemente hace su trabajo
# y devuelve None.

# Por lo tanto:
#     x → None


#  3. PRINT DENTRO DE PRINT DENTRO DE PRINT

print(print(print("Hola")))

# Esto parece una invocación satánica de print(), pero Python
# simplemente evalúa las funciones desde dentro hacia afuera.

# 1. print("Hola")
#       ↓
#    imprime "Hola"
#       ↓
#    devuelve None

# 2. print(None)
#       ↓
#    imprime "None"
#       ↓
#    devuelve None

# 3. print(None)
#       ↓
#    imprime "None"

# Resultado:

# Hola
# None
# None

# print() imprime algo, pero su retorno sigue siendo None.


# 4. UNA FUNCIÓN SIN return TAMBIÉN "DEVUELVE" ALGO

def sumar(a, b):
    resultado = a + b

# ¿Dónde está el return?

# No hay ninguno.

# Aun así, podemos hacer:

x = sumar(5, 3)

print(x)

# Resultado:

# None

# Una función que termina sin ejecutar un return explícito devuelve None.

# OJO:

# La función SÍ calculó:
#     resultado = 8

# pero ese valor nunca salió de la función.
# El problema no es que sumar() no haya calculado 8.
# El problema es que nunca hicimos:

#     return resultado


# 🔄 5. INTERCAMBIAR VARIABLES SIN CREAR UNA VARIABLE TEMPORAL

a, b, c = 10, 20, 30

print(a, b)

a, b = b, a

print(a, b)

# Resultado:

# 10 20
# 20 10

# Python permite asignar varios valores simultáneamente.

# En:
#     a, b = b, a

# Python obtiene los valores de la derecha y los asigna a las
# variables de la izquierda.

# Así podemos intercambiar dos variables sin hacer:
#     temporal = a
#     a = b
#     b = temporal

# No es realmente "magia", pero cuando lo descubres por primeravez parece un ejercicio que Juan Díaz no explicó. 😂


# 👻 6. ¿CÓMO PUEDE UNA LISTA VACÍA SER "FALSE"?

print(bool([]))
print(bool([1]))

# Resultado:

# False
# True

# Una lista vacía se considera falsy.
# Una lista que contiene elementos se considera truthy.

# Esto significa que podemos hacer:

if []:
    print("La lista tiene valor verdadero")
else:
    print("La lista está vacía")

# Python considera falsy, entre otros:
#     None
#     False
#     0
#     ""
#     []
#     {}

# Mientras que objetos con contenido normalmente son truthy.

# 🤯 7. PERO... [] == False ES FALSE

print(bool([]))

print([] == False)

# Resultado:

# False
# False

# ¿¿¿CÓMO QUE FALSE Y FALSE NO SON LO MISMO??? 😭
# Porque estamos haciendo DOS cosas diferentes.

# ------------------------------------------------------------
# bool([])
# ------------------------------------------------------------

# Pregunta:
#     "¿La lista vacía se considera verdadera o falsa en un contexto booleano?"
# Respuesta:
#     False


# ------------------------------------------------------------
# [] == False
# ------------------------------------------------------------

# Pregunta:
#     "¿La lista vacía es igual al objeto False?"
# Respuesta:
#     False


# Por lo tanto:

#     bool([])    → False
#     [] == False → False

# Ser FALSY no significa ser IGUAL a False.

# 🧠 RESUMEN

# False  → un valor booleano.

# None   → representa ausencia de valor.

# Falsy  → un objeto que Python interpreta como falso cuando
#          necesita evaluar su valor de verdad.

# Truthy → un objeto que Python interpreta como verdadero.

# Y sí:

#     bool([]) == False

# pero:

#     [] == False da False.

# Python: "No son la misma pregunta, bro." 🗿