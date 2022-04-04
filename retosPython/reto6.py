#
 # Reto #5
 # ASPECT RATIO DE UNA IMAGEN
 # Fecha publicación enunciado: 01/02/22
 # Fecha publicación resolución: 07/02/22
 # Dificultad: DIFÍCIL
 #
 # Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 # - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 # - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920#1080px.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda la acomunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
from PIL import Image
import urllib.request
from io import BytesIO
from fractions import Fraction
url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png'
#conectando a la url
webUrl = urllib.request.urlopen(url)
if webUrl.getcode() == 200:
    response = webUrl.read()
    imagen = Image.open(BytesIO(response))
    tuplaMedidas= imagen.size
    heigth = tuplaMedidas[1]
    width = tuplaMedidas[0]
    print(str(heigth)+ ' '+ str(width))
    aspectRatio = Fraction(heigth / width)
    print(str(aspectRatio.denominator)+':'+str(aspectRatio.numerator))