# ASSIGNMENT 5 - GRADIENT DESCENT BY EE22B025

## Overall Approach

### Understanding the Problem:
- The main goal of the problem is to optimise the given functions and to find the __optimum values__ of each function.
- We need to use _Gradient Descent_ to find the optimum values of the functions.
- Two of the given functions are __2__ variable functions, thus we also need to extend Gradient Descent for 2 variables.
- We also need to use __Matplotlib__ and __FuncAnimation__ to plot the graph and display animation of the Gradient Descent.

### Implementing Gradient Descent:
- I have created 2 seperate _Grad_Desc_ functions : 
    1) __Grad_Desc_1D()__ - For one variable functions
    2) __Grad_Desc_2D()__ - For two variable functions
- The overall structure of both these functions is same.
- For _Grad_Desc_1D_ : 
    - We start with an initial guess of bestx and then check whether $x\in(RangeMin , RangeMax)$.
    - If yes, then we update the bestx by using the equation
    $$bestx = bestx - f'(x)dx$$
    - If no, then we update the bestx and make it equal to Range_min.
    - This keeps repeating until we reach the loop limit.
    - The idea is to keep finding an $x$ such that $f(x)$ is smaller than the previous _bestcost_ value until we reach a __local/global minima__.
- For _Grad Desc_2D_ :
    - This function also follows the same logic as its 1D counterpart, with the difference being an extra variable $z$.
    - Here, we have inital guess of $bestx$ and $besty$ along with $bestcost$.
    - Again, we check $x\in(RangeMin , RangeMax)$ and $y\in(RangeMin , RangeMax)$ and update them using the same equation as given above.
    - Again, this keeps repeating till we reach the loop limit.

### What Parameters does the Gradient Descent Function take?
1) ___Lr___ - This is the Learning Rate which tells us how big the step size between each iteration is.
2) ___bestcost, bestx , besty___ have been explained above.
3) ___func___ - This is the given function which we need to optimise.
4) ___ddx/ddy___ - This is again the (partial) derivative of the given function.
5) ___range_min and range_max___ - These give the range in which we need to optimise the given function.

### What types of Function can Gradient Descent Function take?
- Usually functions which are ___differentiable___, ___smooth___, ___well behaved___ are taken as inputs to the Gradient Descent function.
- There should be ___well defined gradient___ everywhere in the optimisation range.
- Functions which are ___discontinuous___, ___having peaks and valleys___ with ___not a well-defined derivative___ are usually restricted for the use of Gradient Descent.
- When a function has too many _local minima/maximas_ and if the bestcost value reaches a local optima, then it doesn't move from there again as the _gradient is 0_ at that point and we end up having a __wrong answer__.
- Also, if we keep the _Learning Rate_ very high, then we won't be able to find a good optimum solution because the $bestx$ value will keep jumping.

## PROBLEM 1
- This function is a simple __Quadratic 1D Polynomial__. The __gradient__ has also been provided.
- Since this is a 1D polynomial, I have used the grad_Desc_1D function to implement Gradient Descent.
- The parameters I used are : 
    - LR = 0.1
    - bestcost = 10000
    - bestx = 5
    - Range of Optimisation = $[-5,5]$
- The Final PLOT after Gradient_Descent is :  
![Plot showing Gradient Descent of $f1(x)$](fig_1.png){ width=75% }  
- The RESULT is :
    -  __Minima of f1 = 5.75__
    - __Point of Minima = -1.4999999999999996__  
    
## PROBLEM 2
- This function is a simple __2D Polynomial__. The __Partial Derivatives__ have also been provided.
- Since this is a 2D polynomial, I have used the grad_Desc_2D function to implement Gradient Descent.
- The parameters I used are : 
    - LR = 0.05
    - bestcost = 10000
    - bestx = 6 , besty = 6
    - Range of Optimisation = $[-10,10]$
- The Final PLOT after Gradient_Descent is :  
![Plot showing Gradient Descent of $f1(x)$](fig_2.png){ width=75% }  
- The RESULT is :
    - Optimum of f2 occurs at __(x,y) = (4.049561394942729,2.0000000000000018)__
    - Optimum value of f2 = __2.000006033566251__

## PROBLEM 3
- This function is a complicated __2D Function__. The __Partial Derivatives__ have been provided.
- Since this is a 2D function, I have used grad_Desc_2D() to implement Gradient Descent.
- The parameters I used are : 
    - LR = 0.05
    - bestcost = 10000
    - bestx = 6 , besty = 6
    - Range of Optimisation = $[-10,10]$
- The Final PLOT after Gradient_Descent is :  
![Plot showing Gradient Descent of $f1(x)$](fig_3.png){ width=75% }  
- The RESULT is :
    - Optimum of f4 occurs at __(x,y) = (-1.5707963267948954,-1.5707963267948957)__
    - Optimum value of __f4 = -1.0__
    
## PROBLEM 4
- This function is a 1D ___Trigonometric Function___. The __gradient__ has not been provided, so I created the `f5_prime() function`.
- Since this is a 1D function, I have used grad_Desc_1D() to implement Gradient Descent.
- The parameters I use for this function are : 
    - LR = 0.2
    - bestcost = 1000
    - bestx = 1, besty = 1
    - Range of Optimisation = $[-pi,pi]$
- The reason for a smaller learning rate is because this function, being trigonometric, must have a lots of peaks and valleys and hence if we take longer steps, we might end up at the wrong optima. So if we take smaller Learning rate, the steps will also be smaller.
- The Final PLOT after Gradient_Descent is :  
![Plot showing Gradient Descent of $f1(x)$](fig_4.png){ width=75% }  
- The RESULT is :
    -  __Optima of f5 = -4.045412051572552__
    - __Point of Optima = 1.661660812043789__
    
## INSTRUCTIONS ON HOW TO RUN THE CODE:
- You need to have the `numpy`, `matplotlib` and `FuncAnimation` libraries in the environment.
- You can then run the code and you will be able to see the __final plots__ and __optimum values__.