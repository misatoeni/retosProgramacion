from django.shortcuts import render
from django.http import HttpResponse
import json
import re
import urllib.request

def index(request):
    # Create your views here.
    source = urllib.request.urlopen('https://swapi.dev/api/people/').read()
    contenidoRespuesta = json.loads(source)
    resultados = contenidoRespuesta['results']
    listaPersonajes = []
    for result in resultados:
        personaje = {'nombre':str(result['name']),
        'peso':str(result['mass']),
        'altura':str(result['height']),
        'fechaNacimiento':str(result['birth_year']),
        'genero':str(result['gender'])}
        listaPersonajes.append(personaje)
    
    nextPag = contenidoRespuesta['next']
    previousPag = contenidoRespuesta['previous']
    valorNext=re.split("=",nextPag)
    context={
        'listaPersonajes':listaPersonajes,
        'nextPag':valorNext[1],
        'previousPag':'#'    
    }
    return render(request, "starwarsapp/index.html",context)


def detalle(request,nombre):
    character = re.split("\s+",nombre)
    source = urllib.request.urlopen('https://swapi.dev/api/people/?search='+character[0]).read()
    contenidoRespuesta = json.loads(source)
    resultado = contenidoRespuesta['results'][0]
    planetaSource = urllib.request.urlopen(resultado['homeworld']).read()
    planetaRespuesta = json.loads(planetaSource)
    
    personaje = {'nombre':str(resultado['name']),
        'peso':str(resultado['mass']),
        'altura':str(resultado['height']),
        'fechaNacimiento':str(resultado['birth_year']),
        'genero':str(resultado['gender']),
        'colorCabello':str(resultado['hair_color']),
        'colorpiel':str(resultado['skin_color']),
        'colorOjos':str(resultado['eye_color']),
        'planetaOrigen':planetaRespuesta['name'],
        }
    return render(request , "starwarsapp/detalle.html",personaje)

def paginacion(request,pagina):
 # Create your views here.
    urlRoute = ''
    if pagina != '#':        
        urlRoute = 'https://swapi.dev/api/people/?page='+str(pagina)
    else:
        urlRoute = 'https://swapi.dev/api/people/'
    source = urllib.request.urlopen(urlRoute).read()
    contenidoRespuesta = json.loads(source)
    resultados = contenidoRespuesta['results']
    listaPersonajes = []
    for result in resultados:
        personaje = {'nombre':str(result['name']),
        'peso':str(result['mass']),
        'altura':str(result['height']),
        'fechaNacimiento':str(result['birth_year']),
        'genero':str(result['gender'])}
        listaPersonajes.append(personaje)
    nextPag = '#'
    previousPag = '#'
    if contenidoRespuesta['previous'] != None:
        valorPrevious = re.split("=",contenidoRespuesta['previous'])
        previousPag= valorPrevious[1]

    if contenidoRespuesta['next'] != None:
        valorNext = re.split("=",contenidoRespuesta['next'])
        nextPag=valorNext[1]
    context={
        'listaPersonajes':listaPersonajes,
        'nextPag':nextPag,
        'previousPag':previousPag
    }
    return render(request, "starwarsapp/index.html",context)