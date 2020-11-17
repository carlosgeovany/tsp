# TSP

## Datos

Los archivos contenidos en la carpeta `data` provienen originalmente
de [National Traveling Salesman Problems](https://www.math.uwaterloo.ca/tsp/world/countries.html).

Pero el formato fué modificado para este proyecto.

| Original                | Nombre               |
|:-----------------------:|:--------------------:|
| ar9162.tsp              | argentina.tsp        |
| att_48.tsp, att48_d.txt | eua.tsp, eua48_d.tsp |
| dantzig42_d.tsp         | dantzig_d.tsp        |
| nu3496.tsp              | nicaragua.tsp        |
| qa194.tsp               | qatar.tsp            |
| ym7663.tsp              | yemen.tsp            |
| p01_d.txt, p01_xy.txt   | p01.tsp, p01_d.tsp   |

Los archivos sin sufijo `_d` contienen las coordenadas. Los que tienen
el sufijo `_d` la matriz de distancia.


## Soluciones

La tabla completa con las soluciones y los resultados se encuentran en [solutions](solutions).

A continuación se muestran algunos resultados de los problemas y sus soluciones:

#### Random

Desde la línea de comandos se ejecuta: 

`calculate_tour --random --filename "solutions/random.png" solve`

El grafo del problema resuelto es el siguiente:

![random](https://github.com/carlosgeovany/tsp/blob/master/solutions/random.png)

La solución completa al problema [random](https://github.com/carlosgeovany/tsp/blob/master/solutions/random.txt)
es la siguiente:

| algoritmo | hiperparámetros | costo | tour                      | tiempo |
|:---------:|:---------------:|:-----:|:-------------------------:|:------:|
| AntColony | alpha: 0.5 	  | 325.59| Place(id=3, x=51, y=63)-> | 0.197  |
|			| beta: 1.0		  |			Place(id=1, x=73, y=69)-> |        |
|			| rho: 0.8		  |			Place(id=0, x=59, y=90)-> |		   |	
|			| Q: 10			  |			Place(id=9, x=99, y=88)-> |        |
|			| max_steps: 100  |			Place(id=5, x=77, y=41)-> |        |
|			|							Place(id=4, x=73, y=34)-> |        |
|			|							Place(id=2, x=52, y=39)-> |		   |
|			|							Place(id=7, x=49, y=36)-> |		   |
|			|							Place(id=6, x=32, y=17)-> |		   |
|			|							Place(id=8, x=12, y=92)-> |  	   |
|			|							Place(id=3, x=51, y=63)	  |		   |
 
