import matplotlib.pyplot as plt

pirate_years = range(1850, 2025, 25)
number_of_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(pirate_years, number_of_pirates_thousands, 'ro-',
         linewidth=5, markersize=5, alpha=0.35)
plt.show()


