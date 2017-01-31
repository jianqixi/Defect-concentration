#/usr/bin/env python

## This is the script to calculate the defect concentration based on Arrenhuis equation
import numpy as np 
import sys, os, math
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib.pyplot import style
plt.switch_backend('agg')

### Define the possible parameters
C=[]   #Defect concentration, unit: 1/cm^3
kb=8.617332478e-5  #The Boltzmann constant, unit: eV/K
N=9.4266e22   #The number of sublattice sites per unit volume, unit: atom/cm^3
#N_Li_Frenkel=36N; N_Ta_Frenkel=36N ;N_O_Frenkel=18*6N; N_LiTaO3=6*6*3*17*16N; N_Ta2O5=15*18*17*14*2N; N_Li2O=15*18N; TaLi+4VLi=30N; 5TaLi+4VTa=90N; 2TaLi+VTa+3VLi=360N

#def defect_concentration(N, temp)
Hf=input('the formation energy of defect:')
f=open('output.txt','w')
for T in range(300,1501,2):
   C=N*math.exp(-Hf/(kb*T))
   #C=math.exp(-Hf/(kb*T))
   f.write('{0} {1}\n'.format(T,C))
   plt.semilogy(T,C,'bo',linewidth=2.0)
   plt.xlim(290,1510)
f.close()   
plt.savefig('test',bbox_inches='tight')  
#plt.savefig('con',dpi=600)
