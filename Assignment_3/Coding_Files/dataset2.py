import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

def readFile(filename):
    fp = open(filename ,'r')
    data = fp.readlines()
    
    x = [] #time values
    y = [] #correspoding y values 
    for i in data:
        i= i.split()
        x.append(float(i[0]))
        y.append(float(i[1]))
        
    x = np.array(x)
    y = np.array(y)
    plt.plot(x,y)
    return x , y 
    
def f1(t , A , B, C , D):
    dum = 0.8*np.pi #frequency found using trial and error
    return (A*np.sin(dum*t)) + (B*np.sin(3*dum*t)) + (C*np.sin(5*dum*t)) + D

def CreateMatrix(t): #t is x-axis parameter
    dum = 0.8*np.pi 
    M = np.column_stack( (np.sin(dum*t), np.sin(3*dum*t), np.sin(5*dum*t) , np.ones(len(t)) )) #creating M matrix 
    return M

def getCoef(M, y):
    (A, B , C , D) , _, _, _ = np.linalg.lstsq(M , y , rcond= None) 
    return A, B, C , D

def main_F(filename): #main function
    (x, y) = readFile(filename)
    M = CreateMatrix(x)
    (A, B, C , D) = getCoef(M , y)
    dum = 0.8*np.pi 
    print(f"The estimated equation using LEAST SQUARES is \n{A} sin({dum}t) + {B} sin({dum*3}t) + {C} sin({dum*5}t) + {D}")

    #plotting estimated curve
    y1 = f1(x, A , B , C , D) #getting y values with estimated co-efficients
    plt.plot(x , y1)
    
    #using Curve_fit
    (A1, B1 , C1 , D1 ) , _ = curve_fit(f1 , x , y)
    print(f"The estimated equation using CURVE_FIT is \n{A1} sin({dum}t) + {B1} sin({dum*3}t) + {C1} sin({dum*5}t) + {D1}")
    
    #plotting Curve_fit curve
    y2 = f1(x , A1, B1, C1 , D1)
    plt.plot(x , y2)

    #labelling 
    plt.xlabel("t")
    plt.ylabel("y")
    
    #legend
    plt.legend(['Noisy Original' , 'Estimated'  , 'Curve_Fit' ])
    
    plt.savefig("dataset2_noisy")
    
main_F(sys.argv[1])
