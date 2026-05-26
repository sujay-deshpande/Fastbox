import numpy as np

# Euclidean distance calculation using numpy functionality for point driven points
def calculate_distance(p1, p2):
    # print("points: ",point1,print)
    p1 = np.array(p1)
    p2 = np.array(p2)
    
    return np.sqrt(np.sum(np.square(p1 - p2)))