import numpy as np
import matplotlib.pyplot as plt

def logistic_map(u, x0, num_iterations):
    x_values = [x0]
    for _ in range(num_iterations):
        x_next = u * x_values[-1] * (1 - x_values[-1])
        x_values.append(x_next)
    return x_values


u_values = np.linspace(0.01, 4, 1000)  
x0_values = np.linspace(0.01, 0.99, 1000)  
num_iterations = 50

# Create subplots to show different behaviors for various u values
plt.figure(figsize=(20, 10))

for u in u_values:
    for x0 in x0_values:
        x_values = logistic_map(u, x0, num_iterations)
        plt.plot([u] * (num_iterations + 1), x_values, ',k', alpha=0.25)

plt.xlim(0, 4)
plt.ylim(0, 1)
plt.xlabel("u")
plt.ylabel("x(n)")
plt.title("Existing Logistic Map")
plt.grid(True)
plt.savefig("Logistic_Map.png")  # Save the figure
