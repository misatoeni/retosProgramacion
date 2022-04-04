#
 # Reto #1
 # ¿ES UN ANAGRAMA?
 # Fecha publicación enunciado: 03/01/22
 # Fecha publicación resolución: 10/01/22
 # Dificultad: MEDIA
 #
 # Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 # Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 # NO hace falta comprobar que ambas palabras existan.
 # Dos palabras exactamente iguales no son anagrama.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda la acomunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 #
 #/

def isAnagrama(palabra1, palabra2):
    longitudoPal1 = len(palabra1)
    longitudPal2 = len(palabra2)

    if longitudoPal1 > longitudPal2:
        return False
    elif palabra1 == palabra2:
        return False
    else:
        palabra1Sorted = sortWord(palabra1)
        palabra2Sorted = sortWord(palabra2)
        if palabra1Sorted == palabra2Sorted:
            return True
        else: 
            return False


def sortWord(palabra):
   charactersSorted = sorted(palabra)
   return ''.join(charactersSorted)




palabra1 = str(input("Ingresa la palabra 1: "))
palabra2 = str(input("Ingresa la palabra 2: "))


print("Es anagrama") if isAnagrama(palabra1,palabra2) else print("No es anagrama")

def isPalindromo(palabra1, palabra2):
    longitudoPal1 = len(palabra1)
    longitudPal2 = len(palabra2)

    if longitudoPal1 > longitudPal2 or longitudPal2 > longitudoPal1:
        return False
    else:
        palabra1Reversed = "".join(reversed(palabra1.lower()))
        palabra2Reversed = "".join(reversed(palabra2.lower()))

        if palabra1 == palabra2Reversed or palabra2 == palabra1Reversed:
            return True
        else:
            return False
