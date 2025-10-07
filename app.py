import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs import binomial_price
st.set_page_config(page_title='Option Pricer', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('Multi-tool Binomial Option Pricer')