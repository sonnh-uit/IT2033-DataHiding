import numpy as np
import matplotlib.pyplot as plt

def logistic_map(u, x0, num_iterations):
    x = x0
    for _ in range(num_iterations):
        x = u * x * (1 - x)
    return x

# Parameters
u_values = np.arange(3.57, 4.01, 0.01)
x0 = 0.2
num_iterations = 1000

final_x_values = [logistic_map(u, x0, num_iterations) for u in u_values]

# Create scatter plot using Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(final_x_values, u_values, marker='.', color='black')
plt.xlabel("Final x Value")
plt.ylabel("u")
plt.title("Logistic Map Density Plot")
plt.gca().invert_yaxis()  # Invert the y-axis to have u increasing upwards
plt.savefig("density_plot.png")  # Save the figure