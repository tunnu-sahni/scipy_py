# find root of the equation


from scipy.optimize import root

from math import  cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)



from scipy.optimize import root

from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

print(myroot)



from scipy.optimize import root

from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 1)

print(myroot)


# finding minima


from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)