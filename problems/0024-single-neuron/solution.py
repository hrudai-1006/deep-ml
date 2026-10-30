import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []

    for x in features:
        z = sum(x[i] * weights[i] for i in range(len(weights))) + bias
        sigmoid = 1 / (1 + math.exp(-z))
        probabilities.append(round(sigmoid, 4))

    mse = sum((p - y) ** 2 for p, y in zip(probabilities, labels)) / len(labels)

    mse = round(mse, 4)

    return probabilities, mse