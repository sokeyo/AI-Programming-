import numpy as np
from matplotlib import pyplot as plt

# plotting the graph
x, y = np.loadtxt('C:\School\Yr2-1-Semester\AI-Programming\python\Assignment\population_vs_profit.txt', delimiter=',', unpack=True)
plt.plot(x,y,'o', color = 'black', label='Profit Analysis!')

plt.xlabel('POPULATION')
plt.ylabel('PROFIT')
plt.title('POPULATION VS PROFIT')
plt.legend()
plt.show()


# iterator function
def gradient_descent_runner(points, starting_m, starting_b, learning_rate, num_iterations):
    m = starting_m
    b = starting_b

    for i in range(num_iterations):
        m, b = step_gradient(m, b, np.array(points), learning_rate)

    return m, b

#To calculate the gradient descent, hence optimal values for m and b using partial derivatives of m and b
def step_gradient(current_m, current_b, points, learning_rate):


    n = float(len(points))

    sum_m = 0
    sum_b = 0

    for point in points:
        sum_m += -1 * point[0] * (point[1] - (current_m * point[0] + current_b))
        sum_b += -1 * (point[1] - (current_m * point[0] + current_b))

    # partial derivative of m
    m_gradient = (2 / n) * sum_m

    # partial derivative of b
    b_gradient = (2 / n) * sum_b

    #updated gradient
    m_new = current_m - (learning_rate * m_gradient)

    #updated y-intercept
    b_new = current_b - (learning_rate * b_gradient)

    return m_new, b_new

#mean squared error function
def compute_error_for_given_points(m, b, points):
    # sum of squared errors
    sum_error = 0
    for i in range(len(points)):
        point = points[i]
        sum_error += (point[1] - (m * point[0] + b)) ** 2

    return sum_error / float(len(points))


def run():
    points = np.genfromtxt("data1.txt", delimiter=",")

    # Learning rate of 0.0001 determines how fast our model is going to learn.

    learning_rate = 0.0001

    # y = mx + b. m = slope and b = y-intercept
    initial_b = 0
    initial_m = 0
    initial_error = compute_error_for_given_points(initial_m, initial_b, points)

    print("Starting gradient descent m=", initial_m, " and b=", initial_b, " with an error=", initial_error)

    # Depends on the size of the dataset
    num_iterations = 1000

    [m, b] = gradient_descent_runner(points, initial_m, initial_b, learning_rate, num_iterations)

    error = compute_error_for_given_points(m, b, points)

    print("After 1000 iterations m=", m, " and b=", b, " with an error=", error)
    print("y =", m, "x", "+" ,b )


if __name__ == "__main__":
    print("LINEAR REGRESSION USING GRADIENT DESCENT")
run()