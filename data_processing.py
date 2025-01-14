import csv
import numpy as np

def load_data(filepath):
    with open(filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data_list = [dict(row) for row in csv_reader]
    return data_list

def calc_features(data_row):
    feature_vector = [
        float(data_row['Population']),
        float(data_row['Net migration']),
        float(data_row['GDP ($ per capita)']),
        float(data_row['Literacy (%)']),
        float(data_row['Phones (per 1000)']),
        float(data_row['Infant mortality (per 1000 births)'])
    ]
    return np.array(feature_vector, dtype=np.float64)
