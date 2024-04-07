# Algoritmos Primeros 

Este algoritmo implementa una función para calcular los primeros de cada símbolo en una gramática dada. Los primeros de un símbolo en una gramática son los terminales que pueden aparecer como el primer símbolo de alguna cadena generada por ese símbolo.

## Ejemplo de Uso:

Se proporciona un ejemplo de gramática en forma de diccionario, junto con su llamada a la función principal `calcular_primeros(gramatica)`. Los primeros de cada símbolo en la gramática proporcionada se imprimen al final del script.

## Cambio de Gramática:

Para cambiar la gramática que se está analizando, es necesario reemplazar los elementos del diccionario `gramatica` con la nueva gramática deseada. El diccionario `gramatica` sigue la convención de tener símbolos no terminales como claves y producciones como listas de listas de símbolos (terminales y no terminales) como valores asociados a esas claves.

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


