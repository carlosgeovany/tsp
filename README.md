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


### To plot the problem

`calculate_tour --coordinates_file [file full path] problem-png --filename [full path with file extension .png, jpg]`


### For a problem with coordinates only

`calculate_tour --coordinates_file [file full path] --filename [full path with file extension .png, jpg] solve`


### For a problem with coordinates and distances matrix

`calculate_tour --coordinates_file [file full path] --distances_file [file full path]--filename [full path with file extension .png, jpg] solve`


## Solutions

Solution will be saved as a .txt file with the full problem solution with:

| algorithm | hyperparameters | cost | tour | time |

and plot as image

#### Random problem
![random](https://github.com/carlosgeovany/tsp/blob/master/solutions/random_solution.png)


#### att48 problem
![att48problem](https://github.com/carlosgeovany/tsp/blob/master/solutions/att48_problem.png)

![att48solution](https://github.com/carlosgeovany/tsp/blob/master/solutions/att48_solution.png)


#### qatar problem
![qatarproblem](https://github.com/carlosgeovany/tsp/blob/master/solutions/qatar_problem.png)

![qatarsolution](https://github.com/carlosgeovany/tsp/blob/master/solutions/qatar_solution.png)


Full solutions for this project can be found at [solutions](solutions).