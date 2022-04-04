#
 # Reto #9
 # CÓDIGO MORSE
 # Fecha publicación enunciado: 02/03/22
 # Fecha publicación resolución: 07/03/22
 # Dificultad: MEDIA
 #
 # Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 # - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 # - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 # - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 #
 #
from operator import contains
import re
codigoMorse = {
     'A':'.-',
     'B':'-...',
     'C':'-.-.',
     'D':'-..',
     'E':'.',
     'F':'..-.',
     'G':'--.',
     'H':'....',
     'I':'..',
     'J':'.---',
     'K':'-.-',
     'L':'.-..',
     'M':'--',
     'N':'-.',
     'O':'---',
     'P':'.--.',
     'Q':'--.-',
     'R':'.-.',
     'S':'...',
     'T':'-',
     'U':'..-',
     'V':'...-',
     'W':'.--',
     'X':'-..-',
     'Y':'-.--',
     'Z':'--..',
     '0':'-----',
     '1':'.----',
     '2':'..---',
     '3':'...--',
     '4':'....-',
     '5':'.....',
     '6':'-....',
     '7':'--...',
     '8':'---..',
     '9':'----.',
     '.':'·—·—·—',
     ',':'——··——',
     '?':'··——··',
     ' ':'  '}
morseDecodificado ={}
for key,value in codigoMorse.items():
    morseDecodificado.update({value:key})

regex = r'[a-zA-Z0-9]'
textoCodificado = ''
def codificar(texto):
    codificado =''
    for i in range (0,len(texto)):
        codificado = codificado +' '+codigoMorse.get(texto[i])
    return codificado
    
def decodificar(texto):
    decodificado = ''
    textoMorse = re.split("  ",texto)
    for cadena in textoMorse:
       caracteres = re.split(" ",cadena)
       for c in caracteres:
          if c != '':
            decodificado = decodificado + morseDecodificado.get(c)
       decodificado = decodificado +" "
    return decodificado

texto =str(input("Ingresa la cadena: ")).upper()
contiene = re.search(regex, texto)# si son caracteres alfanumericos llama a codificar
if contiene:
    textoCodificado = codificar(texto)
    print(textoCodificado)
else:
    textoDecodificado = decodificar(texto)
    print(textoDecodificado)
