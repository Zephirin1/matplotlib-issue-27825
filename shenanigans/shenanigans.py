import matplotlib.pyplot as plt

ax = plt.subplot(211)
ax2 = plt.subplot(212, sharex=ax)
ax.plot(range(50))
ax2.plot(range(50))
ax.cla()
ax.set_xlim(0, 20)
plt.show()
