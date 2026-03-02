from array import *
import re 
import time

FIRST_GROUPS = [1,4,6,9,12,14]
SECOND_GROUPS = [1,4,6,9,15,17]
THIRD_GROUPS = [1,4,6,18,20,23,25]
FOURTH_GROUPS = [1,4,6,18,20,26,28]
FIFTH_GROUPS = [1,30,32,35,38,40]
SIXTH_GROUPS = [1,30,32,35,41,43]
SEVENTH_GROUPS = [1,30,32,44,46,49,51]
EIGHTH_GROUPS = [1,30,32,44,46,52,54]

CONVINATIONS = [
    FIRST_GROUPS,
    SECOND_GROUPS,
    THIRD_GROUPS,
    FOURTH_GROUPS,
    FIFTH_GROUPS,
    SIXTH_GROUPS,
    SEVENTH_GROUPS,
    EIGHTH_GROUPS
]

matchs_counter = 0

# expresion regular que encuentra las invariantes
pattern = r"(T0)(((T1)(.*?)(T3)(.*?))((T5)(.*?)((T9)(.*?)(T15)|(T10)(.*?)(T16))|(T13)(.*?)(T7)(.*?)((T9)(.*?)(T15)|(T10)(.*?)(T16)))|((T2)(.*?)(T4)(.*?))((T6)(.*?)((T11)(.*?)(T15)|(T12)(.*?)(T16))|(T14)(.*?)(T8)(.*?)((T11)(.*?)(T15)|(T12)(.*?)(T16))))"

# abrimos el archivo y pasamos todas las lineas a una variable
with open('logs/Tlog.txt') as file:
    transitions = file.readlines()
transitions = transitions[1]
# print(transitions)


while 1:
    # buscamos un match
    result = re.search(pattern,transitions)
    # si result es None significa que no se encontro match, salimos del loop
    if result == None:
        break

    # posicion del caracter donde inicia el match
    start = result.span()[0]
    matchs_counter += 1
    # si el match no empieza en 0 entonces dividimos el string
    if start > 0:
        pre, transitions = transitions[:start], transitions[start:]
    else:
        pre = ""

    # obtenemos un array de lo que fue matcheado por todos los grupos que conforman la regex
#     print("\n===============================================")
#     groups_list = list(result.groups())
#     print("Inicio de match: " + str(start))
#     print("Grupos: ", end="")
#     print(*groups_list, sep=", ")
#     print("Match encontrado: ", end="")

    # vamos a revisar a que invariante corresponde
    # loopeamos entre todas
    for groups in CONVINATIONS:
        
        # ultima posicion del array
        last_group = groups[len(groups) - 1] - 1

        # revisamos si en el grupo final hay una transicion o no. Eso indica si fue esa la invariante encontrada
        if groups_list[last_group] != None:
            # revisamos si en el grupo final hay una transicion o no. Eso indica si fue esa la invariante encontrada
            if len(groups_list[last_group]) == 2 or len(groups_list[last_group]) == 3:
                # vamos grupo por grupo obteniendo la transicion a la que corresponde y eliminandola del string de transiciones.
                for group in groups:
#                     print(groups_list[group-1], end="")
                    transitions = re.sub(groups_list[group-1] + r'(?=\w)',"",transitions,1)
            break

    transitions = pre + transitions
#     print(transitions)
# la ultima ejecucion siempre sobra la ultima transicion
if len(transitions) == 3:
    transitions = ""


print("\n===============================================")
print("Transiciones restantes: " + transitions )
print("Cantidad de matchs encontrados: " + str(matchs_counter) + "\n")



