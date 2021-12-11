# Especificación del API
## ⭐API para figuras que necesitan un solo parámetro
### URL
/cube/volumen/parametro1
### Parametros
- parametro1 Lado del cubo
### Salida
Volumen del cubo

### Ejemplo
- URL ---> localhost:8080/cube/volumen/5
- Salida ---> El volumen del cubo es: 125

### URL
/cube/surfacearea/parametro1
### Parametros
- parametro1: Lado del cubo
### Salida
Superficie del cubo

### Ejemplo
- URL ---> localhost:8080/cube/surfacearea/4
- Salida ---> El area de la superficie del cubo es: 96


## ⭐API para figuras que necesitan dos parámetros
### URL
/general cone/volumen/parametro1/parametro2
### Parametros
- parametro1: Area de la base
- parametro2: Altura
### Salida
Volumen del general cone

### Ejemplo
- URL ---> localhost:8080/general cone/volumen/12/7
- Salida ---> El volumen del general cone es: 28

## ⭐API para figuras que necesitan tres parámetros
### URL
/rectangulo solido/volumen/parametro1/parametro2/parametro3
### Parametros
- parametro1: Largo
- parametro2: Ancho
- parametro3: Altura
### Salida
Volumen del rectangulo solido
### Ejemplo
- URL ---> localhost:8080/rectangulo solido/volumen/20/13/8
- Salida ---> El volumen del rectangulo solido es: 2080

- URL ---> localhost:8080/general cone/volumen/12/7
- Salida ---> El volumen del general cone es: 28

### URL
/rectangulo solido/surfacearea/parametro1/parametro2/parametro3
### Parametros
- parametro1: Largo
- parametro2: Ancho
- parametro3: Altura
### Salida
El area de la superficie del rectangulo solido
### Ejemplo
- URL ---> localhost:8080/rectangulo solido/volumen/20/13/8
- Salida ---> El area de la superficie del rectangulo solido es: 2080
