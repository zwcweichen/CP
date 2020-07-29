# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:17:16 2020

@author: User
"""
from numpy import *
from matplotlib.pyplot import *

#常數設定
I1=20
I2=40
I3=60

def f(r,t):
    omega1,omega2,omega3=r
    fomega1 = ((I2-I3)/I1)*omega2*omega3
    fomega2 = ((I3-I1)/I2)*omega3*omega1
    fomega3 = ((I1-I2)/I3)*omega1*omega2
    return np.array([fomega1,fomega2,fomega3],float)

def leapfrog(r,h,T):
    t=0
    w1,w2,w3=r
    r_half = r+0.5*h*f(r,t+0.5*h)
    r_int=r+h*f(r_half,t+0.5*h)
    t+=h
    ww1,ww2,ww3,tt=[w1],[w2],[w3],[t]
    while t<T:
        r_half=r_half+h*f(r_int,t)
        r_int=r_int+h*f(r_half,t+0.5*h)
        t+=h
        ww1.append(r_int[0])
        ww2.append(r_int[1])
        ww3.append(r_int[2])
        tt.append(t)
    plot(tt,ww1)
    plot(tt,ww2)
    plot(tt,ww3)
    show()
    scatter(tt,I1*(array(ww1,float))**2+I2*(array(ww2,float))**2+I3*(array(ww3,float))**2)
    return ww1,ww2,ww3,tt
t_0 = 0.0
t_max = 1
N = 500
h = (t_max - t_0) / N
leapfrog([1,100,4],h,t_max)




        
