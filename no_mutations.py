import numpy as np
import matplotlib.pylab as plt
from scipy.integrate import odeint
import ternary
e = -0.1 #epsilon can be varied aroun 0, which is the critical point.
u = 0
def F(vec, t):
    x, y = vec
    x_dot = x - e*(x**3) - e*(y**2)*x + (e-1)*(x**2) - 2*x*y - e*(x**2)*y + u*(1-3*x)
    y_dot = (-1)*e*(y**3) + (2*e + 1)*(y**2) - e*x*(y**2) - e*(x**2)*y + (2*e + 2)*x*y - (e+1)*y + u*(1-3*y)
    return [x_dot, y_dot]
vec0 = [0.5,0.4]
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
tax.set_title("No Mutations", fontsize = 20)
tax.plot(sol2, linewidth = 2.0, label = "trajectory")
tax.ticks(axis = 'lbr', multiple = 0.2, linewidth = 1, tick_formats = "%.1f")
tax.legend()
tax.show()