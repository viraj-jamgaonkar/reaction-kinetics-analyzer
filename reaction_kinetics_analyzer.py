# Reaction Kinetics Analyzer
# Author: Viraj Jamgaonkar
# Python + NumPy + Matplotlib

import numpy as np
import matplotlib.pyplot as plt

def reaction_kinetics():
    print("\n--- Reaction Kinetics Analyzer ---")
    
    # Input values
    C0 = float(input("Enter initial concentration (mol/L): "))
    k = float(input("Enter rate constant (1/s): "))
    t_start = float(input("Enter start time (s): "))
    t_end = float(input("Enter end time (s): "))
    t_step = float(input("Enter time step (s): "))
    
    # Time array
    t = np.arange(t_start, t_end + t_step, t_step)
    
    # Concentration array using first-order kinetics
    C = C0 * np.exp(-k * t)
    
    # Display results in table form
    print("\nTime (s)\tConcentration (mol/L)")
    for i in range(len(t)):
        print(f"{t[i]:.2f}\t\t{C[i]:.4f}")
    
    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(t, C, marker='o', color='b', label='C(t) = C0 * exp(-kt)')
    plt.title('First-Order Reaction Kinetics')
    plt.xlabel('Time (s)')
    plt.ylabel('Concentration (mol/L)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the function
if __name__ == "__main__":
    reaction_kinetics()
