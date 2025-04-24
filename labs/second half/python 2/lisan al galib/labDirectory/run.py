from spice import *

data_path = 'spice_locations2.txt'
K, init_centers = 4, None
centers, labels, time_taken = kmeans(data_path, K, init_centers)
print('Time taken for the algorithm to converge:', time_taken)
visualise(data_path, labels, centers)