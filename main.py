from data_processing import load_data, calc_features
from normalization import normalize_features
from hac import hac
from visualization import fig_hac

if __name__ == "__main__":
    csv_data = load_data('countries.csv')
    
    feature_list = [calc_features(row) for row in csv_data]
    country_labels = [row['Country'] for row in csv_data]
    
    normalized_data = normalize_features(feature_list)
    
    Z = hac(normalized_data)
    
    fig_hac(Z, country_labels)
