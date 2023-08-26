import numpy as np
import matplotlib.pyplot as plt
import math

# Function to compute the logistic map
def Existing_logistic_map(u, x0, num_iterations):
    x_values = [x0]
    for _ in range(num_iterations):
        x_next = u * x_values[-1] * (1 - x_values[-1])
        x_values.append(x_next)
    return x_values

# Function to compute the sine map
def Existing_sine_map(r, x0, num_iterations):
    x_values = [x0]
    for _ in range(num_iterations):
        x_next = r * math.sin(math.pi * x_values[-1])
        x_values.append(x_next)
    return x_values

# Function to draw logistic map
def draw_logisticmap(context):
    u_values = context['u_values']
    x0_values = context['x0_values']
    num_iterations = context['num_iterations']
    
    # Create a new figure for the plot
    plt.figure(figsize=(20, 10))
    
    # Iterate through u_values and x0_values to create plots
    for u in u_values:
        for x0 in x0_values:
            x_values = Existing_logistic_map(u, x0, num_iterations)
            plt.plot([u] * (num_iterations + 1), x_values, ',k', alpha=0.05)
    
    # Set plot limits, labels, and title
    plt.xlim(0, 4)
    plt.ylim(0, 1)
    plt.xlabel("u")
    plt.ylabel("x(n)")
    plt.title("Existing Logistic Map")
    plt.grid(True)
    
    # Save the plot as an image and then close the figure
    plt.savefig("results/figures/exist_logistic_map.png")
    plt.close()

# Function to draw sine map
def draw_sinemap(context):
    # Create a new figure for the plot
    plt.figure(figsize=(20, 10))
    
    # Extract values from the context dictionary
    r_values = context['r_values']
    x0_values = context['x0_values']
    num_iterations = context['num_iterations']
    
    print (num_iterations)  # Print the number of iterations
    
    # Iterate through r_values and x0_values to create plots
    for r in r_values:
        for x0 in x0_values:
            x_values = Existing_sine_map(r, x0, num_iterations)
            plt.plot([r] * (num_iterations + 1), x_values, ',k', alpha=0.05)
    
    # Set plot limits, labels, and title
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel("r")
    plt.ylabel("x(n)")
    plt.title("Existing Sine Map")
    plt.grid(True)
    
    # Save the plot as an image and then close the figure
    plt.savefig("results/figures/exist_sine_map.png")
    plt.close()

# Context dictionary for sine map
context_sinemap_map = {
    "r_values": np.linspace(0.01, 0.99, 500),
    "x0_values": np.linspace(0.01, 0.99, 500),
    "num_iterations": 200
}

# Context dictionary for logistic map
context_losgistic_map = {
    "u_values": np.linspace(0.1, 4, 500),
    "x0_values": np.linspace(0.01, 0.99, 500),
    "num_iterations": 200
}

if __name__ == "__main__":
    draw_logisticmap(context_losgistic_map)  # Call function to draw logistic map
    draw_sinemap(context_sinemap_map)  # Call function to draw sine map
