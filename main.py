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

  if figurageometrica=='sphere':#esto es si es una esfera
    if volumenosurfacearea=='volumen':
     volumen= (4/3)*math.pi*(parametro1)**3
     return f'El volumen de la esfera es: {volumen}'
    elif volumenosurfacearea=='surfacearea': 
     surfacearea=4*math.pi*(parametro1)**2
     return f'El area de la superficie de la esfera es: {surfacearea}'   

  if figurageometrica=='regular_tetrahedron':#esto es si es tetrahedro
    if volumenosurfacearea=='volumen':
     volumen= (1/12)*math.sqrt(2)*(parametro1)**3
     return f'El volumen del tetrahedro regular es: {volumen}'
    elif volumenosurfacearea=='surfacearea': 
     surfacearea=math.sqrt(3)*(parametro1)**2
     return f'El area de la superficie del tetrahedro regular es : {surfacearea}'


@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1><parametro2>', methods=['GET'])
#esto es para figuras que necesitan 2 parametros
def CalculoCon2parametros(figurageometrica,volumenosurfacearea,parametro1,parametro2):
    # Su código va aquí
    if figurageometrica=='general cone' or figurageometrica=='general pyramid':
      if volumenosurfacearea=='volumen':
        volumen = (1/3)*parametro1*parametro2
        return volumen
    elif figurageometrica=='right cicular cone':
      if volumenosurfacearea=='volumen':
        volumen = (1/3)*math.pi*((parametro1)**2)*parametro2
        return volumen
      elif volumenosurfacearea=='surfacearea':
        surfacearea = math.pi*(parametro1)*(math.sqrt(((parametro1)**2)+ ((parametro2)**2))) + (math.pi*((parametro1)**2))
        return surfacearea
      else:
        return("opcion invalida")
    elif figurageometrica=='right cicular cylinder':
      if volumenosurfacearea=='volumen':
        volumen = math.pi*((parametro1)**2)*parametro2
        return volumen
      elif volumenosurfacearea=='surfacearea':
        surfacearea = (2*math.pi*parametro1*parametro2) + (2*math.pi*((parametro1)**2))
        return surfacearea
      else:
        return("opcion invalida")
      
      
        
@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1>/<parametro2>/<parametro3>', methods=['GET'])
def rectangulo_solido(figurageometrica,volumenosurfacearea,parametro1,parametro2,parametro3):
  if figurageometrica =="rectangulo_solido":
    if volumenosurfacearea=="volumen":
      volumen=(parametro1*parametro2*parametro3)
      return volumen
    elif volumenosurfacearea=="area":
      area= 2*(parametro1*parametro2)+2*(parametro1*parametro3)+2*(parametro2*parametro3)
      return area
    else:
      return "Ingrese area o volumen, por favor"
      
elif figurageometrica == 'rigthCircularCone':
  if volumenosurfacearea=="volumen":
    volumen = math.pi*
@app.route('/<figurageometrica>/<volumenosurfacearea>/<parametro1>', methods=['GET'])
def rectangulo_solido(figurageometrica,volumenosurfacearea,parametro1,parametro2,parametro3):
  if figurageometrica =="rectangulo_solido":
    parametro1*parametro2+parametro3
    
    
  


   

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))


