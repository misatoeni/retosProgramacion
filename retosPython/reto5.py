#
 # Reto #4
 # ÁREA DE UN POLÍGONO
 # Fecha publicación enunciado: 24/01/22
 # Fecha publicación resolución: 31/01/22
 # Dificultad: FÁCIL
 #
 # Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 # - La función recibirá por parámetro sólo UN polígono a la vez.
 # - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 # - Imprime el cálculo del área de un polígono de cada tipo.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda la acomunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def calcularAreaPoligono(a,b,poligono):
    if a== 0:
        raise Exception("Es necesario ingresar valor 'a' mayor a 0")
    if poligono == 'triángulo':
        if b == 0:
            raise Exception("Es necesario ingresar valor 'b' mayor a 0")
        return ((a*b)//2)
    elif poligono == 'cuadrado':
        return a*a
    elif poligono == 'rectángulo':
        if b == 0:
            raise Exception("Es necesario ingresar valor 'b' mayor a 0")
        return a*b
    else:
        raise Exception("Polígono no soportado")


print("Calculando area poligonos:")
print("calculando para cuadrado : a = 10 , área = "+ str(calcularAreaPoligono(10,0,'cuadrado')))
print("calculando para triángulo : a = 7, b= 8, área = "+ str(calcularAreaPoligono(7,8,'triángulo')))
print("calculando para reactangulo : a = 9, b= 5, área = "+ str(calcularAreaPoligono(9,5,'rectángulo')))
##print("calculando para rectabgulo : a = 9, b= 0, área = "+ str(calcularAreaPoligono(9,0,'rectángulo')))
