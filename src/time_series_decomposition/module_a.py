import matplotlib.pyplot as plt
import ruptures as rpt
import numpy as np

# Parameters
n = 1000  # Number of time points
trend_slope = -0.4  # Slope of the trend
n_jumps = 3  # Number of jumps in trend
jump_magnitude = np.random.randint(50,100, n_jumps)  # Magnitude of jumps
seasonality_period = 5  # Seasonality period (e.g., every 100 time points)
seasonality_amplitude = 10  # Amplitude of seasonality

noise_std = 2  # Standard deviation of noise

# Generate time points
time = np.arange(n)

# Generate upward/downward trend
trend = trend_slope * time

# Add jumps in trend
for i in range(n_jumps):
    jump_time = np.random.randint(0, n)
    trend[jump_time:] += np.random.choice([-1, 1]) * jump_magnitude[i]

# Generate seasonality
seasonality = seasonality_amplitude * np.sin(2 * np.pi * time / seasonality_period)

# Generate noise
noise = np.random.normal(0, noise_std, n)

# Combine all components
time_series = trend + seasonality + noise

# detection
algo = rpt.Pelt(model="rbf").fit(time_series)
result = algo.predict(pen=2)
print(result)
# display
rpt.display(time_series, [], result)
plt.savefig("figure.png")
