# Especificación del API
## API para figuras que necesitan un solo parametro
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


## API para figuras que necesitan dos parametro
### URL
/general cone/volumen/parametro1/parametro2
### Parametros
- parametro1: Area de la base
- parametro2: altura
### Salida
Volumen del general cone

### Ejemplo
- URL ---> localhost:8080/general cone/volumen/12/7
- Salida ---> El volumen del general cone es: 28
