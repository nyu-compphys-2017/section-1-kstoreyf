# This is a python file! The '#' character indicates that the following line is a comment.
from __future__ import division
import numpy as np

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print "hello world!"
    print name
    return
    
    
#Implement the Riemann Sum approximation for integrals.

#Test function
def func(x):
	return x

#Right-handed Riemann Sum
def riemann_sum(f, a, b, N=10):
	w = (b-a)/N
	xs = np.linspace(a+w, b, N)
	hs = np.array([f(x) for x in xs])
	rsum = sum(hs * w)
	return rsum

print riemann_sum(func, 0, 3)
	
