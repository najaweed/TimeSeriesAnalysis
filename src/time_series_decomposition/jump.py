import numpy as np
import pandas as pd


class FindJump:
    def __init__(self,
                time_series:np.ndarray,
                window_size:int = 16,
                ):
        self.time_series = self._normalize(time_series)
        self.window_size = window_size
        self.jumps = self.jump_detection() 

    @staticmethod    
    def rolling_mean_std(time_series: np.ndarray, span_window=10):
        ewm = pd.Series(time_series).ewm(span=span_window, adjust=False)
        mean = ewm.mean().iat[-1]
        std = ewm.std().bfill().iat[-1]
        return mean, std
    
    def jump_metric(self, current_price:float, last_mean:float,last_std:float) -> float:
        last_std = 0.00001 if last_std==0.0 else last_std
        dist = (current_price-last_mean)**2 / 2*last_std**2
        return dist
    
    def is_jump(self,time_series:np.ndarray, threshold_jump=1e-4) -> bool:
        # drop last data for mean and std
        last_mean, last_std = self.rolling_mean_std(time_series[:-1],self.window_size)
           
        dist=self.jump_metric(time_series[-1],last_mean,last_std)
        if dist > threshold_jump:
            return True
        else:
            return False
    
    def _normalize(self,time_series:np.ndarray) -> np.ndarray:
        time_series -= np.min(time_series)
        time_series /= np.max(time_series) - np.min(time_series)
        return time_series

        
    def jump_detection(self) -> dict:
        jump_dict = {}
        time_series = self.time_series  
        window_size = self.window_size
        i = window_size
        while i < len(time_series):
            ts = time_series[i-window_size:i]
            if self.is_jump(ts):
                jump_dict[i] = ts[-1]
                i += window_size  # Shift i by window_size to skip
            else:
                i += 1  # Increment by 1 if no jump is detected
        return jump_dict

    def transform_jumps(self):
        index_jumps = list(self.jumps)
        print(np.mean(self.time_series[index_jumps[0]-10:index_jumps[0]]))
        print(np.mean(self.time_series[index_jumps[0]:index_jumps[0]+10]))

        pass

    @staticmethod
    def fit_line(data: np.ndarray) -> np.ndarray:
        """
        Fits a straight line to the given 1D time series data.
        """
        n = data.size
        x = np.arange(n)
        # Solve for the best fit line y = mx + b using least squares
        A = np.vstack([x, np.ones(n)]).T
        m, b = np.linalg.lstsq(A, data, rcond=None)[0]
        
        return np.array(m * x + b)

# import matplotlib.pyplot as plt
# import stochastic.processes as sto 
# fbm = sto.CauchyProcess()
# ts = fbm.sample(1000)
# #times = fbm.times(1000)
# df = pd.DataFrame(ts, columns=['Value'])

# findJump= FindJump(ts,window_size=32)
# jumps=findJump.jump_detection()
# for key , val in jumps.items():
#     plt.scatter(x=key,y=val)
# plt.plot(findJump.time_series)
# plt.show()