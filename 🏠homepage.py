import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("地震災害防治分析—以美濃地震為例")

st.header("前言")
markedown1="流程(前言)內文"
st.markdown(markedown1)

st.header("分析")
markedown2="分析內文"
st.markdown(markedown2)

st.header("分工表")
work = {
  '學號':["s1043032","s1043038","s1043048"],
  '姓名':["楊宇農","劉家芸","蔡雨潔"],
  '項目':["a","b","c"],
}
df=pd.DataFrame(work)
st.table(df)

st.header("歷史地震展示")
data1="https://raw.githubusercontent.com/liuchia515/gisappreport/refs/heads/main/data/%E6%AD%B7%E5%8F%B2%E8%B3%87%E6%96%99.csv"
df= pd.read_csv(
  data1,
  header=0,
  names=["date","time","lat","lon","depth","ML",],
)
point = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    id="history earthquake",
    get_position=["lon", "lat"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    get_radius="ML",
)
view_state = pdk.ViewState(
    latitude=23.5, longitude=121, controller=True, zoom=7, pitch=30
)
chart = pdk.Deck(
    point,
    initial_view_state=view_state,
    tooltip={"text": "{date}, {time}\nML: {ML}"},
)
st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")

