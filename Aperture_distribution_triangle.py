# Radio Astronomy - John D. Kraus
# Arul 25.02.2025

from scipy import constants
import numpy as np
import matplotlib.pyplot as plt


c = constants.c				# Velocity of EM wave
Frequency = 200e6			# Frequency of observation
wavelength = c / Frequency
element_distance = 1.2			# Antenna's distance in elements (Meters)
theta = np.linspace(-np.pi/2,np.pi/2, 10000)	# angle


# Expression 6-38 

beta      = ( 2 * np.pi ) / wavelength
lin_amplitude = [1, 1, 1, 1, 1, 1, 1]
Dia_amplitude = [1, 2, 3, 4, 3, 2, 1]
delta_phi = np.deg2rad( [0, 0, 0, 0, 0, 0, 0] )	# phase difference b/w elements in Deg

#delta_phi = np.deg2rad( [+2, -1, +4, 0, 1, -2, -5] )

E_lin_total = 0
E_dia_total = 0

for idx in range(len(lin_amplitude)):

    xi               = idx * beta * element_distance * np.sin(theta) + delta_phi[idx]
    E_linear         = lin_amplitude[idx] * np.exp(1j * xi)
    E_diamond        = Dia_amplitude[idx] * np.exp(1j * xi)    
    E_lin_total      += E_linear
    E_dia_total      += E_diamond
    

gauss   = np.exp(-(np.rad2deg(theta)**2)/(51**2))    
Basic_Element_power_pattern = 20*np.log10(np.abs(gauss)/np.max(np.abs(gauss)))
Linear_Array_power_pattern = 20*np.log10(np.abs(E_lin_total * gauss)/np.max(np.abs(E_lin_total * gauss)))
Diamond_Array_power_pattern = 20*np.log10(np.abs(E_dia_total * gauss)/np.max(np.abs(E_dia_total * gauss)))

plt.plot(np.rad2deg(theta), Basic_Element_power_pattern, linewidth=3)
plt.plot(np.rad2deg(theta), Linear_Array_power_pattern, linewidth=3)
plt.plot(np.rad2deg(theta), Diamond_Array_power_pattern, linewidth=3) #power pattern
plt.title("Array Pattern", fontsize = 20)
plt.legend(['Basic Element', 'Linear Array', 'Diamond Array'], fontsize = 14 , loc='upper right')
plt.grid()
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xlabel('Angle [ Degree ]', fontsize = 16)
plt.ylabel('Gain [ dB ]', fontsize = 16)
plt.show()


