#set up imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Gradient Descent for 1 variable function
def grad_desc_1D(lr , bestcost , bestx, func , ddx, range_min , range_max):
    
    #bestcost is a large initial guess for function optimum
    #bestx is an initial guess for optimum x
    #lr is the Learning rate
    xbase = np.linspace(range_min, range_max , 100) 
    ybase = func(xbase)
    
    fig, ax = plt.subplots()
    ax.plot(xbase, ybase)
    xall, yall = [], []
    lnall,  = ax.plot([], [], 'ro-')
    lngood, = ax.plot([], [], 'go', markersize=10)
    
    def animate_1D(frames):
        nonlocal bestx #to get bestx of outer function
        xall.append(bestx)
        yall.append(func(bestx))
        
        if (bestx >=range_min and bestx <=range_max): #bestx in given range or not
            bestx = bestx - ddx(bestx) * lr #update bestx
            y = func(bestx)
            lngood.set_data(bestx, y)
            lnall.set_data(xall, yall)
        else:
            bestx = range_min #if not in given range, make it range_min
            y = func(bestx)
            lngood.set_data(bestx, y)
            lnall.set_data(xall, yall)
        return bestx
            
    ani = FuncAnimation(fig, animate_1D, frames=range(1000), interval=1000, repeat=False)
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Gradient Descent for one variable function')
    plt.show()
    
    for _ in range(1000): #loop to get the optimum value of the function 
                          #because we cannot return from FuncAnimation
        opt_val = animate_1D(1)
        
    return opt_val

# Gradient Descent for 2 variable function
def grad_desc_2D(lr, bestcost, bestx, besty , func , ddx, ddy , range_min, range_max):
    # ddx and ddy are partial derivatives of the function
    
    xbase = np.linspace(range_min, range_max , 100)
    ybase = np.linspace(range_min, range_max , 100)
    
    xbase , ybase = np.meshgrid(xbase,ybase) #making 2D mesh
    zbase = func(xbase, ybase)
    
    # Create a 3D figure
    fig = plt.figure(figsize=(8, 6)) 
    ax = fig.add_subplot(111, projection='3d') #this makes a 3D subplot
    
    #plots the given function surface
    ax.plot_surface(xbase, ybase, zbase, cmap='viridis' , color = "yellow" , alpha = 0.5)  
  

    def animate_2D(frame):
        nonlocal bestx , besty #to get the outer function variables
        # Update bestx and besty if in range else change them to range values
        if (bestx >=range_min and bestx <=range_max):
            x = bestx - ddx(bestx , besty) * lr
            bestx = x
        else:
            x = range_min
            bestx = x
        
        if (besty >=range_min and besty <=range_max):
            y = besty - ddy(bestx , besty) * lr
            besty = y
        else:
            besty = range_min  
        
        z = func(bestx, besty)
        ax.scatter(bestx, besty , z , c='red', marker='o', s=250) #creates dotted scatter plot
        return bestx , besty
    
    ani = FuncAnimation(fig, animate_2D, frames=range(10000), interval=100, repeat=False)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Surface with Scatter Plot')
    plt.show()

    for _ in range(1000): #running again to get optimum values
        opt_val_x, opt_val_y = animate_2D(1)
        
    return opt_val_x , opt_val_y
    

#FUNCTION 1
def f1(x):
    return x ** 2 + 3 * x + 8

def f1_prime(x):
    return 2*x + 3


#FUNCTION 2
def f3(x, y):
    return x**4 - 16*x**3 + 96*x**2 - 256*x + y**2 - 4*y + 262

def df3_dx(x, y):
    return 4*x**3 - 48*x**2 + 192*x - 256

def df3_dy(x, y):
    return 2*y - 4


#FUNCTION 3
def f4(x,y):
    return np.exp(-(x - y)**2) * np.sin(y)

def df4_dx(x, y):
    return -2 * np.exp(-(x - y)**2) * np.sin(y) * (x - y)

def df4_dy(x, y):
    return np.exp(-(x - y)**2) * np.cos(y) + 2 * np.exp(-(x - y)**2) * np.sin(y)*(x - y)


#FUNCTION 4
def f5(x):
    return np.cos(x)**4 - np.sin(x)**3 - 4*np.sin(x)**2 + np.cos(x) + 1

def f5_prime(x):
    return (-4)*(np.cos(x)**3)*(np.sin(x)) + (-3)*(np.sin(x)**2)*(np.cos(x)) + (-8)*np.sin(x)*np.cos(x) - np.sin(x)


a1 = grad_desc_1D(0.1 , 10000 , 5 , f1, f1_prime , -5 , 5)
print(f"Minima of f1 = {f1(a1)}\nPoint of Minima = {a1}")


b1,b2 = grad_desc_2D(0.05 , 10000 , 6 , 6 , f3 , df3_dx , df3_dy , -10 , 10)
print(f"\nOptimum of f2 occurs at (x,y) = ({b1},{b2})\nOptimum value of f2 = {f3(b1,b2)}")


c1, c2 = grad_desc_2D(0.2 , 1000 , 1 , 1, f4 , df4_dx , df4_dy , -np.pi , np.pi)
print(f"\nOptimum of f4 occurs at (x,y) = ({c1},{c2})\nOptimum value of f4 = {f4(c1,c2)}")


d1 = grad_desc_1D(0.05 , 1000 , 0.1 , f5, f5_prime , 0 , 2*np.pi)
print(f"\nOptima of f5 = {f5(d1)}\nPoint of Optima = {d1}")