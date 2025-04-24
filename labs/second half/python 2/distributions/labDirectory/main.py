'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility
np.random.seed(42)

# sampling from each of the six distributions


# plotting histograms for each of the distributions
# plt.subplot(3,2,1)

#Beta
sample=np.random.beta(4,20,1000000)*100
plt.subplot(3, 2, 1)
plt.hist(sample, bins=np.arange(-5, 51, 1),color='red')
plt.title("Beta")

#Exponential
sample=np.random.exponential(0.1, 1000000)*100
plt.subplot(3, 2, 2)
plt.hist(sample, bins=np.arange(-1, 51, 1),color='green',alpha=0.5)
plt.title("Exponential")

#Gamma
sample=np.random.gamma(2, 0.1, 1000000)*100
plt.subplot(3, 2, 3)
plt.hist(sample, bins=np.arange(-1, 51, 1),color='black',alpha=0.8, orientation='horizontal')
plt.title("Gamma")

#Laplace
sample=np.random.laplace(0, 0.5, 1000000)*100
plt.subplot(3, 2, 4)
plt.hist(sample, bins=np.arange(-1, 51, 1),color='orange')
plt.title("Laplace")

#Normal
sample=np.random.normal(0, 3, 1000000)
plt.subplot(3, 2, 5)
plt.hist(sample, bins=np.arange(-10, 12, 1))
plt.title("Normal")

#Poisson
sample=np.random.poisson(3, 1000000)
plt.subplot(3, 2, 6)
plt.hist(sample, bins=np.arange(-1, 12, 1))
plt.title("Poisson")

# adjust the sub-plots to fit the titles and labels
plt.tight_layout()
# save the plot as plot.png
plt.savefig('plot.png')
