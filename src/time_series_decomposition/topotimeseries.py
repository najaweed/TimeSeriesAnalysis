import numpy as np


class TopoTimeSeries:
    def __init__(self,
                 time_series:np.ndarray
                 ) -> None:
        self.time_series = time_series
        

    def _get_tier2_space_condition_epsilon(self) -> float:
        " find upper-band radios of Distance Metric open Ball to keep it tier2 aka Hausdorff"
        pass

    def _get_cech_distance(self) -> float:
        " find lower-band radios of Distance Metric open Ball to keep it connected topology" 
        pass

    def _spatio_temporal_open_ball(self):
        " a distance metric which is product of spatio and temporal distance metric "
        " temporal distance metric would be asymmetric in time,example, 3 lag in past and 1 lag in future "
        " spatio temporal is bounded from below and above by tier-2 radios and cech radios"

        " temporal distance are discretized by time frame sampling rate"
        " spatio distance can be quantized or continuous and depends on variance/std or backward random walk variance"
        
        " or even hyperbolic half plane backward as distance metric for spatio-temporal  "

        " this open ball act as threshold indicator"
        pass

    def find_jumps(self):
        " based on spatio-temporal distance metric and time series, try to find most possible jump in time series "
        " a method should be a threshold based on rolling variance to scale metric distance radios to avoid threshold parameter"
        " but there be a min window of observation as a parameter"
        " recursive identify jumps by: X@t - X@t-1 > threshold_scaled_distance_metric(aka threshold)@t-1 " 
        " threshold dynamically changed during recursion and bounded between tier-2 radios and cech radios"
        
        """ use this prompt to generate formula
        Assume you are a mathematical data analyst tasked with detecting jumps in the mean 
        and variance of a time series. One potential approach to this problem is to use 
        Kullback-Leibler (KL) divergence between two normal distributions. Specifically, at time t:

        The first normal distribution has a mean equal to the value of the time series at 
        time t1 and a variance equal to the rolling variance up to time t1.
        The second normal distribution has a mean equal to the value at time t and a variance 
        equal to the rolling variance up to time t1 scaled by a factor.

        Assume that the variances are related by a scaling factor. Please provide your 
        thoughts on this method, and derive the formula for detecting a jump in the time 
        series using KL divergence between these two distributions.
        """

        pass