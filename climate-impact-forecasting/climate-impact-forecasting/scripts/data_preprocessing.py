
import pandas as pd
import geopandas as gpd
from sklearn.preprocessing import StandardScaler

def load_data():
    climate_data = pd.read_csv('data/raw/climate_data.csv')
    socio_economic_data = pd.read_csv('data/raw/socio_economic_data.csv')
    geospatial_data = gpd.read_file('data/raw/geospatial_data.shp')
    return climate_data, socio_economic_data, geospatial_data

def preprocess_data(climate_data, socio_economic_data, geospatial_data):
    # Example preprocessing steps
    climate_data.fillna(method='ffill', inplace=True)
    socio_economic_data = StandardScaler().fit_transform(socio_economic_data)
    geospatial_data = geospatial_data.to_crs(epsg=4326)  # Convert to a common CRS
    return climate_data, socio_economic_data, geospatial_data

if __name__ == "__main__":
    climate_data, socio_economic_data, geospatial_data = load_data()
    climate_data, socio_economic_data, geospatial_data = preprocess_data(
        climate_data, socio_economic_data, geospatial_data
    )
    climate_data.to_csv('data/processed/climate_data_processed.csv')
    pd.DataFrame(socio_economic_data).to_csv('data/processed/socio_economic_data_processed.csv')
    geospatial_data.to_file('data/processed/geospatial_data_processed.shp')
