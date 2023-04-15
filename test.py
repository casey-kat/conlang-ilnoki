import numpy 
from collections import Counter
import matplotlib.pyplot as plt

counter = Counter()

for i in range(5000):
	# num = round(numpy.random.normal(0, 2.2))
	num = round(pow(numpy.random.uniform(0.0,1.0) * 2, 2)) + 2
	counter[num] += 1
  
plt.bar(counter.keys(), counter.values(), width = 0.5, color = ['blue'])

plt.xlabel('x - range')
plt.ylabel('y - random number')
plt.show()