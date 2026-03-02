# Simulación Productor/Consumidor con Red de Petri

Trabajo práctico de concurrencia.

## Descripción

Implementación en Java de un sistema Productor/Consumidor
modelado mediante una Red de Petri.

La sincronización se realiza utilizando un Monitor.

El programa recibe:
- Matriz de incidencia
- Marcado inicial

Genera:
- Log de transiciones disparadas
- Archivo con invariantes calculadas

## Conceptos aplicados

- Programación concurrente
- Monitores
- Redes de Petri
- Análisis de invariantes

## Ejecución

javac src/*.java
java Main matriz.txt marcado.txt