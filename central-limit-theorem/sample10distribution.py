import numpy as np
import matplotlib.pyplot as plt

# Population parameters
population_mean = 0
population_std = 40 / np.sqrt(12)  # Standard deviation for uniform distribution

# Sample size
sample_size = 10

# Calculate the standard deviation of the sample means
sample_mean_std = population_std / np.sqrt(sample_size)

# Generate x values to represent the sample means
x = np.linspace(-20, 20, 1000)

# Calculate the normal distribution of sample means
y = (1 / (sample_mean_std * np.sqrt(2 * np.pi))) * np.exp(
    -0.5 * ((x - population_mean) / sample_mean_std) ** 2
)

# Plot the normal distribution of sample means
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title(f'Central Limit Theorem - Distribution of Sample Means (n = {sample_size})')
plt.xlabel('Sample Means')
plt.ylabel('Density')
plt.show()
