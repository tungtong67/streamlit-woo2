import streamlit as st
import pandas as pd
import numpy as np
st.write("""
# 첫번째 앱
Hello *world!*
""")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
