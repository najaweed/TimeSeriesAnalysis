import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from typing import Union, Dict, Any

class StationarityTest:
    """
    Class for performing the Augmented Dickey-Fuller (ADF) test for stationarity.
    
    Attributes:
        data (pd.Series or np.ndarray): The time series data to be tested.
        method("str"): method for testing stationarity 
        result (tuple): The result of the ADF test, stored after calling `compute`.
    """

    
    def __init__(self, data: Union[pd.Series, np.ndarray],  method="adf"):
        """
        Initialize the stationarity test with time series data.

        Args:
            data (pd.Series or np.ndarray): The time series data to be tested.
        """
        if not isinstance(data, (pd.Series, np.ndarray)):
            raise TypeError("Data must be a pandas Series or a NumPy ndarray.")
        
        self.data = data
        self.method = method
        self.result = self.compute(method=method)


    def compute(self,method) -> None:
        """
        Compute the  test statistic and store the results.
        """
        if method == "adf":
            return adfuller(self.data)
        else:
            return
    
    def visualize(self) -> None:
        """
        Visualize the time series data along with its rolling mean and standard deviation.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.data, label='Original Data', color='blue')
        plt.plot(self.data.rolling(window=12).mean(), label='Rolling Mean', color='red')
        plt.plot(self.data.rolling(window=12).std(), label='Rolling Std Dev', color='black')
        plt.legend(loc='best')
        plt.title('Time Series Visualization with Rolling Statistics')
        plt.show()

    def test(self) -> Dict[str, Any]:
        """
        Perform the ADF test and return the results.

        Returns:
            dict: A dictionary containing the ADF statistic, p-value, and critical values.
        """
        if self.result is None:
            self.compute()
        
        return {
            'ADF Statistic': self.result[0],
            'p-value': self.result[1],
            'Critical Values': self.result[4],
            'Used Lag': self.result[2],
            'Number of Observations': self.result[3]
        }

    def summary(self) -> str:
        """
        Provide a summary of the ADF test results.

        Returns:
            str: A summary report of the ADF test results.
        """
        if self.result is None:
            self.compute()
        
        summary_str = (
            f"ADF Statistic: {self.result[0]:.4f}\n"
            f"p-value: {self.result[1]:.4f}\n"
            f"Critical Values:\n"
        )
        for key, value in self.result[4].items():
            summary_str += f"    {key}: {value:.4f}\n"
        
        return summary_str
