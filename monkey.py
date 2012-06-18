from math import *

def f(n):
    return (n-1) / 5.0 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n 

def is_int(n):
    return abs(n-int(n)) < 0.0000001
   
# Enter code here.
def main():
	n=0
	found = False
	while not found:
		n = n+1
		found = is_int(f6(float(n)))
	print n

def foo(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)


def update(mean1, var1, mean2, var2):
	    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
	    new_var = 1/(1/var1 + 1/var2)
	    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
	    new_mean =mean1+mean2
	    new_var =var1+var2
	    return [new_mean, new_var]

print predict(10., 4., 12., 4.)