# Especificación del API
## API para figuras que necesitan un solo parámetro
### URL
/cube/volumen/parametro1
### Parametros
- parametro1: Lado del cubo
### Salida
Volumen del cubo
### Ejemplo 1
- URL ---> localhost:8080/cube/volumen/5
- Salida ---> El volumen del cubo es: 125

### URL
/cube/surfacearea/parametro1
### Parametros
- parametro1: Lado del cubo
### Salida
Superficie del cubo
### Ejemplo 2
- URL ---> localhost:8080/cube/surfacearea/4
- Salida ---> El área de la superficie del cubo es: 96


## API para figuras que necesitan dos parámetros
### URL
/general cone/volumen/parametro1/parametro2
### Parametros
- parametro1: Área de la base
- parametro2: Altura
### Salida
Volumen del general cone

### Ejemplo 1
- URL ---> localhost:8080/general cone/volumen/12/7
- Salida ---> El volumen del general cone es: 28

## API para figuras que necesitan tres parámetros
### URL
/rectangulo solido/volumen/parametro1/parametro2/parametro3
### Parametros
- parametro1: Largo
- parametro2: Ancho
- parametro3: Altura
### Salida
Volumen del rectangulo solido
### Ejemplo 1
- URL ---> localhost:8080/rectangulo solido/volumen/20/13/8
- Salida ---> El volumen del rectangulo solido es: 2080

### URL
/rectangulo solido/surfacearea/parametro1/parametro2/parametro3
### Parametros
- parametro1: Largo
- parametro2: Ancho
- parametro3: Altura
### Salida
El área de la superficie del rectangulo solido
### Ejemplo 2
- URL ---> localhost:8080/rectangulo solido/surfacearea/20/13/8
- Salida ---> El área del rectangulo solido es: 1048

## API para figuras que necesitan cuatro parámetros
### URL
/frustum of a cone/volumen/parametro1/parametro2/parametro3/parametro4
### Parametros
- parametro1: Radio superio
- parametro2: Radio base
- parametro3: Altura
- parametro4: Altura inclinada
### Salida
El volumen del del tronco de un cono
### Ejemplo 1
- URL ---> localhost:8080/frustum of a cone/volumen/11/8/19/3
- Salida ---> El volumen de tronco de un cono es: 5431.81

### URL
/frustum of a cone/surfacearea/parametro1/parametro2/parametro3/parametro4
### Parametros
- parametro1: Radio superio
- parametro2: Radio base
- parametro3: Altura
- parametro4: Altura inclinada
### Salida
El área de la superficie del tronco de un cono
### Ejemplo 1
- URL ---> localhost:8080/frustum of a cone/surfacearea/11/8/19/3
- Salida ---> El area de tronco de un cono es: 5431.81
