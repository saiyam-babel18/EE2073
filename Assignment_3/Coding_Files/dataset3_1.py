import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy as sp
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

def nlfunc_given_1(f,T):
    h = sp.constants.h #planck's constant
    c = sp.constants.c #Speed of Light
    k = sp.constants.k #Boltzmann's Constant
    return (2*h*(f**3)/(c*c))*(1/(np.exp((h*f)/(k*T))-1))

def main_Fn(filename):
    (f,y) = readFile(filename)
    ini_guess = [6492.227] #initial temperature guess 
    (T) , _ = curve_fit(nlfunc_given_1 , f , y , ini_guess)
    print("Estimated Temp is :" , float(T) , "K")
    
    y1 = nlfunc_given_1(f, T) #y value with estimated temperature
    plt.plot(f,y1) #plotting estimated curve
    
    plt.legend(['Noisy Original' , 'Estimated Curve'])
    plt.xlabel("Frequency")
    plt.ylabel("Intensity")
    plt.savefig("dataset3_1_plot")
       
main_Fn(sys.argv[1])
    