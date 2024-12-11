import streamlit as st
import leafmap.foliumap as leafmap
import pydeck as pdk
import pandas as pd
import numpy as np
st.title("3D模擬值分布圖")
url="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E6%A8%A1%E6%93%AC%E6%95%B8%E5%80%BC.csv"
data = pd.read_csv(
    url,
    header=0,
    names=[
      "id",
      "x",
      "y",
      "邏輯樹",
      "AbrahamsonEtAl2014",
      "BooreAtkinson2008",
      "CampbellBozorgnia2008",
      "ChiouYoungs2008",
      "LinLee2008SInter",
    ],
)

selectable_columns = ['邏輯樹', 'AbrahamsonEtAl2014','BooreAtkinson2008','CampbellBozorgnia2008','ChiouYoungs2008','LinLee2008SInter']
options = st.selectbox('選擇一個GMPE呈現', selectable_columns)
if options:
    filtered = data[options]
    st.pydeck_chart(
        pdk.Deck(
            initial_view_state=pdk.ViewState(
                latitude=23.5,
                longitude=121,
                zoom=7,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=filtered,
                    get_position="[x, y]",
                    get_radius="selectable_columns",
                    auto_highlight=True,
                    elevation_scale=50,
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )
    st.markdown("選取縣市資料表")
    st.dataframe(filtered)
