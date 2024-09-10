import random

def verificacionLetras (verificar):
    print('\nIngrese su palabra:')
    palabra = ''
    while verificar == False:
        palabra = input('').upper()
        if len(palabra) != len(wordle):
            print(f'SU PALABRA NO ES DE {len(wordle)} LETRAS')
        else:
            verificar = True
    return palabra
    

ganador = False
verificarLetras = False
palabraCorrecta = False

posicionCorrecta = []
letraCorrecta= []

palabras = ['CREATE', 'DELETE', 'READ', 'UPDATE', 'DETAILS', 'STUDENT', 'ENROLLMENT', 'EDIT', 'RAZOR', 'OVERPOSTING', 'MODEL', 'ENTITY', 'INSERT', 'REMOVE', 'DETACHED']
wordle = palabras[random.randint(0, (len(palabras) - 1))]
largo = len(wordle)

print(f'\n\n\t\t\tINGRESE PALABRAS DE {largo} LETRAS:\n')

while ganador == False:
    posicionCorrecta.clear()
    letraCorrecta.clear()
    for i in range(largo):
        posicionCorrecta.append(False)
        letraCorrecta.append(False)
    
    palabra = verificacionLetras(verificarLetras)
    
    if palabra == wordle:
        ganador = True
        print('\n\n------------------------------------------------------------------------------')
        print('\t\t\t\tFELICIDADES GANASTE')
        print('------------------------------------------------------------------------------')
        break
        
    posicion = 0
    for i in range(largo):
        if palabra[i] == wordle[i]:
            posicionCorrecta[posicion] = True
            letraCorrecta[posicion] = True
        posicion += 1
    
    posicionesIncorrectas = []
    for i in range(largo):
        if posicionCorrecta[i] == False:
            posicionesIncorrectas.append(i)
    
    for i in posicionesIncorrectas:
        for x in posicionesIncorrectas:
            if palabra[i] == wordle[x]:
                letraCorrecta[i] = True
    
    print('\n', end = '\t\t')          
    for i in range(largo):
        print(f'[ {palabra[i]}', end = ' ]  ')
        
    print('\n', end = '\t\t')   
    for i in posicionCorrecta:
        if i == True:
            print(f'  o', end = '    ')
        else:
            print(f'  x', end = '    ')
    
    print('\n', end = '\t\t')   
    for i in letraCorrecta:
        if i == True:
            print(f'  o', end = '    ')
        else:
            print(f'  x', end = '    ')    

    
# print('\n')
# print(palabra)
# print(posicionCorrecta)
# print(letraCorrecta)