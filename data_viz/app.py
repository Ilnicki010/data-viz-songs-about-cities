import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import os

st.set_page_config(layout="wide")

cwd = os.getcwd()
data_input = pd.read_csv(cwd + '/../creating_dataset/Data_merged.csv',index_col=[0]);
data = data_input.copy()
data.dropna(inplace=True)


data['lat'] = pd.to_numeric(data['lat'])
data['long'] = pd.to_numeric(data['long'])


st.title('Songs about cities in the U.S.')

options = st.multiselect(
    'Select states',
    np.unique(data['State']),
    np.unique(data['State']))

data = data[data['State'].isin(options)]

map_data = pd.DataFrame(
    np.column_stack([data['lat'],data['long']]),
    columns=['lat', 'lon'])


st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state=pdk.ViewState(
         latitude=37.0902,
         longitude=-95.7129,
         zoom=3,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=map_data,
            get_position='[lon, lat]',
            radius=15000,
            elevation_scale=500,
            elevation_range=[0, 1000],
            pickable=True,
            autoHighlight=True,
            extruded=True,
         ),
     ],
 ))

st.write('*Created by Dominik Ilnicki, read more about this project [here](https://medium.com/@dominikilnicki/data-viz-songs-about-cities-in-the-u-s-69043faa1a7b).*')