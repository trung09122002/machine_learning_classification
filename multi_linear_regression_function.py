import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y):

    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    beta_1 = numerator / denominator
    beta_0 = y_mean - beta_1 * x_mean

    y_pred = beta_0 + beta_1 * x
    sse = np.sum((y - y_pred) ** 2)
    mse = np.mean((y - y_pred) ** 2)

    return (f"y = {beta_0:.2f} + {beta_1:.2f}x"), mse, beta_0, beta_1, sse

def plot_regression(x, y, beta_0, beta_1):
    plt.scatter(x, y, color='blue', label='Data points')
    plt.plot(x, beta_0 + beta_1 * x, color='red', label='Regression line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression')
    plt.grid()
    plt.legend()
    plt.show()

def main():
    x1 = np.array([41, 54, 63, 54, 48, 46, 62, 61, 64, 71])
    x2 = np.array([21, 30, 63, 54, 25, 46, 26, 61, 45, 17])
    x3 = np.array([4, 9, 36, 5, 6, 23, 62, 16, 43, 12])

    y = np.array([1250, 1380, 1425, 1425, 1450, 1300, 1400, 1510, 1575, 1650])

    print(f"phuong trinh hoi quy 1: {linear_regression(x1, y)[0]}")
    print(f"SSE1: {linear_regression(x1, y)[4]:.2f}")
    print(f"MSE1: {linear_regression(x1, y)[1]:.2f}")

    print(f"phuong trinh hoi quy 2: {linear_regression(x2, y)[0]}")
    print(f"SSE2: {linear_regression(x2, y)[4]:.2f}")
    print(f"MSE2: {linear_regression(x2, y)[1]:.2f}")

    print(f"phuong trinh hoi quy 3: {linear_regression(x3, y)[0]}")
    print(f"SSE3: {linear_regression(x3, y)[4]:.2f}")
    print(f"MSE3: {linear_regression(x3, y)[1]:.2f}")

    beta_0 = linear_regression(x1, y)[2] + linear_regression(x2, y)[2] + linear_regression(x3, y)[2]
    sse = linear_regression(x1, y)[4] + linear_regression(x2, y)[4] + linear_regression(x3, y)[4]
    mse = linear_regression(x1, y)[1] + linear_regression(x2, y)[1] + linear_regression(x3, y)[1]

    print(f"phuong trinh hoi quy: y = {beta_0:.2f} + {linear_regression(x1, y)[3]:.2f}x1 + {linear_regression(x2, y)[3]:.2f}x2 + {linear_regression(x3, y)[3]:.2f}x3")
    print(f"SSE: {sse:.2f}")
    print(f"MSE: {mse:.2f}")

    # Vẽ đồ thị hồi quy cho từng biến độc lập
    plot_regression(x1, y, linear_regression(x1, y)[2], linear_regression(x1, y)[3])
    plot_regression(x2, y, linear_regression(x2, y)[2], linear_regression(x2, y)[3])
    plot_regression(x3, y, linear_regression(x3, y)[2], linear_regression(x3, y)[3])

if __name__ == '__main__':
    main()