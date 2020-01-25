# lets Try Learning Neural Data Science In Python
import numpy as np
import matplotlib.pyplot as plt

# Aritmatic

# %precision(15)    ????
a = 9 / 5
print(a)
# mean
b = [1, 2, 3]
print(np.mean(b))
# Indexing
c = [4, 5, 6, 9, 20]
print(c[1])
# Random Gen
d = np.random.rand(5)
print(d)
# EXP inPy
e = 5 ** 3
print(e)
# sqrt
print(np.sqrt(abs(-5)))

# C Elegance Neural Rate Firing
F_rate = np.array([0.5, 1, 2, 4, 8, 0.25, 1, 3])
Number_Neurons = np.array([45, 15, 35, 20, 35, 25, 50, 10])
Spike_count = F_rate * Number_Neurons
print(Spike_count)
EXP_Spike_count = np.inner(Number_Neurons, F_rate)
print(EXP_Spike_count)
spikeCountCrossComparison = np.outer(F_rate, Spike_count)
print(spikeCountCrossComparison)

# C Elegance Visual System
exposure_duration = np.array([1, 2, 3, 4, 5])
light_level = np.array([1, 2, 4, 8, 16])
photon_count = np.outer(exposure_duration, light_level)
print(photon_count)

# Finding the  number of neurons which firing rate is bigger than 3
Indici_bigger_than3 = np.where(F_rate > 3)
print(Indici_bigger_than3)
Neurons_condition = np.sum(Number_Neurons[Indici_bigger_than3])
print(Neurons_condition)

# Plot the Brain Size and IQ relation
smaplesize = 10000
meaniq = 100
stdiq = 15
sampleiq = np.random.randn(smaplesize) * stdiq + meaniq
f = plt.figure()
ax = plt.hist(sampleiq, bins=20)
plt.show()


