import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from textwrap import wrap
def function(xi,y):
    n=3
    theta,psi=y[0],y[1]
    dtheta=-psi/xi**2
    dpsi=(theta**n)*(xi**2)
    return [dtheta,dpsi]


A=np.loadtxt('datasun.dat',skiprows=1)
mass_dist_sun=A[:,0]
radius_dist_sun=A[:,1]
temperature_dist_sun=A[:,2]
density_dist_sun=A[:,3]
pressure_dist_sun=A[:,4]
Y=solve_ivp(function,[1e-3,10],[1,0],max_step=0.01)
Y_radius=Y.t[0:691]
Y_density=Y.y[0][0:691]
Y_mass=Y.y[1][0:691]

plt.rcParams.update({'font.size':34})
"""Mass comparison"""
plt.figure('Mass')
plt.grid()
plt.plot((Y_radius/Y_radius[-1])*radius_dist_sun[-1],
         (Y_mass/Y_mass[-1])*mass_dist_sun[-1],'--',linewidth=4,
         label='Mass Distribution of an $n=3$ Lane-Emden Polytrope')
axes = plt.gca()
axes.set_xlim([0,1])
title='Mass comparison between an $n=3$ Lane-Emden polytrope and the Standard Solar Model'
plt.title('\n'.join(wrap(title,60)))
plt.plot(radius_dist_sun,mass_dist_sun,linewidth=4,label='Mass Distribution of the Sun')
plt.xlabel(r'$r/r_{\odot}$')
plt.ylabel(r'$M/M_\odot$')
plt.legend()
"""Temperature comparison"""
plt.figure('Temperature')
plt.grid()
plt.plot((Y_radius/Y_radius[-1])*radius_dist_sun[-1],
         np.log(Y_density*temperature_dist_sun[0]),'--',linewidth=4,
         label='Temperature Distribution of an $n=3$ Lane-Emden Polytrope')
axes = plt.gca()
axes.set_xlim([0,1])
plt.plot(radius_dist_sun,np.log(temperature_dist_sun),linewidth=4,
         label='Temperature Distribution of the Sun')
title='Temperature comparison between an $n=3$ Lane-Emden polytrope and the Standard Solar Model'
plt.title('\n'.join(wrap(title,60)))
plt.xlabel(r'$r/r_{\odot}$')
plt.ylabel(r'$\log T$')
plt.legend()
"""Density comparison"""
plt.figure('Density')
plt.grid()
plt.plot((Y_radius/Y_radius[-1])*radius_dist_sun[-1],
         np.log(Y_density*density_dist_sun[0]),'--',linewidth=4,
         label='Density Distribution of an $n=3$ Lane-Emden Polytrope')
axes = plt.gca()
axes.set_xlim([0,1])
plt.plot(radius_dist_sun,np.log(density_dist_sun),linewidth=4,
         label='Density distribution of the Sun')
title='Density comparison between an $n=3$ Lane-Emden polytrope and the Standard Solar Model'
plt.title('\n'.join(wrap(title,60)))
plt.xlabel(r'$r/r_{\odot}$')
plt.ylabel(r'$\log \rho$')
plt.legend()
"""pressure comparison"""
plt.figure('Pressure')
plt.grid()
plt.plot((Y_radius/Y_radius[-1])*radius_dist_sun[-1],
         np.log(Y_density**4*pressure_dist_sun[0]),'--',linewidth=4,
         label='Pressure Distribution of an $n=3$ Lane-Emden Polytrope')
axes = plt.gca()
axes.set_xlim([0,1])
plt.plot(radius_dist_sun,np.log(pressure_dist_sun),linewidth=4,
         label='Pressure Distribution of the Sun')
title='Pressure comparison between an $n=3$ Lane-Emden polytrope and the Standard Solar Model'
plt.title('\n'.join(wrap(title,60)))
plt.xlabel(r'$r/r_{\odot}$')
plt.ylabel(r'$\log P$')
plt.legend()








