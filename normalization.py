import numpy as np

def normalize_features(feature_list):
    feature_matrix = np.array(feature_list)
    min_vals = feature_matrix.min(axis=0)
    max_vals = feature_matrix.max(axis=0)
    normalized_matrix = (feature_matrix - min_vals) / (max_vals - min_vals)
    return normalized_matrix.tolist()
