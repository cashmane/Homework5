import numpy as np
import matplotlib.pyplot as plt
import sys

def group(values, n):
    '''Takes in a list, and groups them into sub-lists with each sub-list
        containing n values. (Used for grouping points into 3s for
        Simpson's rule)'''
    return [values[i:i+n] for i in range(0, len(values), n-1)]

def lowerSum(xlist, ylist):
    '''A function which takes in two lists (values of x and values of f(x)),
        and calculates the numerical integral using the lower sum method.'''
    areaList = []
    for i in range(len(xlist[:-1])):
        area = ylist[i]*(xlist[i+1]-xlist[i])
        areaList.append(area)    
    rsum = 0
    for a in areaList:
        rsum += a
    return rsum

def trapSum(xlist, ylist):
    '''Function which takes in two lists (values of x, f(x)), and calculates
        the numerical integral using the trapezoidal method.'''
    areaList = []
    for i in range(len(xlist[:-1])):
        b1 = ylist[i]
        b2 = ylist[i+1]
        area = 0.5*(b1 + b2)*(xlist[i+1]-xlist[i])
        areaList.append(area)
    tsum = 0
    for a in areaList:
        tsum += a
    return tsum

def simpsonSum(xlist, ylist):
    '''Function which takes in two lists (values of x, f(x)), and calculates
        the numerical integral using Simpons rule.'''
    groupx = group(xlist, 3)
    groupy = group(ylist, 3)
    areaList = []
    for i in range(len(groupx)):
        if len(groupx[i]) == 3:
            
            h = (groupx[i][2] - groupx[i][0])/2
            F1 = groupy[i][0]
            F2 = groupy[i][1]
            F3 = groupy[i][2]
            area = (h/3)*(F1+(4*F2)+F3)
            areaList.append(area)   
        elif len(groupx[i]) == 2:
            print('!')
            b1 = groupy[i][0]
            b2 = groupy[i][1]
            h = (groupx[i][1] - groupx[i][0])
            area = 0.5*(b1 + b2)* h
            areaList.append(area)
        else:
            break
    sSum = 0
    for a in areaList:
        sSum += a
    return sSum
        
def f(x):
    '''Function we are evaluating.'''
    return x**2

def analyticInt(x):
    '''The analytic integral of the function we are evaluating.'''
    return x**3/3

def percError(true, aprox):
    '''Calculates the relative error, given the analytic value and the
        calculated numerical value.'''
    return ((true - aprox)/true)*100

if __name__ == '__main__':
    #sys.exit(1)
    myList = np.arange(0, 30, 1)
    

    hList = [0.1, 0.01, 0.001, 0.0001]#, 0.00001, 0.000001]
    lowerErrorList = []
    trapErrorList = []
    simpErrorList = []
    numOfSteps = []
    for h in hList:
        xValues = np.arange(0, 1, h)
        yValues = f(xValues)
        print(len(xValues))
        numOfSteps.append(len(xValues)) #X Axis values
        lower = lowerSum(xValues, yValues)
        lowerError = percError(analyticInt(1), lower)
        lowerErrorList.append(lowerError) #Y Axis values
        trap = trapSum(xValues, yValues)
        trapError = percError(analyticInt(1), trap)
        trapErrorList.append(trapError) #Y Axis values
        simp = simpsonSum(xValues, yValues)
        simpError = percError(analyticInt(1), simp)
        simpErrorList.append(simpError) #Y Axis values
        print(lower)
        print(lowerError)
        print(trap)
        print(trapError)
        print(simp)
        print(simpError)

    plt.plot(numOfSteps, lowerErrorList, color='blue',label='Lower Sum')
    plt.plot(numOfSteps, trapErrorList, color='red',label='Trapezoidal Sum')
    plt.plot(numOfSteps, simpErrorList, color='green',label="Simpson's Rule")
    #plt.ylim(0 ,0.5)
    #plt.xlim(0, 10000)
    plt.legend()
    plt.title('Relative Error in Numerical Integration Methods')
    plt.xlabel('Number of Steps')
    plt.yscale('log')
    plt.ylabel('Relative Error (%)')
    plt.show()






        
        
        
