#                                PROYECTO DE CREACION DE APIS 🖱️ 😎
En este proyecto hemos realizado la creacion de 4 APIS para calcular en "area" y "volumen" depende de lo que el usuario necesite hallar.
En total tenemos 10 figuras sacadas de la siguente imagen [Figura geometricas](https://github.com/cs1000-utec/pc2/blob/main/option4/geometry.jpg)
<a href="url"><img src="https://www.pragma.com.co/hubfs/academia/Im%C3%A1genes%20Blog/h_que_es_api_como_beneficia_negocio.jpg" align="left" height="170" width="990" ></a>
## *INTEGRANTES & CUENTA DE GITHUB* 💁
- [Brigitte Rojas Leon](https://github.com/DayaneRojas1506)
- [Paola Maguiña Aranda](https://github.com/PaolaMag)
- [Jorge Rojas Guillen](https://github.com/JorgeRojasGuillen)
- [Milloshy Crisostomo Rodriguez](https://github.com/MilloshyC-UTEC)
# Instrucciones para ejecutar el proyecto ☑️
. Tener intalado python3.8 o versiones superiores y tener instalado flask
*1.Lo primero que vamos hacer es entrar al **terminal** y clonar el repositorio para abrir el **main.py** del proyecto.
2.Luego entramos a **VSCODE** para verficar el contenido que se encuentra en el **main.py**
3.Corremos el codigo y debe  de aparecer 
 > Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
4. Por ultimo nos dirigimos al buscador y insertamos el URL que nos aperecio, indicando los parametros y valor que usted necesita.*
*A continuacion se explicara mas las especificacion que se encuentran en nuestro proyecto*

# Especificación del API
![Alt Text](https://media.giphy.com/media/KZYTMerDWCEKK9sV4Q/giphy.gif)
## ⭐API para figuras que necesitan un solo parámetro⭐
> Este API es para aquellas figuras que necesitan 1 solo parametro(cubo,esfera,tetrahedro regular)
### URL
`/cube/volumen/parametro1`
### Parametros
- parametro1: Lado del cubo
### Salida
Volumen del cubo
#### *Ejemplo 1*
```
- URL ---> localhost:8080/cube/volumen/5
- Salida ---> El volumen del cubo es: 125
```
---------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145692095-3b32091f-662e-41f1-846d-089d99ce8f7f.png)
------------------------------------------------------------------------------------------
### URL
`/cube/surfacearea/parametro1`
### Parametros
- parametro1: Lado del cubo
### Salida
Superficie del cubo
#### *Ejemplo 2*
```
- URL ---> localhost:8080/cube/surfacearea/4
- Salida ---> El área de la superficie del cubo es: 96
```
- ----------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145693332-9bbcb7b3-52ae-4034-9efd-38ffb984d74a.png)
--------------------------------------------------------------------------------------------------------

## ⭐API para figuras que necesitan dos parámetros⭐
> Este API es para aquellas figuras que necesitan 2 parametros(cono,piramide,cono circular,torus,piramide cuadrada,cilindro,)
### URL
`/general cone/volumen/parametro1/parametro2`
### Parametros
- parametro1: Área de la base
- parametro2: Altura
### Salida
Volumen del general cone

#### *Ejemplo 1*
```
- URL ---> localhost:8080/general cone/volumen/12/7
- Salida ---> El volumen del general cone es: 28
```
- -------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145692683-10ec7354-a9d9-4107-ae16-74383b27c5dc.png)
-----------------------------------------------------------------------

### URL
`/torus/volumen/parametro1/parametro2`
### Parametros
- parametro1: Tube radius
- parametro2: Torus radius
### Salida
Volumen del torus
#### *Ejemplo 2*
```
- URL ---> localhost:8080/torus/volumen/15/23
- Salida ---> El volumen del torus es: 102150.41
```
--------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145692791-1a73fd4b-904b-4dcd-8b4a-b3693fdec9ff.png)
--------------------------------------------------------
### URL
`/torus/surfacearea/parametro1/parametro2`
### Parametros
- parametro1: Tube radius
- parametro2: Torus radius
### Salida
Área del torus
#### *Ejemplo 3*
```
- URL ---> localhost:8080/torus/surfacearea/9/13
- Salida ---> El area del torus es: 4618.97
```
----------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145692742-0a0219c0-82dd-4236-a0ee-223027f72b47.png)
----------------------------------------------------------
### URL
`/right cicular cylinder/volumen/parametro1/parametro2`
### Parametros
- parametro1: radio
- parametro2: altura
### Salida
Volumen del right cicular cylinder
#### *Ejemplo 4*
```
- URL ---> localhost:8080/right cicular cylinder/volumen/6/21
- Salida ---> El volumen del right cicular cylinder es: 2375.04
```
----------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145693034-8cd581b5-901c-42a6-b715-3502bd207cb3.png)
------------------------------------------------------------------------
### URL
`/right cicular cylinder/surfacearea/parametro1/parametro2`
### Parametros
- parametro1: radio
- parametro2: altura
### Salida
Área del right cicular cylinder
#### *Ejemplo 5*
```
- URL ---> localhost:8080/right cicular cylinder/surfacearea/5/23
- Salida ---> El area de superficie del right cicular cylinder es: 879.65
```
---------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145693364-5ad005cc-5fc6-4d11-81d2-890b2a3637cb.png)
--------------------------------------------------------------------

