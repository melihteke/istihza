import matplotlib.pyplot as plt
plt.plot([0, 1, 2, 3, 4], [0, 10, 20, 30, 40], label="First Line")
plt.plot([5, 6, 7, 8, 9], [50, 60, 70, 80, 90], label="Second Line")
plt.xlabel("numbers")
plt.ylabel("numbers multiplied by ten")
plt.title("Generated Graph\nCheck it out")
plt.legend()
plt.show()