# ASSIGNMENT 6 - Travelling Salesman BY EE22B025
## GOAL OF THE PROBLEM :
- The main goal of the problem is to find a _sequence of numbers_ which specifies the order in which to visit the cities. This order of cities must be such that the distance travelled from one city to other should be __minimum__.
 
## Explanation of Functions and Approach:
### ___Unpack_Coord(cities)___ :
- The purpose of this function is that, given a list of tuples (which contains the x and y coordinates), it returns two numpy arrays containing the x and y coordinates seperately, thus _unpacking_ the list of tuples.
- We need this function because we require x and y coordinates seperately so that we can rearrange them in the correct order of cities which is given by the ___tsp(cities)___ function.

###  ___distance(cities , cityorder)___ :
- This function basically takes in the sequence of city coordinates(_cities_) and the _cityorder_ as well and then finds the distance it takes to traverse across the cities in the order specified.
- The function first gets the x and y coordinates and then rearranges these coordinates in the given _cityorder_ and then returns the __total distance__ including the distance of returning back to the first city.

### ___tsp(cities)___ :
- This is the function where the ___Simulated Annealing Algorithm___ is used.
- The basic algorithm of Simlulated Annealing in context of __TSP__ is explained below :
    1) First we define all the Parameters - T , Decay_Rate, initial_guess.
    2) The idea is that for every iteration, we _randomly change_ the cityorder. But this change should be only a little random. In this case, I have randomly selected _two elements_ from the cityorder and __interchanged them__ to generate a new cityorder. Then I find the distance $d$ corresponding to this cityorder.
    3) We then compare $d$ with $Initial Guess$. 
        - If $d < InitialGuess$ then we update Intial_Guess to $d$.
        - If $d > InitialGuess$ then we generate a random probabilty $p$ in $[0,1)$ and then compare that with $e^{-\frac{\Delta E}{kT}}$, which depends on the Parameters. Again, if $p < e^{-\frac{\Delta E}{kT}}$ then update Initial_Guess, else proceed as it is using `pass` command. 
        - In our case, $\Delta E$ is the (_Current_Random_Distance - Previous_Guess_).
    4) We keep repeating this process until the __For Loop Limit__ is reached and then return the final _cityorder_.
    
## Result for the given test file (4 cities) : 
- Upon running the code with the given 4 city coordinates, we get the following result : 
    1) The City Order is ___[2 1 3 0]___ and the minimum distance is ___d = 14.64154124236167.___
    2) The first random distance guess generated was ___17.794818674426676.___
    3) The percentage improvement is ___17.7201998500645.___
- NOTE:
    - Even if we rotate the city_order array, we will get the same minimum distance.
    - Every time you run the code, the _first random distance_ changes and thus _percentage improvement_ also changes. Along with these two, the _city_order_ and the _graph_ may also change.
    - But the __minimum distance__ remains the same.

## PLOT of `4 city test case` :
- __NOTE regarding Legend__:
    1) The RED dots represent the intermediate cities.
    2) The GREEN dot represents the First/Starting City.
    3) The BLUE line represents the connection between 1st and 2nd city.
    4) The YELLOW line represents the connection between 1st and Last city.  
![Plot showing connection of 4 Cities.](Plot_A6.png){ width=75% }  

## RESULT and PLOT of `40 city test case` :
- Upon running the code with the given 4 city coordinates, we get the following result : 
    1) The City Order is ___[15 23 25 16  1 31  8 35  2  7 32  5 29  0  9 28 37 39 11 17 19 20 30 33
  6 36  4 12 27 13 24 18 26 21 38 10 22 34  3 14]___ and the minimum distance is ___d = 7.155829730703569___
    2) The first random distance guess generated was ___20.365669083061096.___
    3) The percentage improvement is ___64.86327210012782.___  
- The Plot is given below:
***
***
***
***  
![Plot showing connection of 4 Cities.](tsp_40.png){ width=75% }  

## Instructions on how to run the Code : 
- `numpy` and `matplotlib` libraries should be available.
- You have to make sure the test file should be in the same directory as the Python Notebook.
- You need change the filename to your "testfile name" in the code (where Reading_File() is called).
- Run ALL the cells at once.
