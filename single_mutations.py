import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint
import ternary
e = 0.1
u = 0.03
def F(vec, t):
    x, y = vec
    f_x = 1 - x - (e +2)*y
    f_y = (e + 2)*x + (e + 1)*(y - 1)
    phi = e*(x**2 + y**2 - x - y + x*y)
    x_dot = x*(f_x - phi) - u*x
    y_dot = y*(f_y - phi) + u*x
    return [x_dot, y_dot]
vec0 = [0.8,0]
t = np.linspace(0, 1000, 10000)
sol = odeint(F, vec0, t)
# x, y = sol
# sol = x, y, 1 - x - y
sol2 = []
for x, y in sol:
    sol2.append([x, y, 1-x-y])

#for v in vec0:
    #sol = odeint(F, v, t)
    #plt.plot(sol[:, 0], sol[:, 1])

figure, tax = ternary.figure(scale = 1.0)
tax.boundary()
tax.gridlines(multiple = 0.2, color = "black")
tax.set_title("Single Mutations", fontsize = 20)
tax.plot(sol2, linewidth = 2.0, label = "trajectory")
tax.ticks(axis = 'lbr', multiple = 0.2, linewidth = 1, tick_formats = "%.1f")
tax.legend()
tax.show()

# Samyak is learning git