import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 6130040059 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, critical_values, pvalue = anderson_ksamp([x, y])
    alpha = 0.08
    if statistic > critical_values[2]:
        return True
    else:
        return False
