import matplotlib.pyplot as plt

ax = plt.subplot(211)
ax2 = plt.subplot(212, sharex=ax, sharey=ax)
ax.plot(range(50))
ax2.plot(range(50))
ax.cla()
plt.show()

# test comment
