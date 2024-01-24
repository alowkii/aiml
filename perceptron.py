import numpy as np

theta = 1
epoch = 1


class Perceptron:
    def __init__(self, input_size, learning_rate=0.05):
        self.learning_rate = learning_rate
        self.weights = np.zeros(input_size + 1)  # zero init for weights and bias

    def predict(self, x):
        return np.dot(x, self.weights[1:]) + self.weights[0]  # X.W + B

    def train(self, x, y, weights):
        for inputs, label in zip(x, y):
            net_in = self.predict(inputs)
            print("\n", net_in)
            if net_in > theta:
                y_out = 1
            elif net_in < -theta:
                y_out = -1
            else:
                y_out = 0

            if y_out != label:  # updating the net on incorrect prediction
                self.weights[1:] += (
                    self.learning_rate * label * inputs
                )  # W = alpha * Y * X
                self.weights[0] += self.learning_rate * label  # B = alpha * Y
            print(
                f"{inputs[0]}\t{inputs[-1]}\t\t {net_in:.2f}\t\t {label}\t\t {y_out}\t\t {(self.weights[0]):.2f}\t\t {self.weights[1:]}"
            )


x = []
x.append(np.array([1, 1]))
x.append(np.array([1, -1]))
x.append(np.array([-1, 1]))
x.append(np.array([-1, -1]))
y = np.array([-1, 1, 1, -1])
perceptron = Perceptron(2)

for i in range(epoch):
    print(f"\nEpoch {i + 1}")
    weights = perceptron.weights
    print("Initial Weights", weights)
    print("X1\tX2\t\t Net\t\t T\t\t Y\t\t B\t\t Weights")
    perceptron.train(x, y, weights)
