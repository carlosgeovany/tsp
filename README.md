# TSP

## Data

Files inside `data` folder originally provided by [National Traveling Salesman Problems](https://www.math.uwaterloo.ca/tsp/world/countries.html).

Although, format was modifyed for this project.

| Original                | Name               |
|:-----------------------:|:--------------------:|
| ar9162.tsp              | argentina.tsp        |
| att_48.tsp, att48_d.txt | eua.tsp, eua48_d.tsp |
| dantzig42_d.tsp         | dantzig_d.tsp        |
| nu3496.tsp              | nicaragua.tsp        |
| qa194.tsp               | qatar.tsp            |
| ym7663.tsp              | yemen.tsp            |
| p01_d.txt, p01_xy.txt   | p01.tsp, p01_d.tsp   |

Files without sufix `_d` are the coordenates. Those with sufix `_d`
contains distance matrix.

## How to run

From command line: 

### For a random problem

`calculate_tour --random --filename [full path with file extension .png, jpg] solve`

It will save a .txt file with the full problem solution with:

| algorithm | hyperparameters | cost | tour | time |

And the solution plot as a image like:

![random](https://github.com/carlosgeovany/tsp/blob/master/solutions/random.png)


### For a problem



## Solutions

La tabla completa con las soluciones y los resultados se encuentran en [solutions](solutions).



| algoritmo | hiperparámetros | costo | tour                      | tiempo |
|:---------:|:---------------:|:-----:|:-------------------------:|:------:|
| AntColony | alpha: 0.5 	  | 325.59| Place(id=3, x=51, y=63)-> | 0.197  |
|			| beta: 1.0		  |		  |	Place(id=1, x=73, y=69)-> |        |
|			| rho: 0.8		  |		  |	Place(id=0, x=59, y=90)-> |		   |	
|			| Q: 10			  |		  |	Place(id=9, x=99, y=88)-> |        |
|			| max_steps: 100  |		  |	Place(id=5, x=77, y=41)-> |        |
|			|				  |		  |	Place(id=4, x=73, y=34)-> |        |
|			|				  |		  |	Place(id=2, x=52, y=39)-> |		   |
|			|				  |		  |	Place(id=7, x=49, y=36)-> |		   |
|			|				  |		  |	Place(id=6, x=32, y=17)-> |		   |
|			|				  |		  |	Place(id=8, x=12, y=92)-> |  	   |
|			|				  |		  |	Place(id=3, x=51, y=63)	  |		   |
 
#### 