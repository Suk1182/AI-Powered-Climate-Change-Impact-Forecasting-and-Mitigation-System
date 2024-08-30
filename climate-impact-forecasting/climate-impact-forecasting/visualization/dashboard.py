
import plotly.express as px
import pandas as pd

def create_dashboard():
    data = pd.read_csv('data/processed/climate_data_processed.csv')
    fig = px.line(data, x='date', y='temperature')
    fig.show()

if __name__ == "__main__":
    create_dashboard()
