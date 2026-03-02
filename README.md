# Producer/Consumer Simulation using a Petri Net

Final project for the Concurrent Programming course.

## Description

Java implementation of a Producer/Consumer system modeled using a Petri Net.

Synchronization is implemented through a Monitor using a binary semaphore.

The program receives:
- Incidence matrix
- Initial marking

It generates:
- A log file containing the fired transitions

Additionally, the repository provides:
- A script that extracts all transition invariants from the generated log file.

## Concepts Applied

- Concurrent programming
- Monitors
- Petri Nets
- Invariant analysis

## Execution

javac src/*.java  
java Main  
python3 scripts/script-invariantes.py



# Simulación Productor/Consumidor con Red de Petri

Trabajo práctico final de programacion concurrente.

## Descripción

Implementación en Java de un sistema Productor/Consumidor
modelado mediante una Red de Petri.

La sincronización se realiza utilizando un Monitor con semaforo binario.

El programa recibe:
- Matriz de incidencia
- Marcado inicial

Genera:
- Log de transiciones disparadas

Se provee:
- Script que extrae todas las invariantes de transicion disparadas en el archivo log.

## Conceptos aplicados

- Programación concurrente
- Monitores
- Redes de Petri
- Análisis de invariantes

## Ejecución

javac src/*.java
java Main
python3 scripts/script-invariantes.py