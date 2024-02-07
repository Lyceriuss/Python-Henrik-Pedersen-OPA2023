import matplotlib.pyplot as plt

# Function to plot the graph based on x and y data


def plot_graph(x_data, y_data, graph_type='scatter'):
    if graph_type == 'line':
        plt.plot(x_data, y_data, marker='o')
    elif graph_type == 'scatter':
        plt.scatter(x_data, y_data)
    plt.title('Graph Calculator Plot')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()

# Main function to collect data points and call the plotting function


def graph_calculator():
    X = []
    Y = []
    number_of_points = int(input("How many points do you want to enter? "))

    for i in range(number_of_points):
        x = int(input(f"Enter x value for point {i+1}: "))
        y = int(input(f"Enter y value for point {i+1}: "))
        X.append(x)
        Y.append(y)

    graph_type = input("Enter graph type ('line' or 'scatter'): ").lower()
    plot_graph(X, Y, graph_type)


# Call the graph calculator function
graph_calculator()
