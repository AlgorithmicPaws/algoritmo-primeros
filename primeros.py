#funcion principal
def calcular_primeros(gramatica):
    primeros = {}
    
    # Función auxiliar para determinar si un símbolo es terminal
    def es_terminal(simbolo):
        return simbolo not in gramatica.keys()

    
    # Función recursiva para calcular los primeros de un símbolo
    # PRIMEROS(αlpha) = primeros
    # PRIMEROS(a1) = primeros_del_simbolo
    def calcular_primeros_rec(simbolo):
        # Si ya hemos calculado los primeros para este símbolo, regresar
        if simbolo in primeros:
            return primeros[simbolo]
        
        primeros[simbolo] = set()
        
        # Regla 1: Si es épsilon, agregar épsilon
        if simbolo == 'ε':
            primeros[simbolo].add('ε')
            return primeros[simbolo]
        
        #symbol itera todos los no term. y simbolo es la regla actual
        for produccion in gramatica[simbolo]:
            # Regla 2a: Si es un terminal, agregarlo
            if es_terminal(produccion[0]):
                primeros[simbolo].add(produccion[0])
            # Regla 2b, 2c, 2d: Si es un no terminal, calcular primeros recursivamente
            else:
                for i, symbol in enumerate(produccion):
                    if es_terminal(symbol):
                        primeros[simbolo].add(symbol)
                        break
                    #regla 2d: se llama recursivamente 
                    primeros_del_simbolo = calcular_primeros_rec(symbol)
                    #regla 2b: restando epsilon
                    primeros[simbolo].update(primeros_del_simbolo - {'ε'})
                    if 'ε' not in primeros_del_simbolo:
                        break
                    #regla 2c: n=1
                    if i == len(produccion) - 1:
                        primeros[simbolo].add('ε')
        
        return primeros[simbolo]
    
    # Calcular primeros para cada símbolo de la gramática
    for simbolo in gramatica:
        calcular_primeros_rec(simbolo)
    
    return primeros

# Ejemplo de diapositivas del profe
gramatica = {
    'S': [['A', 'uno', 'B', 'C'], ['S','dos']],
    'A': [['B', 'C', 'D'], ['A', 'tres'], ['ε']],
    'B': [['D', 'cuatro', 'C', 'tres'], ['ε']],
    'C': [['cinco','D', 'B'], ['ε']],
    'D': [['seis'], ['ε']]
}

# Ejercicio de diapositivas del profe
"""gramatica = {
    'A': [['B', 'C'], ['ant', 'A', 'all']],
    'B': [['big', 'C'], ['bus', 'A', 'boss'], ['ε']],
    'C': [['cat'], ['cow']],
}"""

#llamar a la funcion principal
primeros = calcular_primeros(gramatica)
for simbolo, primeros_simbolo in primeros.items():
    print(f'PRIMEROS({simbolo}): {primeros_simbolo}')
