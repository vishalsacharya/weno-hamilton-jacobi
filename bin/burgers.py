from wenohj.solver import Solver
import numpy as np
import matplotlib.pyplot as plt


def get_alpha(x, t, u, u_x_plus, u_x_minus):
    f1 = np.abs(u_x_plus + 1.0)
    f2 = np.abs(u_x_minus + 1.0)

    return np.maximum(f1, f2)


def flux(x, t, u, u_x):
    return (u_x + 1)**2 / 2.0

lb = -1.0
rb = 1.0
ncells = 320
T = 3.5 / np.pi**2

s = Solver(lb, rb, ncells, flux, get_alpha, 'periodic', cfl=0.1)
x = s.get_x()
u0 = -np.cos(np.pi * x)
solution = s.solve(u0, T)

plt.plot(x, solution)
plt.show()
