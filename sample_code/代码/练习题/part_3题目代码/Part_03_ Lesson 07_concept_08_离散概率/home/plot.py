def plot_probability(normalized_counts):
	import matplotlib.pyplot as plt
	plt.bar([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], normalized_counts)
	plt.title('Probability of the Sum when Rolling Two Dice')
	plt.xlabel('Sum of Rolling Two Dice')
	plt.ylabel('Probability')
	plt.show()