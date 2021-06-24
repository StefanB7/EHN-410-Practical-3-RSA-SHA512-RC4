import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MaxNLocator
#...
ax = plt.figure().gca()
#...
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
y = np.array([9630, 9598, 9593, 9592, 9592, 9592, 9592, 9592, 9592, 9592]) # 100000

y1 = np.array([78584, 78509, 78501, 78498, 78498, 78498, 78498, 78498, 78498, 78498]) # 1 mil

plt.plot([1,2,3,4,5,6,7,8,9,10],y)
plt.grid()
plt.xlabel("# rounds")
plt.ylabel("# primes found")
# plt.plot(y)

ax.annotate('9592', xy=(4, 9592), xytext=(4.5, 9598),
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )


#...
ax = plt.figure().gca()
#...
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()


# 664579 less than  10 million
# 78498 less than 1 million
# 9592 less than 100 000 

import time

test = RSA(10)

final = []

for j in range(10):
    print("round ",j+1)
    iCount = 0
    a = time.time()
    for i in range(1000000):
        flag = test.miller_rabin(i+1,j+1)
        if flag:
            iCount += 1

    print(iCount)
    final.append(iCount)
    print("Tyd (s): ",time.time()-a)

print(final)