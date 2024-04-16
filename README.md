# Guia de Uso:

Se proporciona un ejemplo de gramática en forma de diccionario, junto con su llamada a la función principal `calcular_primeros(gramatica)`, `calcular_siguientes(gramatica, primeros, simbolo_inicial)` y  `calcular_prediccion(gramatica, primeros, siguientes, no_terminal)`. Los primeros, siguientes y conjuntos de prediccion para la gramática proporcionada se imprimen al final del script. Para ejecutar el programa se debe usar el comando `python3 primeros.py`.

# Cambio de Gramática:

Para cambiar la gramática que se está analizando, es necesario reemplazar los elementos del diccionario `gramatica` con la nueva gramática deseada, hay opciones comentadas en codigo en caso de querer remplasarla con algun otro ejemplo o pueden ser modificadas. El diccionario `gramatica` sigue la convención de tener símbolos no terminales como claves y producciones como listas de listas de símbolos (terminales y no terminales) como valores asociados a esas claves.

# Algoritmos Primeros 

Este algoritmo implementa una función para calcular los primeros de cada símbolo en una gramática dada. Los primeros de un símbolo en una gramática son los terminales que pueden aparecer como el primer símbolo de alguna cadena generada por ese símbolo.

## Puntos Claves del Algoritmo:

1. **Definición de la Función Principal**: La función principal es `calcular_primeros(gramatica)`, que toma como entrada la gramática en forma de diccionario.

2. **Identificación de Terminales**: Se define la función `es_terminal(simbolo)` para determinar si un símbolo es terminal o no. Un símbolo se considera terminal si no está presente como clave en el diccionario que representa la gramática.

3. **Cálculo Recursivo de Primeros**: La lógica principal del algoritmo reside en la función recursiva `calcular_primeros_rec(simbolo)`, que calcula los primeros de un símbolo dado.

4. **Reglas para Calcular los Primeros**:
   - Regla 1: Si el símbolo es ε (épsilon), se agrega ε a los primeros de ese símbolo.
   - Regla 2a: Si el primer símbolo de una producción es terminal, se agrega ese terminal a los primeros del símbolo.
   - Regla 2b: Si el primer símbolo de una producción es no terminal, se calculan recursivamente los primeros de ese símbolo.
   - Regla 2c: Si todos los símbolos en una producción derivan ε, se agrega ε a los primeros del símbolo actual.
   - Regla 2d: Se continua el cálculo hasta que ya no se agreguen ε a los primeros del símbolo actual.

5. **Iteración sobre la Gramática**: Se itera sobre cada símbolo en la gramática y se calculan sus primeros llamando a `calcular_primeros_rec(simbolo)`.

# Algoritmo de Siguientes

Este algoritmo implementa una función para calcular los siguientes de cada símbolo no terminal en una gramática dada. Los siguientes de un símbolo no terminal en una gramática son los terminales que pueden aparecer inmediatamente a continuación de ese símbolo en alguna cadena generada por la gramática.

### Pasos del algoritmo:

1. **Inicialización**: Inicializar el conjunto de siguientes de cada símbolo no terminal como vacío.
   
2. **Añadir Símbolo Inicial**: Añadir el símbolo inicial de la gramática al conjunto de siguientes de sí mismo.

3. **Iteración**: Iterar hasta que ya no haya cambios en los conjuntos de siguientes:
   - Para cada regla de producción A -> αBβ, donde B es un símbolo no terminal y α y β son cadenas de símbolos terminales y/o no terminales:
     - Añadir los primeros de β (excluyendo ε si está presente) al conjunto de siguientes de B.
     - Si ε está en los primeros de β, añadir los siguientes de A al conjunto de siguientes de B.
   
4. **Resultados**: Una vez que no haya más cambios en los conjuntos de siguientes, los conjuntos de siguientes de cada símbolo no terminal están completos y pueden ser utilizados según sea necesario.

# Algoritmo de Predicción

Este algoritmo implementa una función para calcular las predicciones de cada producción de un símbolo no terminal en una gramática dada. Las predicciones de una producción son los terminales que pueden aparecer como el siguiente símbolo después de esa producción en una cadena generada por el símbolo no terminal correspondiente.

## Pasos del algoritmo:

1. **Inicialización**: Inicializar un conjunto de predicciones para cada producción del símbolo no terminal dado.

2. **Calcular Predicciones**:
   - Para cada producción del símbolo no terminal:
     - Calcular las predicciones de esa producción llamando a una función recursiva `calcular_prediccion_rec`.

3. **Función Recursiva**:
   - Para cada símbolo en la producción:
     - Si el símbolo es un no terminal, calcular sus primeros y agregarlos a las predicciones.
     - Si el símbolo es un terminal, agregarlo a las predicciones.
     - Si el símbolo es ε, agregar los siguientes del no terminal al conjunto de predicciones.

4. **Resultados**: Una vez completado el proceso, se obtienen las predicciones de cada producción del símbolo no terminal dado.







