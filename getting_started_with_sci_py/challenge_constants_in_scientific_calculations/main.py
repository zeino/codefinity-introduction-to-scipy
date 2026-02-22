from scipy.constants import h, c

def photon_energy(frequency):
    energy = h * frequency
    return energy

# Example usage:
energy = photon_energy(5e14)
print(energy)
