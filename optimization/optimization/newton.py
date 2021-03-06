import numpy as np
import optimization.multivariable_calculus as mvc

def best(f, criticalPoints, maximize):
    globalOptimum = criticalPoints[0]
    optimumOutput = f(globalOptimum)
    for i in range(1, len(criticalPoints)):
        contender = f(criticalPoints[i])
        if (not maximize and contender < optimumOutput) or (maximize and contender > optimumOutput):
            globalOptimum = criticalPoints[i]
            optimumOutput = contender
    return globalOptimum

def optimize(f, n, convergence = 1e-4, trials=2, maxSteps = 1000, stepSize=0.1, lowerBound = -1, upperBound = 1, maximize=False):
    criticalPoints = []
    for trial in range(trials):
        coordinates = np.array([np.random.random() * (upperBound-lowerBound) + lowerBound for i in range(n)])
        convergenceSquared = convergence**2
        for i in range(maxSteps):
            grad = np.array(mvc.gradient(f, coordinates.tolist()))
            if grad.dot(grad) < convergenceSquared: # x dot x is the squared magnitude of x
                break # Optimum reached.
            H = np.array(mvc.hessian(f, coordinates.tolist()))
            step = -(np.linalg.inv(H)).dot(grad) # step to the minimum
            coordinates = coordinates + stepSize * (-step if maximize else step)
        criticalPoints.append(coordinates.tolist())
    return best(f, criticalPoints, maximize)
