import numpy as np
import matplotlib.pyplot as plt

# Population parameters
population_mean = 0
population_std = 40 / np.sqrt(12)  # Standard deviation for uniform distribution

# Sample sizes
sample_sizes = [1, 10, 50, 1000, 4000, 5000]

# Calculate standard deviations for sample means
sample_mean_stds = population_std / np.sqrt(sample_sizes)

# Plotting the normal distribution of sample means
x = np.linspace(-30, 30, 1000)  # Range of x values for the plot

plt.figure(figsize=(10, 6))
plt.title('Central Limit Theorem - Distribution of Sample Means')
plt.xlabel('Sample Means')
plt.ylabel('Density')

# Plotting the theoretical normal distributions
for i in range(len(sample_sizes)):
    # Generate normal distribution using the calculated mean and standard deviation
    y = (1 / (sample_mean_stds[i] * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - population_mean) / sample_mean_stds[i]) ** 2
    )
    plt.plot(x, y, label=f'n = {sample_sizes[i]}')

plt.legend()
plt.show()
