import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Vaule",fontsize=14)
plt.plot(squares)
plt.tick_params(axis='both',labelsize=14)
plt.show()
