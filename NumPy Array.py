# Get information about NumPy Array
import numpy as np

def collect_info(array):
    return "Shape: {}; dimensions: {}; length: {}; size: {}".format(array.shape, array.ndim, array.shape[0], array.size)

# NumPy Array or List Check
import numpy as np

def custom_sum(arg1, arg2):
    if type(arg1) is np.ndarray and type(arg2) is list or type(arg2) is np.ndarray and type(arg1) is list:
        return 'One argument is a list'
    elif type(arg1) is np.ndarray and type(arg2) is np.ndarray:
        return arg1 + arg2
    elif type(arg1) is list and type(arg2) is list:
        return 'Both arguments are lists, not arrays'
