import numpy as np
import matplotlib.pyplot as plt

def logistic_map(u, x0, num_iterations):
    x_values = [x0]
    for _ in range(num_iterations):
        x_next = u * x_values[-1] * (1 - x_values[-1])
        x_values.append(x_next)
    return x_values

# Parameters
u_values = np.arange(3.57, 4.01, 0.01)
x0_values = np.linspace(0.01, 0.99, 100)  # Exclude 0 and 1
num_iterations = 100

# Store the sequences for different u and x0 values
sequences = []
for u in u_values:
    for x0 in x0_values:
        sequence = logistic_map(u, x0, num_iterations)
        sequences.append((u, x0, sequence))

# Create subplots for line plots
num_plots = len(u_values)
fig, axes = plt.subplots(num_plots, 1, figsize=(10, 6 * num_plots))

# Iterate over different u values and plot sequences
for i, u in enumerate(u_values):
    axes[i].set_title(f"Logistic Map for u = {u:.2f}")
    axes[i].set_xlabel("Iteration")
    axes[i].set_ylabel("x")
    for u_value, x0_value, sequence in sequences:
        if u_value == u:
            axes[i].plot(sequence, label=f"x0 = {x0_value:.2f}")
    axes[i].legend()

plt.tight_layout()
plt.savefig("line_plots.png")  # Save the figure
plt.show()

# Create scatter plot for final values
plt.figure(figsize=(10, 6))
for u, x0, sequence in sequences:
    plt.scatter([u] * len(sequence), sequence, c='black', alpha=0.1)
plt.xlabel("u")
plt.ylabel("x")
plt.title("Final Values of Logistic Map")
plt.savefig("scatter_plot.png")  # Save the figure
plt.show()
