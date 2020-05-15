import pandas as pd
import plotly.express as px
import fiona


def open_(shp, df=None):
    features = list(fiona.open(shp))
    ids = [f["id"] for f in features]
    if df is None:
        df = pd.DataFrame(columns=["ID", ])
    geo_json = dict(type="FeatureCollection", features=features)
    fig = px.choropleth(geojson=geo_json, locations=ids, labels=dict(locations="e"))
    return fig
