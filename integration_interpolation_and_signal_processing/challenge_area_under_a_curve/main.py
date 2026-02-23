from scipy.integrate import quad

def velocity(t):
    # Example velocity function: v(t) = 3 * t**2 + 2 * t + 1
    return 3 * t**2 + 2 * t + 1

def total_distance_traveled(start_time, end_time):
    # Use quad to integrate the velocity function from start_time to end_time
    distance, error = quad(velocity, start_time, end_time)
    return float(distance)

# Sample calls
distance1 = total_distance_traveled(0, 5)
distance2 = total_distance_traveled(2, 8)
print(distance1)
print(distance2)
