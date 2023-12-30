import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

def readFile(filename):
    fp = open(filename ,'r')    
    data = fp.readlines()
    f = [] #frequency values
    y = [] #correspoding y values 
    for i in data:
        i = i.split()
        f.append(float(i[0]))
        y.append(float(i[1])) 
    f = np.array(f)
    y = np.array(y)
    plt.plot(f,y) #plotting original noisy curve
    return f , y

def nlfunc_given_2(f,T,h , c , k): # 4 parameters
    return (2*h*(f**3)/(c*c))*(1/(np.exp((h*f)/(k*T))-1))

def main_Fn(filename):
    (f,y) = readFile(filename)
    ini_guess = [4990 , 6.6e-34 , 3e8 , 1.38e-23] #initial temperature guess 
    (T , h, c ,k) , _ = curve_fit(nlfunc_given_2 , f , y , ini_guess)
    print(f"The estimated values are:- \n1) T = {T} \n2) h = {h} \n3) c = {c} \n4) k = {k}")
    
    y1 = nlfunc_given_2(f, T, h ,c ,k) #y value with estimated temperature
    plt.plot(f,y1) #plotting estimated curve
    
    plt.legend(['Noisy Original' , 'Estimated Curve'])
    plt.xlabel("Frequency")
    plt.ylabel("Intensity")
    plt.savefig("dataset3_2_plot")
       
main_Fn(sys.argv[1])
    