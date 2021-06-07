# Import required libraries
import numpy as np
import statistics as st
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc
from scipy.signal import find_peaks as fp
import math


# Compute histogram bins
def compute_bins(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    min_boundary = -1.0 * (min_val % desired_bin_size - min_val)
    max_boundary = max_val - max_val % desired_bin_size + desired_bin_size
    n_bins = int((max_boundary - min_boundary) / desired_bin_size) + 1
    bins = np.linspace(min_boundary, max_boundary, n_bins)
    return bins

# Compute distance between two histograms
def bdm(h1, h2):
    k = len(compute_bins(h1, 10)) - 1
    h1size = len(h1)
    h2size = len(h2)
    size = 1/math.sqrt(h1size*h2size*k*k)
    sum = 0
    h1freq, _, _ = plt.hist(h1, bins=k)
    h2freq, _, _ = plt.hist(h2, bins=k)
    for i in range(k):
        sum += math.sqrt(h1freq[i] * h2freq[i])
    dd = size * sum
    bdm = math.sqrt(1-dd)
    return round(bdm, 2)