## ⭐API para figuras que necesitan tres parámetros⭐
> Este API es para aquellas figuras que necesitan 3 parametros (rectangulo)
### URL
`/rectangulo solido/volumen/parametro1/parametro2/parametro3`
### Parametros
- parametro1: Largo
- parametro2: Ancho
- parametro3: Altura
### Salida
Volumen del rectangulo solido
#### *Ejemplo 1*
```
- URL ---> localhost:8080/rectangulo solido/volumen/20/13/8
- Salida ---> El volumen del rectangulo solido es: 2080
```
------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145692992-cfb20036-a002-454f-a6a4-3d223ebda873.png)
---------------------------------------------------------------------------------
### URL
`/rectangulo solido/surfacearea/parametro1/parametro2/parametro3`
### Parametros
- parametro1: Largo
- parametro2: Ancho
- parametro3: Altura
### Salida
El área de la superficie del rectangulo solido
#### *Ejemplo 2*
```
- URL ---> localhost:8080/rectangulo solido/surfacearea/20/13/8
- Salida ---> El área del rectangulo solido es: 1048
```
--------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145693011-6ee3f883-6ea4-435f-ad4f-a51c35ce3a3e.png)
-----------------------------------------------------------------------------------------
## ⭐API para figuras que necesitan cuatro parámetros⭐
> Este API es para aquellas figuras que necesiten 4 parametro(tronco de un cono)
### URL
`/frustum of a cone/volumen/parametro1/parametro2/parametro3/parametro4`
### Parametros
- parametro1: Radio superior
- parametro2: Radio base
- parametro3: Altura
- parametro4: Altura inclinada
### Salida
El volumen del del tronco de un cono
#### *Ejemplo 1*
```
- URL ---> localhost:8080/frustum of a cone/volumen/11/8/19/3
- Salida ---> El volumen de tronco de un cono es: 5431.81
```
-------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145693295-de667a86-65f5-4b02-9805-14c139e6252a.png)
----------------------------------------------------------------------
### URL
`/frustum of a cone/surfacearea/parametro1/parametro2/parametro3/parametro4`
### Parametros
- parametro1: Radio superio
- parametro2: Radio base
- parametro3: Altura
- parametro4: Altura inclinada
### Salida
El área de la superficie del tronco de un cono
#### *Ejemplo 1*
```
- URL ---> localhost:8080/frustum of a cone/surfacearea/11/8/19/3
- Salida ---> El area de tronco de un cono es: 760.27
```
---------------------------------------------------------------
![image](https://user-images.githubusercontent.com/91268793/145693129-a1274236-2b66-4b72-9dce-2df6ff9804d0.png)
---------------------------------------------------------------
