import pandas as pd 
import numpy as np 
import scipy.stats as st 
from statsmodels.stats.weightstats import ztest as ztest

chat_id = 1141722952 # Ваш chat ID, не меняйте название переменной 
 
def solution(x: np.array) -> bool: 
    alpha = 0.08
    p_value=ztest(x, value=500, alternative = 'larger')
    return p_value < alpha # Ваш ответ, True или False
