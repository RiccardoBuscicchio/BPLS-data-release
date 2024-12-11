import numpy as np

yearinseconds= 31557600.0
Tobs = yearinseconds*4
dof = 1000
fmin = 10**-4
fmax = 10**-2
df = dof / Tobs
L = 8.3
c = 299792458.0
H02 = (69.8*1e3/ (3.08 * 1e22))**2
f0 = 10**-2.5