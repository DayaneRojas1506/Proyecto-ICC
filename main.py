from flask import Flask, render_template
import math
app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1>', methods=['GET'])
#esto es para figuras que necesitan 1 parametro
def CalculoCon1Parametro(figurageometrica,volumenosurfacearea,parametro1):
  # Su código va aquí
  if figurageometrica=='cube': #esto es si es un cubo
    if volumenosurfacearea=='volumen':
     volumen= (parametro1)**3  
     return f'El volumen del cubo es:{volumen}'
    elif volumenosurfacearea=='surfacearea': 
     surfacearea=6*(parametro1)**2
     return f'El area de la supercificie del cubo es:{surfacearea}'
    else:
      return "Ingrese area o volumen, por favor" 

  if figurageometrica=='sphere':#esto es si es una esfera
    if volumenosurfacearea=='volumen':
     volumen= (4/3)*math.pi*(parametro1)**3
     return f'El volumen de la esfera es: {volumen}'
    elif volumenosurfacearea=='surfacearea': 
     surfacearea=4*math.pi*(parametro1)**2
     return f'El area de la superficie de la esfera es: {surfacearea}'
    else:
      return "Ingrese area o volumen, por favor"    

  if figurageometrica=='regular tetrahedron':#esto es si es tetrahedro
    if volumenosurfacearea=='volumen':
     volumen= (1/12)*math.sqrt(2)*(parametro1)**3
     return f'El volumen del tetrahedro regular es: {volumen}'
    elif volumenosurfacearea=='surfacearea': 
     surfacearea=math.sqrt(3)*(parametro1)**2
     return f'El area de la superficie del tetrahedro regular es : {surfacearea}'
    else:
      return "Ingrese area o volumen, por favor" 


@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1><parametro2>', methods=['GET'])
#esto es para figuras que necesitan 2 parametros
def CalculoCon2parametros(figurageometrica,volumenosurfacearea,parametro1,parametro2):
    # Su código va aquí
    if figurageometrica=='general cone' or figurageometrica=='general pyramid':
      if volumenosurfacearea=='volumen':
        volumen = (1/3)*parametro1*parametro2
        return f'El volumen del general cone es:{volumen}'

    elif figurageometrica=='right cicular cone':
      if volumenosurfacearea=='volumen':
        volumen = (1/3)*math.pi*((parametro1)**2)*parametro2
        return f'El volumen del right circular cone es:{volumen}'
      elif volumenosurfacearea=='surfacearea':
        surfacearea = math.pi*(parametro1)*(math.sqrt(((parametro1)**2)+((parametro2)**2))) + (math.pi*((parametro1)**2))
        return f'El area de la superficie del rigth circular cone es:{surfacearea}'
      else:
        return("opcion invalida")
        
    elif figurageometrica=='right cicular cylinder':
      if volumenosurfacearea=='volumen':
        volumen = math.pi*((parametro1)**2)*parametro2
        return f'El volumen del right circular cylinder es:{volumen}'
      elif volumenosurfacearea=='surfacearea':
        surfacearea = (2*math.pi*parametro1*parametro2) + (2*math.pi*((parametro1)**2))
        return f'El area de superficie del right circular cylinder es:{surfacearea}'
      else:
        return("opcion invalida")
        
    elif figurageometrica=='square pyramid':
      if volumenosurfacearea=='volumen':
        volumen = (1/3)*((parametro1)**2)*parametro2
        return f'El volumen del {figurageometrica} es: {volumen}'
      elif volumenosurfacearea=='surfacearea':
        surfacearea = parametro1*(parametro1+ (math.sqrt((parametro1**2)+(4*(parametro2**2)))))
        return f'El area de superficie del {figurageometrica} es: {surfacearea}'
      else:
        return("opcion invalida")
        
    elif figurageometrica=='torus':
      if volumenosurfacearea=='volumen':
        volumen = 2*(math.pi**2)*(parametro1**2)*parametro2
        return f'El volumen del {figurageometrica} es:{volumen}' 
      elif volumenosurfacearea=='surfacearea':
        surfacearea = 4*(math.pi**2)*parametro1*parametro2
        return f'El area de superficie del {figurageometrica} es: {surfacearea}'
      else:
        return("opcion invalida")
      
      
'''elif figurageometrica == 'rigthCircularCone':
  if volumenosurfacearea=="volumen":
    volumen = ((math.pi*parametro1**2*parametro2)*(1/3)
return volumen
  elif volumenosurfacearea=="surfacearea":
   surfacearea = math.pi*parametro1*((parametro1**2 + parametro2**2)××(1/2))+math.pi×parametro1××2
return surfacearea'''

        
@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1>/<parametro2>/<parametro3>', methods=['GET'])
#esto es para figuras que necesitan 3 parametros
def CalculoCon3Parametros(figurageometrica,volumenosurfacearea,parametro1,parametro2,parametro3):
  if figurageometrica =="rectangulo solido":
    if volumenosurfacearea=="volumen":
      volumen=(parametro1*parametro2*parametro3)
      return f'El volumen del rectangulo es: {volumen}'
    elif volumenosurfacearea=="surfacearea":
      area= 2*(parametro1*parametro2)+2*(parametro1*parametro3)+2*(parametro2*parametro3)
      return f'El area del rectangulo es:{area}'
    else:
      return "Ingrese area o volumen, por favor"

@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1>', methods=['GET'])
#esto es para figuras que necesitan 4 parametros
def calculoCon4Parametros(figurageometrica,volumenosurfacearea,parametro1,parametro2,parametro3, parametro4):
  if figurageometrica == "frustum of a cone":
    if volumenosurfacearea=="volumen":
      volumen = ((math.pi/3)*(parametro1**2+parametro1*parametro2+parametro2**2))*parametro3
      return f'El volumen de tronco de un cono es: {volumen}'

    elif volumenosurfacearea== "area":
      area = (math.pi*parametro4)*(parametro2+parametro1)+(math.pi*parametro1**2)+(math.pi*parametro2**2)
      return f'El area del tronco de un cono es: {area}'


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))


