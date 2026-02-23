import numpy as np
from scipy.interpolate import interp1d

def interpolate_temperatures(times, temperatures, regular_times):
    intrp = interp1d(times, temperatures, kind = 'linear' )
    return intrp(regular_times)

# Example data: times (in seconds) and corresponding temperature measurements (in degrees Celsius)
times = np.array([0, 3, 7, 10, 15])
temperatures = np.array([22.0, 23.5, 24.0, 23.0, 22.5])

# Regular intervals where you want to estimate temperatures
regular_times = np.arange(0, 16, 1)  # 0, 1, 2, ..., 15

interpolated_values = interpolate_temperatures(times, temperatures, regular_times)
print(interpolated_values)
