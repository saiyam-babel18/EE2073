import numpy as np
import matplotlib.pyplot as plt
import sys

def readFile(filename):
    fp = open(filename ,'r') 
    data = fp.readlines()
    t = [] #x values
    y = [] #correspoding y values 
    
    for i in data:
        i = i.split() #splits the given data into x and y values
        t.append(float(i[0])) #appending x values to t
        y.append(float(i[1])) #appending y values to y

    t = np.array(t) 
    y = np.array(y)
    plt.plot(t,y) #original data with noise
    return t , y

def CreateMatrix(t): #t is x-axis parameter
    M = np.column_stack((t, np.ones(len(t)))) #creating M matrix
    return M

def getCoef(M, y):
    (m , c) , _, _, _ = np.linalg.lstsq(M , y , rcond= None) 
    return m ,c 

def main_F(filename): #main function
    (t, y) = readFile(filename)
    M = CreateMatrix(t)
    (m ,c) = getCoef(M , y)
    print(f"The estimated equation is {m} t + {c}")
    
    y1 = (m*t) + c #output with estimated parameters
    plt.plot(t,y1)
    
    n = np.random.randn(len(t))
    plt.errorbar(t[::25], y[::25], np.std(n), fmt='ro') #plotting errorbar every 25 data points
    
    #adding legend to the plot
    plt.legend(['Noisy Original' , 'Estimated'  , 'ErrorBar' ])
    
    #labelling x and y axes
    plt.xlabel("t")
    plt.ylabel("y")

    plt.savefig("dataset1_plot") #saving the plot as png file
    
main_F(sys.argv[1])


    