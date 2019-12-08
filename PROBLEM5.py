import math #for user-inputs with lib-dependent characteristics
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
user = input('Input function x(n): ')
reses = [] #storage
xn = [] #storage of x(n) variables
gibx = list(range(0,200))

#y(n)
for n in range (0,200):
    #y(n) = -1.5x(n) + 2x(n + 1) - 0.5x(n+2)
    if n == 0:
        #convert string input into a formula that python can utilize
        n0 = -1.5*(eval(user))  #evaluate x(n) where n = 0, the result will then be multiplied to -1.5
        n = n + 1               #x(n + a); in this case, a = 1
        nm1 = 2*(eval(user))
        n = n + 2
        nm2 = -.5*(eval(user))
        res1 =  n0 + nm1 + nm2 #compilation of formulas
        reses.append(res1)  #storing of all values of y(n) into a single list

    #y(n) = 0.5x(n + 1) - 0.5x(n-1)
    elif n > 0 and n <= 198:
        n = n + 1
        n0 = .5*(eval(user))
        n = n - 1
        nm1 = -.5*(eval(user))
        res2 = n0 + nm1 
        reses.append(res2)

    #y(n) = 1.5x(n) - 2x(n - 1) + 0.5x(n - 2)
    elif n == 199:
        n0 = 1.5*(eval(user))
        n = n - 1
        nm1 = -2*(eval(user))
        n = n - 2
        nm2 = .5*(eval(user))
        res3 = n0 + nm1 + nm2
        reses.append(res3)
        break #just in case the program enters an endless loop

#x(n) / user-defined function
for n in range(0,200):
    xn.append(eval(user)) #evaluate x(n) with values of n ranging from 0 to 199

#plotting
plt.grid() #add grid
plt.xlabel('n elements')
plt.ylabel('x and y elements')
plt.plot(gibx,reses)
plt.plot(gibx,xn)
blu = mpatch.Patch(color = 'blue', label = 'y(n)') #add custom legend
orange = mpatch.Patch(color = 'orange', label = 'x(n)')
plt.legend(handles = [blu,orange]) #apply legend to graph
plt.show() #show graph