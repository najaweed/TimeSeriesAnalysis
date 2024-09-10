import numpy as np
import time
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from stochastic.processes.continuous import FractionalBrownianMotion
import stochastic.processes as sto 


def ols_univariate(X, y):
    """
    Computes the OLS regression coefficients for a univariate time series.
    
    Parameters:
    X (numpy.ndarray): 1D array of input features.
    y (numpy.ndarray): 1D array of target values.

    Returns:
    tuple: A tuple containing the intercept and slope of the OLS regression.
    float: Execution time in seconds.
    """
    # Start time
    
    # Add a column of ones to X for the intercept
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
    
    # Compute OLS coefficients using the normal equation
    theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
    
    # End time
    
    # Extract coefficients
    intercept, slope = theta_best
    
    # Plotting the time series and the regression line
    plt.figure(figsize=(10, 6))
    plt.plot(X, y, label='Original Time Series', color='blue')
    plt.plot(X, intercept + slope * X, label='OLS Regression Line', color='red', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Univariate Time Series with OLS Regression Line')
    plt.legend()
    plt.savefig("figure.png")

    
    return (intercept, slope), execution_time


#fbm =  FractionalBrownianMotion(hurst=0.7, t=1)
fbm = sto.CauchyProcess()
s = fbm.sample(1000)
times = fbm.times(1000)

coefficients, execution_time = ols_univariate(times,s)
print(f"Intercept: {coefficients[0]}, Slope: {coefficients[1]}")
print(f"Execution Time: {execution_time:.6f} seconds")
