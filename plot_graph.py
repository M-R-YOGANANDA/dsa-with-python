import time
import numpy as np
import matplotlib.pyplot as plt

        
elements = []
tim = []
for j in range(1, 6):
    elements.append(j * 500)
    array = np.sort(np.random.randint(1, 1000, j * 500))
    
    

    stime = time.perf_counter()

#call function

  
    etime = time.perf_counter()
    
    ttime = etime - stime
    tim.append(ttime)

plt.plot(elements, tim, label='label', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('title')
plt.legend()
plt.grid(True)
plt.show()
